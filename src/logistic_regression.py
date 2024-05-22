#https://www.datacamp.com/tutorial/understanding-logistic-regression-python

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

cols = ['Age','Cholesterol','Heart Rate','Diabetes','Family History','Smoking','Obesity','Alcohol Consumption','Exercise Hours Per Week','Previous Heart Problems','Medication Use','Stress Level','Sedentary Hours Per Day','Income','BMI','Triglycerides','Physical Activity Days Per Week','Sleep Hours Per Day','Heart Attack Risk']

heart_attack_dataset = pd.read_csv('heart_attack_prediction_dataset.csv')

heart_attack_dataset.head()

feature_cols = ['Age','Cholesterol','Heart Rate','Diabetes','Family History','Smoking','Obesity','Previous Heart Problems']

features = heart_attack_dataset[feature_cols]
target = heart_attack_dataset.label

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=16)

logreg = LogisticRegression(random_state=16)

logreg.fit(x_train, y_train)

y_pred = logreg.predict(x_test)

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix