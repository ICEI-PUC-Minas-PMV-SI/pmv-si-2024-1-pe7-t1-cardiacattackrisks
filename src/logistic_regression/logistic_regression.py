import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, recall_score, f1_score

# Importando o dataset do CSV
data = pd.read_csv('heart_attack_prediction_dataset.csv')

# Deletar coluna ID
data = data.drop(columns=['Patient ID'])

# Edição da Pressão Sanguinea
data["Systolic Pressure"] = data["Blood Pressure"].apply(
    lambda x: x.split("/")[0]).astype(int)
data["Dyastolic Pressure"] = data["Blood Pressure"].apply(
    lambda x: x.split("/")[1]).astype(int)

# Deletar Blood Pressure
data = data.drop(columns=['Blood Pressure'])

# Redução de casas decimais para uma após a vírgula

pd.set_option('display.precision', 1)

# Transformando dados de 'Diet'
ordinal_map = {'Healthy': 2, 'Average': 1, 'Unhealthy': 0}
data['Diet'] = data['Diet'].map(ordinal_map)

# Transformando Male = 1 e Female = 0
ordinal_map_sex = {'Male': 1, 'Female': 0}
data['Sex'] = data['Sex'].map(ordinal_map_sex)

# Remover colunas desnecessárias para o modelo
data = data.drop(columns=['Country', 'Continent', 'Hemisphere'])

# Separar variáveis preditoras e variável a ser prevista
X = data.drop(columns=['Heart Attack Risk'])
y = data['Heart Attack Risk']

# Normalizar demais variáveis preditoras
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir conjunto de dados
# Conjunto de treinamento: 80% - Conjunto de teste 20%
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.20, random_state=42)

# Criar modelo
# logreg_model = LogisticRegression(random_state=42)
logreg_model = LogisticRegression()
logreg_model.fit(X_train, y_train)

# Fazer previsões
y_pred = logreg_model.predict(X_test)

# Calculo e metricas
print("Precisão:", accuracy_score(y_test, y_pred))
print("Matrix de confusão:\n", confusion_matrix(y_test, y_pred))
print("Classificação:\n", classification_report(y_test, y_pred))
# print("Recall: ", recall_score(y_test, y_pred))
# print("F1 Score: ", f1_score(y_test, y_pred))