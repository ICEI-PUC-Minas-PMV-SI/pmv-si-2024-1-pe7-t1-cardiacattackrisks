from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})


# Carregar o modelo treinado e o scaler
model = joblib.load('knn_heart_attack_model.pkl')
scaler = joblib.load('scaler.pkl')

# Carregar a lista das colunas esperadas
with open('expected_columns.txt', 'r') as f:
    expected_columns = [line.strip() for line in f]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receber os dados da requisição
        data = request.get_json(force=True)
        app.logger.info(f"Dados recebidos: {data}")

        # Transformar os dados em um DataFrame
        df = pd.DataFrame([data])

        # Preencher colunas ausentes com valores padrão (por exemplo, 0 ou valores médios)
        for column in expected_columns:
            if column not in df.columns:
                df[column] = 0

        # Conversão para variáveis binárias
        df['Sex'] = df['Sex'].apply(lambda x: 1 if x == 'Male' else 0)
        df['Country'] = df['Country'].apply(lambda x: 1 if x == 'Argentina' else 0)
        df['Continent'] = df['Continent'].apply(lambda x: 1 if x == 'South America' else 0)
        df['Hemisphere'] = df['Hemisphere'].apply(lambda x: 1 if x == 'Southern' else 0)
        df['Diet'] = df['Diet'].apply(lambda x: 1 if x == 'Average' else 0)

        # Garantir que as colunas estejam na ordem correta
        df = df[expected_columns]

        # Normalizar os dados
        df_scaled = scaler.transform(df)

        # Fazer a previsão
        prediction = model.predict(df_scaled)
        output = int(prediction[0])

        # Retornar a resposta em JSON
        return jsonify({'Heart Attack Risk': output})
    except Exception as e:
        app.logger.error(f"Erro ao fazer a previsão: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)