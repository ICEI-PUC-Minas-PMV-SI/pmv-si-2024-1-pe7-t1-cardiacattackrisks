import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Carregar o dataset
data = pd.read_csv('heart_attack_prediction_dataset.csv')

# Converter variáveis categóricas em binárias (0 ou 1)
def binary_encoder(column, positive_value):
    return column.apply(lambda x: 1 if x == positive_value else 0)

data['Sex'] = binary_encoder(data['Sex'], 'Male')
# data['Country'] = binary_encoder(data['Country'], 'Argentina')
# data['Continent'] = binary_encoder(data['Continent'], 'South America')
# data['Hemisphere'] = binary_encoder(data['Hemisphere'], 'Southern')
data['Diet'] = binary_encoder(data['Diet'], 'Average')

# Separar a coluna 'Blood Pressure' em duas colunas: 'Systolic Blood Pressure' e 'Diastolic Blood Pressure'
blood_pressure_split = data['Blood Pressure'].str.split('/', expand=True)
data['Systolic Blood Pressure'] = blood_pressure_split[0].astype(float)
data['Diastolic Blood Pressure'] = blood_pressure_split[1].astype(float)

# Remover a coluna original 'Blood Pressure'
data = data.drop(['Blood Pressure'], axis=1)

# Remover as colunas 'Country', 'Continent' e 'Hemisphere'
data = data.drop(['Country'], axis=1)
data = data.drop(['Continent'], axis=1)
data = data.drop(['Hemisphere'], axis=1)
data = data.drop(['Income'], axis=1)

# Separar os dados em características (features) e rótulos (labels)
X = data.drop(['Patient ID', 'Heart Attack Risk'], axis=1)
y = data['Heart Attack Risk']

# Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Salvar o scaler para uso na API
joblib.dump(scaler, 'scaler.pkl')

# Salvar o dataset processado se necessário
processed_data = pd.DataFrame(X_scaled, columns=X.columns)
processed_data['Heart Attack Risk'] = y
processed_data.to_csv('processed_heart_attack_prediction_dataset.csv', index=False)

print("Pré-processamento concluído e scaler salvo.")

# Salvar a lista de colunas esperadas
expected_columns = list(X.columns)
with open('expected_columns.txt', 'w') as f:
    for column in expected_columns:
        f.write(f"{column}\n")

print("Lista de colunas esperadas salva.")
