import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Importando o dataset do CSV
data = pd.read_csv('heart_attack_prediction_dataset.csv')