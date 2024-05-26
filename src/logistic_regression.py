#https://www.datacamp.com/tutorial/understanding-logistic-regression-python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

# Loading Data

cols = ['Age','Cholesterol','Heart Rate','Diabetes','Family History','Smoking','Obesity','Alcohol Consumption','Exercise Hours Per Week','Previous Heart Problems','Medication Use','Stress Level','Sedentary Hours Per Day','Income','BMI','Triglycerides','Physical Activity Days Per Week','Sleep Hours Per Day','Heart Attack Risk']

heart_attack_dataset = pd.read_csv('heart_attack_prediction_dataset.csv', header=None, names=cols)

#heart_attack_dataset.head()

print(heart_attack_dataset)

# Converting Data

# heart_attack_dataset['Age'] = pd.to_numeric(heart_attack_dataset['Age'], errors='coerce')
# heart_attack_dataset['Cholesterol'] = pd.to_numeric(heart_attack_dataset['Cholesterol'], errors='coerce')
# heart_attack_dataset['Heart Rate'] = pd.to_numeric(heart_attack_dataset['Heart Rate'], errors='coerce')
# heart_attack_dataset['Diabetes'] = pd.to_numeric(heart_attack_dataset['Diabetes'], errors='coerce')
# heart_attack_dataset['Family History'] = pd.to_numeric(heart_attack_dataset['Family History'], errors='coerce')
# heart_attack_dataset['Smoking'] = pd.to_numeric(heart_attack_dataset['Smoking'], errors='coerce')
# heart_attack_dataset['Obesity'] = pd.to_numeric(heart_attack_dataset['Obesity'], errors='coerce')
# heart_attack_dataset['Previous Heart Problems'] = pd.to_numeric(heart_attack_dataset['Previous Heart Problems'], errors='coerce')

# print(heart_attack_dataset)

# Selecting Feature

feature_cols = ['Age','Cholesterol','Heart Rate','Diabetes','Family History','Smoking','Obesity','Previous Heart Problems']

features = heart_attack_dataset[feature_cols]
target = heart_attack_dataset['Heart Attack Risk']

# Splitting Data

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=16)

# Model Development and Prediction

logreg = LogisticRegression(random_state=16)

logreg.fit(x_train, y_train)

y_pred = logreg.predict(x_test)

# Model Evaluation using Confusion Matrix

cnf_matrix = confusion_matrix(y_test, y_pred)
cnf_matrix

# Heatmap

class_names=[0,1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Matriz de confusão', y=1.1)
plt.ylabel('Atual')
plt.xlabel('Previsão')

Text(0.5,257.44,'Previsão')

# Confusion Matrix Evaluation Metrics

target_names = ['without Heart Attack Risk', 'with Heart Attack Risk']
print(classification_report(y_test, y_pred, target_names=target_names))

# ROC Curve

y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = roc_curve(y_test,  y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()