# import pandas as pd
# import matplotlib.pyplot as plt
   
# maintainence = 1200


# # Create second chart for Maintainence
# data = {'Year': [1, 2, 3, 4, 5],
#         'Cost': [maintainence, maintainence + (12000 * 0.0058), maintainence + (12000 * 0.008), maintainence + (12000 * 0.0085), maintainence + (12000 * 0.009)]
#     }

# df = pd.DataFrame(data,columns=['Year','Cost'])
# df.plot(x ='Year', y='Cost', kind = 'bar', rot=0)
# plt.title(f"Approximate maintainence cost for car over 5 years")
# plt.xlabel("Year")
# plt.ylabel("Cost ($)")
# plt.axis([-1, 5, maintainence-50, maintainence + (12000 * 0.009) + 50])
# plt.show()
# plt.savefig("maintainence.png", dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,)



# # data = {'Year': [0, 1, 2, 3, 4, 5],
# #         'Car Value': [50000, 40000, 38000, 32000, 18000, 16000]
# #        }
  
# # df = pd.DataFrame(data,columns=['Year','Car Value'])
# # df.plot(x ='Year', y='Car Value', kind = 'line')
# # plt.title("Approximate Depreciation rate over 5 years")
# # plt.xlabel("Year")
# # plt.ylabel("Value ($)")
# # plt.savefig("Plot1.jpg", dpi=None, facecolor='w', edgecolor='w',
# #         orientation='portrait', format=None,
# #         transparent=False, bbox_inches=None, pad_inches=0.1,)
# # plt.show()


# # import shutil

# # original = r'C:\Users\vhsha\OneDrive\Documents\Visual Studio Code.ba\finance\depreciation.png'
# # target = r'C:\Users\vhsha\OneDrive\Documents\Visual Studio Code.ba\finance\static\depreciation.png'

# # shutil.move(original,target)
