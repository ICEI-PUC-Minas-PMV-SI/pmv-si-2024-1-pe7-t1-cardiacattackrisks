import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


labels = ['Age','Cholesterol','Heart Rate','Diabetes','Family History','Smoking','Obesity','Alcohol Consumption','Exercise Hours Per Week','Previous Heart Problems','Medication Use','Stress Level','Sedentary Hours Per Day','Income','BMI','Triglycerides','Physical Activity Days Per Week','Sleep Hours Per Day','Heart Attack Risk']

heart_attack_dataset = pd.read_csv('heart_attack_prediction_dataset.csv')

sns.scatterplot(data=heart_attack_dataset, x='Age', y='Heart Attack Risk')

plt.savefig('scatterplot_age_hearth_attack_risk.png',bbox_inches='tight')

# plt.show()