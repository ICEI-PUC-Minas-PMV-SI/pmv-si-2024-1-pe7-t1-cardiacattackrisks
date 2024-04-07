import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy as sp

# labels = ['Age','Sex','Cholesterol','Blood Pressure','Heart Rate','Diabetes','Family History','Smoking','Obesity','Alcohol Consumption','Exercise Hours Per Week','Diet','Previous Heart Problems','Medication Use','Stress Level','Sedentary Hours Per Day','Income','BMI','Triglycerides','Physical Activity Days Per Week','Sleep Hours Per Day','Country','Continent','Hemisphere','Heart Attack Risk']
labels = ['Age','Cholesterol','Heart Rate','Diabetes','Family History','Smoking','Obesity','Alcohol Consumption','Exercise Hours Per Week','Previous Heart Problems','Medication Use','Stress Level','Sedentary Hours Per Day','Income','BMI','Triglycerides','Physical Activity Days Per Week','Sleep Hours Per Day','Heart Attack Risk']

heart_attack_dataset = pd.read_csv('heart_attack_prediction_dataset.csv')
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
# heart_attack_dataset['Sex'] = heart_attack_dataset['Sex'].apply(pd.to_numeric, errors='coerce')
# heart_attack_dataset['Blood Pressure'] = heart_attack_dataset['Blood Pressure'].apply(pd.to_numeric, errors='coerce')
# heart_attack_dataset['Diet'] = heart_attack_dataset['Diet'].apply(pd.to_numeric, errors='coerce')
# heart_attack_dataset['Country'] = heart_attack_dataset['Country'].apply(pd.to_numeric, errors='coerce')
# heart_attack_dataset['Continent'] = heart_attack_dataset['Continent'].apply(pd.to_numeric, errors='coerce')
# heart_attack_dataset['Hemisphere'] = heart_attack_dataset['Hemisphere'].apply(pd.to_numeric, errors='coerce')

heart_attack_matrix = heart_attack_dataset[labels].corr(method='pearson',numeric_only=False)
# heart_attack_matrix = heart_attack_dataset[labels].corr(method='spearman',numeric_only=True)
# heart_attack_matrix = heart_attack_dataset.corr()

# cmap = sns.diverging_palette(
#     h_neg=240,
#     h_pos=10,
#     s=100,
#     as_cmap=True,
# )

plt.figure(figsize = (16,5))

sns.heatmap(
    heart_attack_matrix,
    cmap='coolwarm',
    # cmap=cmap,
    center=0,
    vmin=-1,
    vmax=1,
    # square=True,
    linewidths=0.01,
    annot=True,
    xticklabels=labels,
    yticklabels=labels,
)

plt.savefig('heatmap_pearson_non_numeric.png',bbox_inches='tight')

# plt.show()