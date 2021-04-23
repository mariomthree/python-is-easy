import pandas
import seaborn
import matplotlib 
import numpy
import sklearn.neigbors 
from sklearn.neigbors  import KNeighborsClassifier
import os

def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

#1: Load the (heart.csv) dataset 
hearts = pandas.read_csv(getCurrentDirname()+'/heart.csv')

#2: Get the target and features
print(hearts.info())
print(hearts)

#3: Split into training and test set 

#4: Create and fit your model using KNeighbors classification for five neighbors (sklearn)

# KNN model fit
#5: Predict on dataset model calculate Accuracy Score
#6: Calculate the model accuracy
#7: Create a confusion matrix with a Pandas cross table - confusion matrix
#8: Print the TN, FN, TP, FP values
# 9: Print the model precision value
# precision is the ratio of  tp / (tp + fp)
#10: # recall = the ratio tp / (tp + fn)
#11: Visualize the confusion matrix with a Heatmap