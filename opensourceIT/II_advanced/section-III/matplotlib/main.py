import matplotlib.pyplot as plt
import numpy as np 


# sample example

xpoints = np.array([0, 6])
ypoints = np.array([0, 12])

plt.plot(xpoints, ypoints)
plt.show()

# The plot() function is used to draw points (markers) in a diagram.
# By default, the plot() function draws a line from point to point.

# The function takes parameters for specifying points in the diagram.
# - Parameter 1 is an array containing the points on the x-axis(horizontal axis).
# - Parameter 2 is an array containing the points on the y-axis(vertical axis).

# Plotting Without Line
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

# Multiple Points
# You can plot as many points as you like, just make sure you have the same number of points in both axis.

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Default X-Points
# If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.
# So, if we take the same example as above, and leave out the x-points, the diagram will look like this:

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# Markers
# You can use the keyword argument marker to emphasize each point with a specified marker:

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
# plt.plot(ypoints, marker = '*')
plt.show()

# Create Labels for a Plot
# With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# Creating Scatter Plots
# With Pyplot, you can use the scatter() function to draw a scatter plot.
# The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

# Creating Bars
# With Pyplot, you can use the bar() function to draw bar graphs:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

# Create Histogram
# In Matplotlib, we use the hist() function to create histograms.

# The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

# # Creating Pie Chartss
# # With Pyplot, you can use the pie() function to draw pie charts:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()


# credits
# https://www.w3schools.com/python/matplotlib_getting_started.asp
