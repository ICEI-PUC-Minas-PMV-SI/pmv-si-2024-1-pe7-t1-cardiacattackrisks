import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def load_data(file_path):
    # Importa dataset
    data = pd.read_csv(file_path)
    return data


def clean_data(data):
    # Deletar coluna ID
    data = data.drop(columns=['Patient ID'])

    # Edição da Pressão Sanguinea
    data["Systolic Pressure"] = data["Blood Pressure"].apply(
        lambda x: x.split("/")[0]).astype(int)
    data["Dyastolic Pressure"] = data["Blood Pressure"].apply(
        lambda x: x.split("/")[1]).astype(int)
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

    return data


def preprocess_data(data):
    # Separar variáveis preditoras e variável a ser prevista
    X = data.drop(columns=['Heart Attack Risk'])
    y = data['Heart Attack Risk']

    # Normalizar demais variáveis preditoras
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y


def train_svm(X_train, y_train):
    # Criar modelo SVM usando um kernel linear
    svm_model = SVC(kernel='rbf', class_weight='balanced')
    svm_model.fit(X_train, y_train)
    return svm_model


def train_linear_regression(X_train, y_train):
    # Treinar um modelo de regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    # Fazer previsões
    y_pred = model.predict(X_test)

    # Calcular métricas de avaliação
    accuracy = accuracy_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return accuracy, confusion, report


# Importa e limpa os dados
data = load_data('heart_attack_prediction_dataset.csv')
cleaned_data = clean_data(data)

# Pré-processamento dos dados
X, y = preprocess_data(cleaned_data)

# Dividir conjunto de dados
# Conjunto de treinamento: 80% - Conjunto de teste 20%
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42)

# Treinar SVM
svm_model = train_svm(X_train, y_train)

# Avaliar SVM
accuracy, confusion, report = evaluate_model(svm_model, X_test, y_test)
print("SVM Accuracy:", accuracy)
print("SVM Confusion Matrix:\n", confusion)
print("SVM Classification Report:\n", report)

# Treinar regressão linear
linear_model = train_linear_regression(X_train, y_train)

# Avaliar regressão linear
y_pred = linear_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Linear Regression MSE:", mse)
