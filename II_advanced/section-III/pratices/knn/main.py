import pandas
import seaborn
import matplotlib 
import numpy
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import os
import math

def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

#1: Load the (heart.csv) dataset 
hearts = pandas.read_csv(getCurrentDirname()+'/heart.csv')

#2: Get the target and features
print(hearts.info())
print(hearts)

#3: Split into training and test set 
# x = hearts.target
# y = hearts.drop(columns=['target'])
x = hearts.iloc[:,0:13]
y = hearts.iloc[:,13]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#4: Create and fit your model using KNeighbors classification for five neighbors (sklearn)
# knn = KNeighborsClassifier(n_neighbors=5) 
# knn.fit(x_train, y_train)
# print(math.sqrt(len(y_test))) 7.810249675906654 = 6
classifier = KNeighborsClassifier(n_neighbors=6, P=2, metric="euclidean")

# KNN model fit
#5: Predict on dataset model calculate Accuracy Score
y_pred = classifier.predict(x_test)

#6: Calculate the model accuracy
accuracy = accuracy_score(y_test, y_pred)

#7: Create a confusion matrix with a Pandas cross table - confusion matrix
confusion = confusion(y_test, y_pred)

#8: Print the TN, FN, TP, FP values

# 9: Print the model precision value

# precision is the ratio of  tp / (tp + fp)

#10: # recall = the ratio tp / (tp + fn)

#11: Visualize the confusion matrix with a Heatmap