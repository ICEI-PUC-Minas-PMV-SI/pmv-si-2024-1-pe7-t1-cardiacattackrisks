import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

heart_attack_dataset = pd.read_csv('heart_attack_prediction_dataset.csv')
heart_attack_matrix = heart_attack_dataset.corr()