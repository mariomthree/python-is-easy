# 1. Import the libraries
import pandas as pd
import os


# 2. Get the data sets
def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

train = pd.read_csv(f'{getCurrentDirname()}/train.csv')
test = pd.read_csv(f'{getCurrentDirname()}/test.csv')

# 3. Drop the PAssengerID
train = train.drop(columns=['PassengerId'])
test = test.drop(columns=['PassengerId'])

# 4. Do the Data Exploration/Analysis
print(train.info())

trainNullSets = train.apply(lambda x:sum(x.isnull()), axis=0)
print(trainNullSets)

age = train.Age.value_counts()
cabin = train.Cabin.value_counts()
embarked = train.Embarked.value_counts()

print(f'Age:\n {age}')
print(f'Cabin:\n {cabin}')  
print(f'Embarked:\n {embarked}')

# 5. Describe the training dataset
print(train.info())

# 6. Clean the dataset
train.Age = train.Age.fillna(24)
train.Cabin = train.Cabin.fillna('B96')
train.Embarked = train.Embarked.fillna('S')

# 7. Display the head upto 10 rows
print(train.head())