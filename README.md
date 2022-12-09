# Carparison
#### Video Demo:  https://youtu.be/7N24X1a1bnU
#### Extensions: Python, HTML, CSS, Javascript and SQL
#### Libraries: Flask, MatPlotLib, Shutil, Pandas, CS50, Datetime
#### Description:
Carparison is a web app designed to help you see predictions on the depreciation of value and how much maintenance will cost on your vehicle. It is designed in a way that you only need to input 4 major numbers, Fuel Economy, Price, Regional Tax and Cost of Gas for 1 litre. With these values inputted, Carparison will be able to create nearly accurate predictions on that car!

How Carparison can create these predictions of values for maintenance is because of the extensive research done on the topic of car depreciation over time and mileage and car maintenance costs based on fuel economy and mileage (again). With this research, we were able to create an equation that gives you an approximate value of much the car will be worth over the span of 5 years, and how much maintenance will cost.

### Framework and Structure
Index (Homepage):
    Car Make: This is just to give a name to the results
    Fuel Economy: This is how many litres of gas the car uses for every 100 km driven
    Price: This is how many dollars the car will cost
    Regional Tax: This is a percentage of how much tax is applied in your region
    Gas: This is the cost of gas for each region

Results:
    Depreciation Table: Shows table of values of how much car the will be worth for 5 years
    Depreciation Chart: Shows chart to help visualize the results
    Maintenance Table: Similar to depreciation, shows values on the cost of maintenance over 5 years
    Maintenance Chart: This Shows chart to help visualize the results

Feedback:
    Form for the user to submit feedback or to suggest a change

### Assets
/carparison
⤷/static
    carparison.jpg
    carparison.png
    crash.jpg
    favicon.ico
    icon.png
    styles.css
⤷/templates
    apology.html
    help.html
    index.html
    layout.html
    results.html
⤷app.py
⤷chart.py (for testing only)
⤷helpers.py
⤷info.db (database to store info)
⤷other_code (for testing only)
⤷README.md
⤷script.txt

### How to run
To run this app locally on your own machine, it is very simple
Requirements:
⤷Python 3.9
⤷sqlite3
⤷Library: Flask
⤷Library: MatPlotLib
⤷Library: Pandas
⤷Library: Shutil
⤷Library: CS50

In your terminal, in the directory **/carparison** type **flask run**
Then click on the link provided and thats it! The app will run.

### Future Implementations
Some ideas for the future:
- Finding API to have results without needing user input
- Creating universal chart that includes all user inputs so that if a user wants to return to the page one day, they don't need to make a new query, their results are there for everyone to access
- Updating CSS and implementing more JS to improve user interface