from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
from svm.main import svm_model
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)


# Carregar o modelo treinado e o scaler
model_knn = joblib.load('knn_heart_attack_model.pkl')
scaler = joblib.load('scaler.pkl')

# Carregar a lista das colunas esperadas
with open('expected_columns.txt', 'r') as f:
    expected_columns = [line.strip() for line in f]


def preprocess_df(df):
    # Preencher colunas ausentes com valores padrão (por exemplo, 0 ou valores médios)
    for column in expected_columns:
        if column not in df.columns:
            df[column] = 0

    # Conversão para variáveis binárias
    df['Sex'] = df['Sex'].apply(lambda x: 1 if x == 'Male' else 0)
    df['Diet'] = df['Diet'].apply(lambda x: 1 if x == 'Average' else 0)

    # Garantir que as colunas estejam na ordem correta
    df = df[expected_columns]

    return df


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receber os dados da requisição
        data = request.get_json(force=True)
        app.logger.info(f"Dados recebidos: {data}")

        # Transformar os dados em um DataFrame
        df = pd.DataFrame([data])

        # Preprocessar os dados
        df = preprocess_df(df)

        # Normalizar os dados
        df_scaled = scaler.transform(df)

        # Fazer a previsão
        prediction = model_knn.predict(df_scaled)
        output = int(prediction[0])

        # Retornar a resposta em JSON
        return jsonify({'Heart Attack Risk': output})
    except Exception as e:
        app.logger.error(f"Erro ao fazer a previsão: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/predict/svm', methods=['POST'])
def predict_svm():
    try:
        # Receber os dados da requisição
        data = request.get_json(force=True)
        app.logger.info(f"Dados recebidos: {data}")

        # Transformar os dados em um DataFrame
        df = pd.DataFrame([data])

        # Preprocessar os dados
        df = preprocess_df(df)

        # Normalizar os dados
        input_scaled = scaler.transform(df)

        # Fazer a previsão
        prediction = svm_model.predict(input_scaled)
        result = int(prediction[0])

        # Retornar a resposta em JSON
        return jsonify({'Heart Attack Risk': result})
    except Exception as e:
        app.logger.error(f"Erro ao fazer a previsão: {e}")
        app.logger.error(f"with_traceback: {e.with_traceback}")
        app.logger.error(f"__annotations__: {e.add_note}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False)
    # app.run(host="0.0.0.0", port=5000, debug=False)
