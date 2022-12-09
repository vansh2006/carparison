# export API_KEY=pk_323ebdc536c443678eea805ef06d9e0e

import os
import pandas as pd
import matplotlib.pyplot as plt
import shutil

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
# Security: https://techmonger.github.io/4/secure-passwords-werkzeug/
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, usd
from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///info.db")

chart = None

@app.route("/index", methods=["GET", "POST"])
def index():
    """Show display for inputting details"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get inputted data from form
        make = request.form.get("make")
        mileage = float(request.form.get("mileage"))
        price = int(request.form.get("price"))
        tax = float(request.form.get("tax"))
        gas = float(request.form.get("gas"))

        # Ensure mileage was submitted
        if not request.form.get("make"):
            return apology("must provide make of car (ford escape)", 400)

        # Ensure mileage was submitted
        elif not request.form.get("mileage"):
            return apology("must provide mileage", 400)

        # Ensure price was submitted
        elif not request.form.get("price"):
            return apology("must provide price of car", 400)
        
        # Ensure tax was submitted
        elif not request.form.get("tax"):
            return apology("must provide tax (in percent)", 400)

        elif not request.form.get("gas"):
            return apology("must provide gas price (dollars per litre)", 400)



        # Ensure that inputted data is valid
        if mileage >= 20:
            return apology("inputted mileage is too high", 400)
        elif mileage <= 1:
            return apology("inputted mileage is too low", 400)

        elif price >= 2700000: # (Most expensive car, Bugatti Chiron, $2.7 Mil)
            return apology("a car cannot be this expensive", 400)
        elif price <= 1000: # (Cheapest used car)
            return apology("a car cannot be this cheap", 400)

        elif tax >= .18:
            return apology("tax cannot be this high", 400)
        elif tax <= 0.03:
            return apology("tax cannot be this low", 400)

        elif gas >= 3: # (Highest possible gas)
            return apology("gas does not cost this much")
        elif gas <= .40: # (Cheapest gas, Venezuela)
            return apology("gas is not this cheap")

        # Create id to know which data to display
        query_id = db.execute("SELECT id FROM data ORDER BY id DESC LIMIT 1")[0]["id"] + 1


        # Average Value Deprecation Per Year
        # https://www.ramseysolutions.com/saving/car-depreciation#:~:text=The%20value%20of%20your%20car%20goes%20down%20over,faster%20your%20car%E2%80%99s%20value%20will%20drop%20%28or%20depreciate%29.
        value_year1 = price * 0.8
        value_year2 = price * 0.68
        value_year3 = price * 0.63
        value_year4 = price * 0.59
        value_year5 = price * 0.41

        # Create first chart for Depreciation
        data = {'Year': [0, 1, 2, 3, 4, 5],
                'Car Value': [price, value_year1, value_year2, value_year3, value_year4, value_year5]
            }
        
        df = pd.DataFrame(data,columns=['Year','Car Value'])
        df.plot(x ='Year', y='Car Value', kind = 'line')
        plt.title(f"Approximate value for {make} over 5 years")
        plt.xlabel("Year")
        plt.ylabel("Value ($)")
        plt.savefig("depreciation.png", dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,)
        
        # Move chart (img) to /static, overwriting any other chart
        original = r'C:\Users\vhsha\OneDrive\Documents\Visual Studio Code.ba\carparison\depreciation.png'
        target = r'C:\Users\vhsha\OneDrive\Documents\Visual Studio Code.ba\carparison\static\depreciation.png'

        shutil.move(original,target)

        # approximately how much maintainence will cost based on mileage and cost
        maintainence = (price * 0.01) * (mileage / 2)


        # Create second chart for Maintainence
        data = {'Year': [1, 2, 3, 4, 5],
        'Cost': [maintainence, maintainence + (12000 * 0.0058), maintainence + (12000 * 0.008), maintainence + (12000 * 0.0085), maintainence + (12000 * 0.009)]
        }
        
        df = pd.DataFrame(data,columns=['Year','Cost'])
        df.plot(x ='Year', y='Cost', kind = 'bar', rot=0)
        plt.title(f"Approximate maintainence cost for {make} over 5 years")
        plt.xlabel("Year")
        plt.ylabel("Cost ($)")
        plt.axis([-1, 5, maintainence-50, maintainence + (12000 * 0.009) + 50])
        plt.savefig("maintainence.png", dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,)

        # Move maintainence chart (img) to /static, overwriting any other chart
        original = r'C:\Users\vhsha\OneDrive\Documents\Visual Studio Code.ba\carparison\maintainence.png'
        target = r'C:\Users\vhsha\OneDrive\Documents\Visual Studio Code.ba\carparison\static\maintainence.png'

        shutil.move(original, target)


        # Create sql table with these slots
        db.execute(
            "INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            query_id, make, value_year1, value_year2, value_year3, value_year4, value_year5, mileage, gas, tax, 1, 1, maintainence
        )


        # Redirect user to results page
        flash(f"Here are our predictions for your {make}")
        return redirect("/results")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html")

@app.route("/")
def home():
    return redirect("/index")


@app.route("/results", methods=["GET", "POST"])
def results():
    """Display Results from Inputted Data"""
    # Get last inputted data

    info = db.execute("SELECT * FROM data WHERE id = (SELECT id FROM data ORDER BY id DESC LIMIT 1)")
    print(info)

    return render_template("results.html", info=info)


@app.route("/help", methods=["GET", "POST"])
def help():
    """Show create form that allows response for feedback"""
    if request.method == "POST":
        email = request.form.get("email")
        feedback = request.form.get("feedback")
        rating = request.form.get("rating")

        db.execute("INSERT INTO feedback VALUES (?, ?, ?)", email, feedback, rating)
        print(email, feedback, rating)
        flash("Thank you for submitting this form!")
        return redirect("/help")

    else:

        return render_template("help.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
