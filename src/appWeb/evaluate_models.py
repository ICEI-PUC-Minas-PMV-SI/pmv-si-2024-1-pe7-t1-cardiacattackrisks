import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Carregar o dataset
data = pd.read_csv('heart_attack_prediction_dataset.csv')

# Converter variáveis categóricas em binárias (0 ou 1)
def binary_encoder(column, positive_value):
    return column.apply(lambda x: 1 if x == positive_value else 0)

models = [
    ('KNeighbors Classifier', 'knn', KNeighborsClassifier(n_neighbors=5)),  
    ('Support Vector Machine', 'svm', SVC(random_state=42)),
    ('Random Forest', 'rf', RandomForestClassifier(n_estimators=100, random_state=42))
]

data['Sex'] = binary_encoder(data['Sex'], 'Male')
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

# Dividir os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

for name, short_name, model in models:
    # Carregar o modelo treinado e o scaler, se existirem
    try:
        model = joblib.load(short_name+'_heart_attack_model.pkl')
        scaler = joblib.load('scaler.pkl')
        print("Modelos carregados com sucesso.")
    except FileNotFoundError:
        print("Modelos não encontrados, treinando um novo modelo.")
        # model = KNeighborsClassifier(n_neighbors=5)
        model.fit(X_train, y_train)
        joblib.dump(model, short_name+'_heart_attack_model.pkl')
        joblib.dump(scaler, 'scaler.pkl')

    # Fazer previsões no conjunto de teste
    y_pred = model.predict(X_test)

    # Avaliar o desempenho do modelo
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    print("Matriz de Confusão "+name+":")
    print(conf_matrix)
    print("\nRelatório de Classificação "+name+":")
    print(class_report)
