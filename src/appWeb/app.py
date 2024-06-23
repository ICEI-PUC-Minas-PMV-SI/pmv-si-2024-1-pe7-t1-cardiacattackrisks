from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
from svm.main import svm_model
from sklearn.preprocessing import StandardScaler

app = Flask(__name__,
            static_url_path='', 
            static_folder='Static',
            template_folder='Templates')
CORS(app, resources={r"/predict": {"origins": "*"}})


# Carregar o modelo treinado e o scaler
model_knn = joblib.load('knn_heart_attack_model.pkl')
model_svm = joblib.load('svm_heart_attack_model.pkl')
scaler = joblib.load('scaler.pkl')

# Carregar a lista das colunas esperadas
with open('expected_columns.txt', 'r') as f:
    expected_columns = [line.strip() for line in f]

@app.route('/')
def index():
   print('Request for index page received')
#    return render_template('index.html')
   return redirect(url_for('static', filename='index.html'))

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
        prediction_knn = model_knn.predict(df_scaled)
        output_knn = int(prediction_knn[0])

        prediction_svm = model_svm.predict(df_scaled)
        output_svm = int(prediction_svm[0])

        # Retornar a resposta em JSON
        return jsonify({'Heart Attack Risk (KNN)': output_knn, 'Heart Attack Risk (SVM)': output_svm})
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
