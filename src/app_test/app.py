from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Carregar o modelo e o scaler
knn_model = joblib.load('models/knn_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Função para transformar e preparar os dados de entrada
def transform_input_data(input_data):
    input_df = pd.DataFrame([input_data])
    
    # Transformar os dados de entrada
    ordinal_map = {'Healthy': 2, 'Average': 1, 'Unhealthy': 0}
    input_df['Diet'] = input_df['Diet'].map(ordinal_map)

    ordinal_map_sex = {'Male': 1, 'Female': 0}
    input_df['Sex'] = input_df['Sex'].map(ordinal_map_sex)

    input_df["Systolic Pressure"] = input_df["Blood Pressure"].apply(lambda x: x.split("/")[0]).astype(int)
    input_df["Diastolic Pressure"] = input_df["Blood Pressure"].apply(lambda x: x.split("/")[1]).astype(int)
    input_df = input_df.drop(columns=['Blood Pressure'])

    # Selecionar e normalizar as features
    features = ['Sex', 'Age', 'Cholesterol', 'Heart Rate', 'Diabetes', 'Family History', 'Dyastolic Pressure',
                'Systolic Pressure', 'Smoking', 'Obesity', 'Alcohol Consumption', 'Diet', 'Exercise Hours Per Week',
                'Previous Heart Problems', 'Medication Use', 'Triglycerides', 'Sleep Hours Per Day', 'BMI',
                'Physical Activity Days Per Week']

    input_df = input_df[features]
    input_df = scaler.transform(input_df)

    return input_df

@app.route('/predict_knn', methods=['POST'])
def predict_knn():
    input_data = request.json
    transformed_data = transform_input_data(input_data)
    
    # Fazer a predição com o modelo KNN
    prediction = knn_model.predict(transformed_data)

    # Retornar o resultado como JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)