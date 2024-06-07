import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Função para carregar e preparar os dados
def load_and_prepare_data():
    data = pd.read_csv('data/heart_attack_prediction_dataset.csv')

    # Transformando dados de 'Diet' e 'Sex'
    ordinal_map = {'Healthy': 2, 'Average': 1, 'Unhealthy': 0}
    data['Diet'] = data['Diet'].map(ordinal_map)

    ordinal_map_sex = {'Male': 1, 'Female': 0}
    data['Sex'] = data['Sex'].map(ordinal_map_sex)

    # Edição da Pressão Sanguinea
    data["Systolic Pressure"] = data["Blood Pressure"].apply(lambda x: x.split("/")[0]).astype(int)
    data["Dyastolic Pressure"] = data["Blood Pressure"].apply(lambda x: x.split("/")[1]).astype(int)

    data = data.drop(columns=['Patient ID', 'Blood Pressure', 'Continent', 'Hemisphere', 'Country'])

    return data

# Carregar e preparar os dados
data = load_and_prepare_data()

# Definir features e target
X = data.drop('Heart Attack Risk', axis=1)
y = data['Heart Attack Risk']

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Treinar o modelo KNN
knn_classifier = KNeighborsClassifier(n_neighbors=11)
knn_classifier.fit(X_train, y_train)

# Avaliar o modelo
y_pred_knn = knn_classifier.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
conf_matrix_knn = confusion_matrix(y_test, y_pred_knn)

print(f"Acurácia: {accuracy_knn}")
print(f"Matriz de Confusão:\n{conf_matrix_knn}")

# Salvar o modelo e o scaler
joblib.dump(knn_classifier, 'models/knn_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
