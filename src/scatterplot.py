import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

labels = ['Age','Sex','Cholesterol','Blood Pressure','Heart Rate','Diabetes','Family History','Smoking','Obesity','Alcohol Consumption','Exercise Hours Per Week','Diet','Previous Heart Problems','Medication Use','Stress Level','Sedentary Hours Per Day','Income','BMI','Triglycerides','Physical Activity Days Per Week','Sleep Hours Per Day','Country','Continent','Hemisphere','Heart Attack Risk']

heart_attack_dataset = pd.read_csv('heart_attack_prediction_dataset.csv')

# sns.scatterplot(data=heart_attack_dataset, x='Age', y='Heart Attack Risk')

# plt.savefig('scatterplot_age_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Cholesterol', y='Heart Attack Risk')

# plt.savefig('scatterplot_cholesterol_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Heart Rate', y='Heart Attack Risk')

# plt.savefig('scatterplot_heart_rate_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Diabetes', y='Heart Attack Risk')

# plt.savefig('scatterplot_diabetes_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Family History', y='Heart Attack Risk')

# plt.savefig('scatterplot_family_history_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Smoking', y='Heart Attack Risk')

# plt.savefig('scatterplot_smoking_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Obesity', y='Heart Attack Risk')

# plt.savefig('scatterplot_obesity_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Alcohol Consumption', y='Heart Attack Risk')

# plt.savefig('scatterplot_alcohol_consumption_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Exercise Hours Per Week', y='Heart Attack Risk')

# plt.savefig('scatterplot_exercise_hours_per_week_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Previous Heart Problems', y='Heart Attack Risk')

# plt.savefig('scatterplot_previous_heart_problems_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Medication Use', y='Heart Attack Risk')

# plt.savefig('scatterplot_medication_use_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Stress Level', y='Heart Attack Risk')

# plt.savefig('scatterplot_stress_level_hearth_attack_risk.png',bbox_inches='tight')


# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Sedentary Hours Per Day', y='Heart Attack Risk')

# plt.savefig('scatterplot_sedentary_hours_per_day_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Income', y='Heart Attack Risk')

# plt.savefig('scatterplot_income_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='BMI', y='Heart Attack Risk')

# plt.savefig('scatterplot_bmi_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Triglycerides', y='Heart Attack Risk')

# plt.savefig('scatterplot_triglycerides_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Physical Activity Days Per Week', y='Heart Attack Risk')

# plt.savefig('scatterplot_physical_activity_days_per_week_hearth_attack_risk.png',bbox_inches='tight')

# ####################################################################################

# sns.scatterplot(data=heart_attack_dataset, x='Sleep Hours Per Day', y='Heart Attack Risk')

# plt.savefig('scatterplot_sleep_hours_per_day_hearth_attack_risk.png',bbox_inches='tight')

sns.scatterplot(data=heart_attack_dataset[heart_attack_dataset["Heart Attack Risk"] == 1], x='Age', y='Sex', hue='Sex', size='Sex')

plt.savefig('scatterplot_age_hearth_attack_risk.png',bbox_inches='tight')

# plt.show()