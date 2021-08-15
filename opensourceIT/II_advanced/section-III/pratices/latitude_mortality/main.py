import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy.stats import pearsonr
import os

def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

#1: Load the data and print the column names
recordsDataFrame = pd.read_csv(getCurrentDirname()+"/lmdata.csv")
print(f"Records:\n{recordsDataFrame} \n")
print(f"Columns:\n{recordsDataFrame.columns}")

#2: Generate descriptive statistics for the data
print(recordsDataFrame.describe())

# 3: Create a line plot for the variables. Add a title and x & y axes.
#   a) Beautify the x-labels
#   b) plot a line graph
ypoints = recordsDataFrame['latitude'].to_numpy()
xpoints = recordsDataFrame['mortality'].to_numpy()

plt.xlabel("Mortality")
plt.plot(xpoints, ypoints,  marker = '.')
plt.show()

# 4: Create a scatter plot / Add title and (X,Y) axis names
ypoints = recordsDataFrame['latitude'].to_numpy()
xpoints = recordsDataFrame['mortality'].to_numpy()

plt.title("Statistics")
plt.xlabel("Mortality")
plt.ylabel("Latitude")
plt.scatter(xpoints, ypoints,  marker = '.')
plt.show()

# 5: Create a boxplot for mortality
plt.boxplot(x="mortality",data=recordsDataFrame)
plt.title("Mortality")
plt.show()

# 6: Conduct a Pearson’s correlation test for the variables
latitude = recordsDataFrame['latitude'].to_numpy()
mortality = recordsDataFrame['mortality'].to_numpy()

correlation = pearsonr(mortality, latitude)
print(f"Pearson’s correlation: {correlation}")

# 7: Create a pair plot for the data
sns.pairplot(recordsDataFrame)
plt.show()

# 09: Create a Seaborn regplot of the regression model and a 95% confidence interval
# plot the regression model y ~ x and a 95% confidence interval for that regression
sns.regplot(x="mortality", y="latitude",data=recordsDataFrame, ci=95, marker=".")
plt.show()

# 8: Type in this command: from statsmodels.formula.api import ols
# 10: Create the regression model using ols() from the statsmodel package
# 11: Print the model Summary
results = smf.ols(formula='mortality ~ latitude', data=recordsDataFrame)
results = results.fit()
print(results.summary())