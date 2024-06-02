# Pergunta orientada a dados

Ao ser considerada uma pergunta orientada a dados, esta, traz consigo uma abordagem mais específica e técnica, trazendo em sua essência, a fonte dos dados, o direcionamento mais assertivo para a resolução de um possível problema e fornece insumos para que a análise dos dados colabore na identificação de oportunidades e ou desafios. Nesse sentido, levando em conta o escopo do presente trabalho, a pergunta orientada a dados pode ser descrita como _"quais são os principais fatores de risco para a ocorrência de ataques cardíacos"?_ Neste sentido, a pergunta aqui descrita, traz essencialmente o questionamento de quais fatores podem vir a configurar a ocorrência de ataques cardíacos. 

# Tipos de dados do dataset

| Atributo  |  Tipo   | Classificação |
|-----------|---------|------------|
|Patient ID |  Qualitativo  |  Polinominal   |
|Age   |  Quantitativo | Numérico de Razão |
|Sex   | Qualitativo |   Binominal Simétrico  |
|Cholesterol  | Quantitativo | Numérico de Razão |
|Blood Pressure  |  Quantitativo | Numérico de Razão|
|Heart Rate  | Quantitativo | Numérico de Razão |
|Diabetes | Qualitativo | Binominal Assimétrico |
|Family History  | Qualitativo | Binominal Assimétrico |
|Smoking   | Qualitativo | Binominal Assimétrico |
|Obesity | Qualitativo | Binominal Assimétrico |
|Alcohol Consumption  | Qualitativo  | Binominal Assimétrico |
|Exercise Hours Per Week |  Quantitativo | Numérico Intervalar |
|Diet    | Qualitativo | Polinominal Ordinal |
|Previous Heart Problems  | Qualitativo | Binominal Assimétrico |
|Medication Use  | Qualitativo | Binominal Simétrico |
|Stress Level  | Quantitativo | Numérico Normalizado |
|Sedentary Hours Per Day  | Quantitativo | Numérico Intervalar |
|Income| Quantitativo | Numérico de Razão |
|BMI   | Quantitativo | Numérico de Razão |
|Triglycerides | Quantitativo | Numérico de Razão |
|Physical Activity Days Per Week | Quantitativo | Numérico Intervalar |
|Sleep Hours Per Day | Quantitativo | Numérico Intervalar |
|Country  | Qualitativo | Polinominal Não-Ordinal |
|Continent | Qualitativo | Polinominal Não-Ordinal |
|Hemisphere  | Qualitativo | Polinominal Não-Ordinal |
|Heart Attack Risk | Qualitativo | Binominal Assimétrico |

# Outras bases de dados úteis 

Considerando os atributos do presente _dataset_, considera-se que o mesmo apresenta dados que são relevantes para ser considerados os riscos para ataque cardíaco. Em primeiro momento, a necessidade de buscar de outros _datasets_ não se faz presente pela variabilidade de elementos que foram considerados na construção do _dataset_ atual. Mas isto por si só não exime a possibilidade de que outras fontes possam ser consideradas, avaliando outros elementos e conteúdos. 

# Preparação dos dados

* Limpeza de Dados

Para avaliar a limpeza de dados, importamos algumas bibliotecas para auxiliar neste processo, tais como:

```python
from google.colab import files
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import geopandas as gpd
from sklearn.preprocessing import LabelEncoder
```

Atribuir 'data' à referência do datast escolhido:
```python
data = pd.read_csv ('heart_attack_prediction_dataset.csv')
data
```

Carregar as primeiras linhas do dataset para visualização
```python
data.head()
```

Verificação de valores nulos e linhas duplicadas:
```python
print(f"Total de linhas duplicadas: {data.duplicated().sum()}")
print("---------------")
print(f"Total Valores Nulos        : {data.isnull().sum().sum()}")
```

Optou-se por deletar a coluna 'Patient ID', dado que não impactará a análise dos dados:
```python
data = data.drop(columns=['Patient ID'])
```

Exclusão da coluna 'Blood Pressure' em razão da divisão dos dados nela contidos:
```python
data = data.drop(columns=['Blood Pressure'])
```

* Transformação de Dados:  torne os dados comparáveis, normalizando ou padronizando os valores para uma escala específica; codifique variáveis categóricas: converta variáveis categóricas em uma forma numérica, usando técnicas como _one-hot encoding_.

Para melhor visualização, as os números decimais foram reduzidos a um número após a virgula:
```python
pd.set_option('display.precision', 1)
data.head()
```

Também com fim a melhorar a visualização dos dados, atribuiu-se o valor 1 para o sexo Masculino e 0 para o sexo Feminino:
```python
ordinal_map_sex = {'Male':1, 'Female':0}
data['Sex'] = data['Sex'].map(ordinal_map_sex)
```

Os dados da coluna 'Diet' foram transformados em 0, 1 e 2.
```python
ordinal_map = {'Healthy':2,'Average':1,'Unhealthy':0}
data['Diet'] = data['Diet'].map(ordinal_map)
```

* _Feature Engineering_: crie novos atributos que possam ser mais informativos para o modelo; selecione características relevantes e descarte as menos importantes.

A coluna 'Blood Pressure' consta em um mesmo registro, a pressão diastólica e sistólica. Por isto, optamos por segregá-las:

```python
data["Systolic Pressure"] = data["Blood Pressure"].apply(lambda x: x.split("/")[0]).astype(int)
data["Dyastolic Pressure"] = data["Blood Pressure"].apply(lambda x: x.split("/")[1]).astype(int)
```

* Separação de dados: divida os dados em conjuntos de treinamento, validação e teste para avaliar o desempenho do modelo de maneira adequada.

Conujunto de treinamento:
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

y_train = y_train.values.reshape(-1, 1)
y_test = y_test.values.reshape(-1, 1)
y_test.shape
```
  
* Redução de Dimensionalidade: aplique técnicas como PCA (Análise de Componentes Principais) se a dimensionalidade dos dados for muito alta.

Reduzindo a Dimensionalidade:
```python
from sklearn.decomposition import PCA

# Inicializar o objeto PCA com o número desejado de componentes
pca = PCA(n_components=2)  # Define o número de componentes principais desejados

# Aplicar PCA aos dados de treinamento (assumindo que X_train já está definido)
X_train_pca = pca.fit_transform(X_train)

# Converter para DataFrame para uma melhor visualização
X_train_pca_df = pd.DataFrame(data=X_train_pca, 
                              columns=['Principal Component 1', 'Principal Component 2'])

# Exibir as primeiras linhas para visualização
print(X_train_pca_df.head())

# Exibir a nova forma dos dados após a redução de dimensionalidade
print("Forma dos dados após a redução de dimensionalidade:", X_train_pca_df.shape)

# Exibir a variância explicada por cada componente
print("Variância explicada por cada componente:", pca.explained_variance_ratio_)
```

Após a redução da dimensionalidade, chegou-se ao resultado:
```python
   Principal Component 1  Principal Component 2
0               -1.1e+00                    0.2
1                5.4e-01                    1.0
2               -2.3e-01                   -0.5
3                1.4e-01                   -0.7
4               -4.2e-02                    0.2
Forma dos dados após a redução de dimensionalidade: (6134, 2)
Variância explicada por cada componente: [0.08351793 0.05333054]
```

* Validação Cruzada: utilize validação cruzada para avaliar o desempenho do modelo de forma mais robusta.

Realizamos a validação cruzada da seguinte forma:
```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Carregando os dados
data = pd.read_csv('heart_attack_prediction_dataset.csv')
X = data.drop('Heart Attack Risk', axis=1)
y = data['Heart Attack Risk']

# Criamos um pipeline  modelo
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Padronização dos dados
    ('clf', RandomForestClassifier())  # Modelo RandomForest
])

# Realização da validação cruzada
scores = cross_val_score(pipeline, X, y, cv=5)  # 5 folds
print("Acurácia Média: {:.2f}".format(scores.mean()))
print("Desvio Padrão dos Scores: {:.2f}".format(scores.std()))
```
O resultado impresso foi:

```python
Acurácia Média: 0.63
Desvio Padrão dos Scores: 0.00
```

O que nos indica que a acurácia média foi de 63% com um desvio padrão de 0, signficando que o modelo é estável.

# Descrição dos modelos

* MODELO KNN

Considerando o modelo KNN como algoritmo de _machine learning_, este, traz a possibilidade de classificar cada amostra de um conjunto de dados avaliando sua distância em relação aos vizinhos mais próximos. Se os vizinhos mais próximos forem majoritariamente de uma classe, a amostra em questão será classificada nesta categoria.

Neste sentido, apresenta-se o modelo avaliado, abaixo:
```python
#Selecionando variáveis importantes pro modelo
X = data[['Sex', 'Age', 'Cholesterol', 'Heart Rate','Diabetes', 'Family History','Dyastolic Pressure','Systolic Pressure',
                        'Smoking', 'Obesity','Alcohol Consumption', 'Diet', 'Exercise Hours Per Week',
                        'Previous Heart Problems', 'Medication Use', 'Triglycerides', 'Sleep Hours Per Day', 'Income',
                        'BMI', 'Physical Activity Days Per Week']]

y= data['Heart Attack Risk'].values
```

É importante, criar um conjunto de dados de treinamento e teste. Sendo que, o test_size=0.2 significa que 20% dos dados serão usados ​​como conjunto de teste, enquanto 80% serão usados ​​como conjunto de treinamento.
```python
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state = 1,test_size=0.2)
```

Em seguida, usamos do StandardScaler para normalizar os dados e deixá-los em uma única escala para facilitar a análise.
```python
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
```

Criou-se quatro possibilidades de vizinhos para avaliar qual a melhor alternativa. Escolheu-se primeiramente, a avaliação de 1 a 30 vizinhos.
```python
classifier_1 = KNeighborsClassifier(n_neighbors=1)
classifier_2 = KNeighborsClassifier(n_neighbors=2)
classifier_3 = KNeighborsClassifier(n_neighbors=3)
classifier_4 = KNeighborsClassifier(n_neighbors=4)
classifier_5 = KNeighborsClassifier(n_neighbors=5)
classifier_6 = KNeighborsClassifier(n_neighbors=6)
classifier_7 = KNeighborsClassifier(n_neighbors=7)
classifier_8 = KNeighborsClassifier(n_neighbors=8)
classifier_9 = KNeighborsClassifier(n_neighbors=9)
classifier_10 = KNeighborsClassifier(n_neighbors=10)
classifier_11 = KNeighborsClassifier(n_neighbors=11)
classifier_12 = KNeighborsClassifier(n_neighbors=12)
classifier_13 = KNeighborsClassifier(n_neighbors=13)
classifier_14 = KNeighborsClassifier(n_neighbors=14)
classifier_15 = KNeighborsClassifier(n_neighbors=15)
classifier_16 = KNeighborsClassifier(n_neighbors=16)
classifier_17 = KNeighborsClassifier(n_neighbors=17)
classifier_18 = KNeighborsClassifier(n_neighbors=18)
classifier_19 = KNeighborsClassifier(n_neighbors=19)
classifier_20 = KNeighborsClassifier(n_neighbors=20)
classifier_21 = KNeighborsClassifier(n_neighbors=21)
classifier_22 = KNeighborsClassifier(n_neighbors=22)
classifier_23 = KNeighborsClassifier(n_neighbors=23)
classifier_24 = KNeighborsClassifier(n_neighbors=24)
classifier_25 = KNeighborsClassifier(n_neighbors=25)
classifier_26 = KNeighborsClassifier(n_neighbors=26)
classifier_27 = KNeighborsClassifier(n_neighbors=27)
classifier_28 = KNeighborsClassifier(n_neighbors=28)
classifier_29 = KNeighborsClassifier(n_neighbors=29)
classifier_30 = KNeighborsClassifier(n_neighbors=30)
```

Assim, treinamos o modelo KNN relacionado ao cenário de treinamento.
```python
classifier_1.fit(X_train, y_train)
classifier_2.fit(X_train, y_train)
classifier_3.fit(X_train, y_train)
classifier_4.fit(X_train, y_train)
classifier_5.fit(X_train, y_train)
classifier_6.fit(X_train, y_train)
classifier_7.fit(X_train, y_train)
classifier_8.fit(X_train, y_train)
classifier_9.fit(X_train, y_train)
classifier_10.fit(X_train, y_train)
classifier_11.fit(X_train, y_train)
classifier_12.fit(X_train, y_train)
classifier_13.fit(X_train, y_train)
classifier_14.fit(X_train, y_train)
classifier_15.fit(X_train, y_train)
classifier_16.fit(X_train, y_train)
classifier_17.fit(X_train, y_train)
classifier_18.fit(X_train, y_train)
classifier_19.fit(X_train, y_train)
classifier_20.fit(X_train, y_train)
classifier_21.fit(X_train, y_train)
classifier_22.fit(X_train, y_train)
classifier_23.fit(X_train, y_train)
classifier_24.fit(X_train, y_train)
classifier_25.fit(X_train, y_train)
classifier_26.fit(X_train, y_train)
classifier_27.fit(X_train, y_train)
classifier_28.fit(X_train, y_train)
classifier_29.fit(X_train, y_train)
classifier_30.fit(X_train, y_train)
```

E então, criou-se o algoritmo para fazer a predição dos resultados dos testes.
```python
y_pred_1 = classifier_1.predict(X_test)
y_pred_2 = classifier_2.predict(X_test)
y_pred_3 = classifier_3.predict(X_test)
y_pred_4 = classifier_4.predict(X_test)
y_pred_5 = classifier_5.predict(X_test)
y_pred_6 = classifier_6.predict(X_test)
y_pred_7 = classifier_7.predict(X_test)
y_pred_8 = classifier_8.predict(X_test)
y_pred_9 = classifier_9.predict(X_test)
y_pred_10 = classifier_10.predict(X_test)
y_pred_11 = classifier_11.predict(X_test)
y_pred_12 = classifier_12.predict(X_test)
y_pred_13 = classifier_13.predict(X_test)
y_pred_14 = classifier_14.predict(X_test)
y_pred_15 = classifier_15.predict(X_test)
y_pred_16 = classifier_16.predict(X_test)
y_pred_17 = classifier_17.predict(X_test)
y_pred_18 = classifier_18.predict(X_test)
y_pred_19 = classifier_19.predict(X_test)
y_pred_20 = classifier_20.predict(X_test)
y_pred_21 = classifier_21.predict(X_test)
y_pred_22 = classifier_22.predict(X_test)
y_pred_23 = classifier_23.predict(X_test)
y_pred_24 = classifier_24.predict(X_test)
y_pred_25 = classifier_25.predict(X_test)
y_pred_26 = classifier_26.predict(X_test)
y_pred_27 = classifier_27.predict(X_test)
y_pred_28 = classifier_28.predict(X_test)
y_pred_29 = classifier_29.predict(X_test)
y_pred_30 = classifier_30.predict(X_test)
```

Por fim, escolheu-se as métricas de avaliação das performances dos cenários do modelo criado.
```python
cm_KNN = confusion_matrix(y_test, y_pred_1)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_1))

cm_KNN = confusion_matrix(y_test, y_pred_2)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_2))

cm_KNN = confusion_matrix(y_test, y_pred_3)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_3))

cm_KNN = confusion_matrix(y_test, y_pred_4)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_4))

cm_KNN = confusion_matrix(y_test, y_pred_5)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_5))

cm_KNN = confusion_matrix(y_test, y_pred_6)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_6))

cm_KNN = confusion_matrix(y_test, y_pred_7)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_7))

cm_KNN = confusion_matrix(y_test, y_pred_8)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_8))

cm_KNN = confusion_matrix(y_test, y_pred_9)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_9))

cm_KNN = confusion_matrix(y_test, y_pred_10)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_10))

cm_KNN = confusion_matrix(y_test, y_pred_11)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_11))

cm_KNN = confusion_matrix(y_test, y_pred_12)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_12))

cm_KNN = confusion_matrix(y_test, y_pred_13)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_13))

cm_KNN = confusion_matrix(y_test, y_pred_14)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_14))

cm_KNN = confusion_matrix(y_test, y_pred_15)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_15))

cm_KNN = confusion_matrix(y_test, y_pred_16)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_16))

cm_KNN = confusion_matrix(y_test, y_pred_17)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_17))

cm_KNN = confusion_matrix(y_test, y_pred_18)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_18))

cm_KNN = confusion_matrix(y_test, y_pred_19)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_19))

cm_KNN = confusion_matrix(y_test, y_pred_20)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_20))

cm_KNN = confusion_matrix(y_test, y_pred_21)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_21))

cm_KNN = confusion_matrix(y_test, y_pred_22)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_22))

cm_KNN = confusion_matrix(y_test, y_pred_23)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_23))

cm_KNN = confusion_matrix(y_test, y_pred_24)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_24))

cm_KNN = confusion_matrix(y_test, y_pred_25)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_25))

cm_KNN = confusion_matrix(y_test, y_pred_26)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_26))

cm_KNN = confusion_matrix(y_test, y_pred_27)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_27))

cm_KNN = confusion_matrix(y_test, y_pred_28)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_28))

cm_KNN = confusion_matrix(y_test, y_pred_29)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_29))

cm_KNN = confusion_matrix(y_test, y_pred_30)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_30))
```
O resultado das acurácias obtidas, foram aumentando ao passo que a variância de elementos foi caindo, conforme tabela abaixo:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/5cecca72-bbf1-4bd5-9bc7-7205f39d5829)

Nota-se que os valores cresceram, entretanto, considerando os números pares, estes variaram. Para evitar o empate entre os dados analisados, foram considerados o número de vizinhos somente ímpares, de 1 ao 31, obtendo-se o mesmo resultado com aumento da acurácia e diminuição da variância.

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/28a9ab90-f00b-4681-8a95-e3f93d63cfa6)

Neste sentido, decidiu-se com base nas observações acima destacadas, que para o modelo KNN, o número de 11 vizinhos, pode ser mais adequado. Sendo assim, os dados do modelo se apresentam abaixo:

```python
# MODELO KNN - 11 vizinhos
classifier_11 = KNeighborsClassifier(n_neighbors=11)

# MODELO KNN - Treinando o modelo KNN com 11 vizinhos.
classifier_11.fit(X_train, y_train)

# MODELO KNN - Para fazer predições dos resultados dos testes de 11 vizinhos
y_pred_11 = classifier_11.predict(X_test)

# MODELO KNN - Métricas de performance do modelo
cm_KNN = confusion_matrix(y_test, y_pred_11)
print (cm_KNN)
print(accuracy_score(y_test, y_pred_11))
cm_KNN = confusion_matrix(y_test, y_pred_11)
acc_KNN = accuracy_score(y_test, y_pred_11)
sns.heatmap(cm_KNN, annot=True, fmt='d', cmap='Reds')
plt.xlabel('Precisão')
plt.ylabel('Atual')
plt.title('Confusion Matrix')
plt.show()
```
Dessa forma, a matriz de confusão obtida é:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/4da91f01-e122-40b6-abad-c6e1d218d28b)

Conclui-se que:
* Verdadeiros Positivos (83): São indivíduos com previsão correta de
risco de ataque cardíaco.
* Verdadeiros Negativos (976): Estes são indivíduos corretamente previstos como não correndo risco de ataque cardíaco.
* Falsos Positivos (166): São indivíduos com previsão incorreta de risco de ataque cardíaco.
* Falsos Negativos (528): São indivíduos com previsão incorreta de não correrem risco de ataque cardíaco.

A precisão de 0,604 indica que quando o modelo prevê que um indivíduo corre risco de ter um ataque cardíaco, **ele está correto em cerca de 60,4% das vezes.**

**Video de apresentação**: https://youtu.be/yTDmvu9SLxM

* MODELO DE REGRESSÃO LOGÍSTICA

Na construção do modelo de regressão logística, há a técnica de aprendizado de máquina voltado para problemas de classificação. Ele é utilizado para prever a probabilidade de um evento ocorrer, com base em um conjunto de variáveis independentes. Uma vez treinado, o modelo pode ser usado para fazer previsões sobre novos dados, atribuindo probabilidades às diferentes classes. Nesse sentido, a construção do modelo segue o código abaixo:

```python
# Conjunto de teste 20% e Kernel RBF
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.20, random_state=42)

svm_model = SVC(kernel='rbf', class_weight='balanced')
     
# Criar modelo
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Fazer previsões
y_pred = svm_model.predict(X_test)

# Calculo e metricas
print("Precisão:", accuracy_score(y_test, y_pred))
print("Matrix de confusão:\n", confusion_matrix(y_test, y_pred))
print("Classificação:\n", classification_report(y_test, y_pred))
# print("Recall: ", recall_score(y_test, y_pred))
# print("F1 Score: ", f1_score(y_test, y_pred))
```
O resultado obtido com o conjunto de treinamentos de 80% e de teste wem 20% foi:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/e4264f1b-5215-4aec-abd6-b3791ef57ce3)

Percebe-se a acurácia e m **51%**. Nesse sentido, em seguida, mudamos os valores de conjunto de teste para 45%:

```python

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.45, random_state=42)

svm_model = SVC(kernel='rbf', class_weight='balanced')
```

O resultado foi:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/700ef765-04cd-4112-9f1d-55735be4b2e3)

Neste caso, a acurácia ficou em **52%**

* MODELO RANDON FOREST

No Modelo Randon Forest, no pré-processamento de dados, consideramos:

```python
# Remover colunas não necessárias para o modelo
data_model = data.drop(columns=['Patient ID', 'Country', 'Continent', 'Hemisphere'])

# Codificar variáveis categóricas
label_encoder = LabelEncoder()
data_model['Sex'] = label_encoder.fit_transform(data_model['Sex'])
data_model['Diet'] = label_encoder.fit_transform(data_model['Diet'])

# Separar a coluna de pressão arterial em duas colunas separadas
data_model[['Systolic_BP', 'Diastolic_BP']] = data_model['Blood Pressure'].str.split('/', expand=True).astype(float)

# Remover a coluna original de pressão arterial
data_model = data_model.drop(columns=['Blood Pressure'])

# Converter colunas relevantes para valores numéricos
data_model['Heart Rate'] = pd.to_numeric(data_model['Heart Rate'], errors='coerce')
data_model['Income'] = pd.to_numeric(data_model['Income'], errors='coerce')
data_model['Triglycerides'] = pd.to_numeric(data_model['Triglycerides'], errors='coerce')
data_model['Physical Activity Days Per Week'] = pd.to_numeric(data_model['Physical Activity Days Per Week'], errors='coerce')

# Preencher valores ausentes com a média
data_model = data_model.fillna(data_model.mean())

# Exibir as primeiras linhas do dataframe processado para verificação
data_model.head()
```
Em seguida, definiu-se o conjunto de treinamento de dados

```python
# Separar variáveis de entrada (X) e saída (y)
X = data_model.drop(columns=['Heart Attack Risk'])
y = data_model['Heart Attack Risk']

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar os tamanhos dos conjuntos
print("Tamanho do conjunto de treino:", X_train.shape)
print("Tamanho do conjunto de teste:", X_test.shape)
```

Cujo resultado foi:

```python
# Matriz de Confusão
conf_matrix = confusion_matrix(y_test, y_pred_simple)

plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['No Risk', 'Risk'], yticklabels=['No Risk', 'Risk'])
plt.xlabel('Predito')
plt.ylabel('Verdadeiro')
plt.title('Matriz de Confusão do Modelo de Random Forest')
plt.show()
```

A Matriz de Confusão é apresentada abaixo:

  ![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/5b2b6b84-d303-4ba8-ab43-8a6045bfb734)

* MODELO NAIVE BAYES

No Modelo Naive Bayes, foi utulizada foi utilizada a SMOTE, como técnica para aumentar o número de casos do conjunto.

```python
# Aplicar SMOTE
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X_scaled, y)

# Dividir os dados em conjunto de treinamento e teste
X_train_res, X_test_res, y_train_res, y_test_res = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Treinar o modelo Naive Bayes
naive_bayes_model_res = GaussianNB()
naive_bayes_model_res.fit(X_train_res, y_train_res)

# Fazer previsões e avaliar o modelo
y_pred_res = naive_bayes_model_res.predict(X_test_res)
print("Precisão:", accuracy_score(y_test_res, y_pred_res))
print("Matriz de confusão:\n", confusion_matrix(y_test_res, y_pred_res))
print("Classificação:\n", classification_report(y_test_res, y_pred_res))
``

Os atributos foram selecionados para avalição do modelo.

```python
# Inserir novos dados para previsão
novos_dados = pd.DataFrame({
    'Age': [20],  # Exemplo: 50 anos
    'Sex': [0],  # 0 para feminino
    'Cholesterol': [120],  # Exemplo: 220 mg/dL
    'Heart Rate': [75],  # Exemplo: 75 bpm
    'Diabetes': [0],  # Sem diabetes
    'Family History': [1],  # Histórico familiar positivo
    'Smoking': [1],  # Fumante
    'Obesity': [1],  # Obeso
    'Alcohol Consumption': [2],  # Consumo de álcool (por exemplo, 2 unidades)
    'Exercise Hours Per Week': [1],  # 1 hora de exercício por semana
    'Diet': [0],  # Dieta não saudável
    'Previous Heart Problems': [0],  # Sem problemas cardíacos prévios
    'Medication Use': [1],  # Uso de medicação
    'Stress Level': [4],  # Nível de estresse (por exemplo, 4)
    'Sedentary Hours Per Day': [8],  # 8 horas sedentárias por dia
    'Income': [45000],  # Renda anual (por exemplo, 45.000)
    'BMI': [28],  # Índice de Massa Corporal (por exemplo, 28)
    'Triglycerides': [180],  # Triglicerídeos (por exemplo, 180 mg/dL)
    'Physical Activity Days Per Week': [2],  # 2 dias de atividade física por semana
    'Sleep Hours Per Day': [6],  # 6 horas de sono por dia
    'Systolic Pressure': [130],  # Pressão sistólica (por exemplo, 130 mmHg)
    'Dyastolic Pressure': [85]  # Pressão diastólica (por exemplo, 85 mmHg)
})

# Normalizar os novos dados
novos_dados_scaled = scaler.transform(novos_dados)

# Fazer a previsão
previsao = naive_bayes_model_res.predict(novos_dados_scaled)
previsao_proba = naive_bayes_model_res.predict_proba(novos_dados_scaled)

# Mostrar os resultados
print("\nPrevisão de risco de ataque cardíaco (0 = Baixo, 1 = Alto):", previsao[0])
print("Probabilidades:", previsao_proba[0])
```

O resultado final, obtido neste modelo foi:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/2e0d77e0-d5a6-4d3a-a7e2-df38075e6c33)


# Avaliação dos modelos criados

## Métricas utilizadas

* Modelo KNN

Para o Modelo KNN, avaliou-se as três métricas de precisão, recall e F1 Score.

```python
# Métricas Modelo KNN

def matriz_confusao(y_test, y_predit_11):

  # Recriando Matriz de Confusão
  matriz_confusao = confusion_matrix(y_test, y_predit_11)

  # Extraindo valores da matriz
  VP = matriz_confusao[0, 0]
  FN = matriz_confusao[0, 1]
  FP = matriz_confusao[1, 0]
  VN = matriz_confusao[1, 1]

  # Cálculo das métricas
  acuracia = (VP + VN) / (VP + VN + FP + FN)
  precisao = VP / (VP + FP)
  revocacao = VP / (VP + FN)
  f1_score = 2 * (precisao * revocacao) / (precisao + revocacao)

# Returnando as métricas e a matriz
  return matriz_confusao, acuracia, precisao, revocacao, f1_score

# Retornando os valores
matriz_confusao_personalizada, acuracia, precisao, revocacao, f1_score = matriz_confusao(y_test, y_pred_11)

# Imprimindo os resultados
print("Matriz de Confusão Personalizada:")
print(matriz_confusao_personalizada)
print("\nMetricas Personalizadas:")
print(f"Acurácia: {acuracia}")
print(f"Precisão: {precisao}")
print(f"Revocação: {revocacao}")
print(f"F1-Score: {f1_score}")
```

O resultado foi impresso abaixo:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/f7802633-e15f-4a30-9ea0-51c5d388c9c7)

Nesse aspecto, avalia-se que a taxa de precisão indica que de 100 avalialções, o modelo indica que **60,4%** deles, tenha um risco para ocorrência de ataque cardíaco.

* MODELO DE REGRESSÃO LOGÍSTICA

Tal qual para o modelo KNN, as métricas de avaliação do modelo de Regressão Logística foi semelhante. Considerando o primeiro cenário, de um conjunto de teste de 20%, os resultados são apresentados abaixo:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/ea7d90de-0636-43c1-b0b5-2807fcd8bc59)

Em seguida, testando as mesmas métrica no segundo cenário de um conjunto de treinamento em 45%, os resultados foram de:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/929b474d-ed83-42be-82ac-21e8173f26d0)


* MODELO MSE
  
Considerando o primeiro cenário, de um conjunto de teste de 20%, foi calculado o resultado do MSE (que é uma medida do erro do modelo na previsão de classes), obtendo o seguinte resultado:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273042/8c1a3211-f7fc-4130-aa1a-3b3038d93de5)

* MODELO RANDON FOREST

Os resultados para as métricas do Modelo Randon Forest são:4

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/7e650bae-529f-4acc-a976-21f67c9fe6bc)

* MODELO NAIVE BAYES

Para o modelo Naive Bayes, considerou-se também a avaliação de métricas dos modelos anrteriores.

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/8ac2b418-2532-4930-a9b6-86491fcbb99d)


## Discussão dos resultados obtidos

No Modelo KNN, os resultados obtidos obtiveram uma acurácia de **60,4%**. Sua simplicidade e flexibilidade o tornam uma escolha interessante. No entanto, sua eficácia pode ser limitada em conjuntos de dados de alta dimensionalidade ou com uma grande quantidade de ruído. Isto fica notório quando analisados os números de vizinhos distintos. Em última análise, a eficiência do KNN depende da escolha apropriada do parâmetro k (quantidade de vizinhos) e da natureza subjacente dos dados. Para aplicações onde a interpretabilidade é crucial ou onde a generalização é um desafio, o KNN pode ser uma escolha valiosa, tal qual como no dataset avaliado. Apesar de alguns desafios, o modelo KNN tem o potencial de contribuir significativamente para a previsão de ataques cardíacos neste conjunto de dados, fornecendo insights.

No Modelo MSE (Mean Squared Error), a acurácia se encontrou em **51%**, indica que o modelo está prevendo corretamente a classe alvo para cerca de metade dos exemplos no conjunto de dados de teste. Enquanto isso, uma precisão de 64% sugere que o modelo está fazendo um trabalho relativamente bom na identificação correta dos verdadeiros positivos em relação ao total de instâncias classificadas como positivas pelo modelo. Por outro lado, o MSE (Mean Squared Error) de 0.2321 é uma medida de erro que quantifica a média dos quadrados das diferenças entre os valores previstos pelo modelo e os valores reais do conjunto de dados de teste. Um valor de MSE mais baixo indica que o modelo está fazendo previsões mais precisas, pois os erros entre as previsões e os valores reais são menores em magnitude.

No modelo de Regressão Logística, uma acurácia de **52%** e uma precisão de 64% para um modelo de regressão logística sugerem um desempenho moderado na tarefa de classificação do conjunto de dados. A acurácia de 52% indica que o modelo está prevendo corretamente a classe alvo para aproximadamente metade dos exemplos no conjunto de dados de teste. A precisão de 64% indica que, entre todas as instâncias que o modelo previu como positivas, 64% delas realmente são positivas. Isso sugere que o modelo está realizando um trabalho melhor na identificação correta dos verdadeiros positivos, em comparação com a taxa de acurácia geral. 

No modelo Randon Forest, uma acurácia de **64%** indica um desempenho moderado na tarefa de classificação do conjunto de dados. O Random Forest é uma técnica de aprendizado de máquina baseada em árvores de decisão, que utiliza uma combinação de múltiplas árvores de decisão para fazer previsões. Uma acurácia de 64% sugere que o modelo está prevendo corretamente a classe alvo para cerca de dois terços dos exemplos no conjunto de dados de teste. Isso indica uma capacidade razoável do modelo em distinguir entre as diferentes classes ou categorias do problema em questão.

No modelo Naive Bayes, uma acurácia de **57%** sugere um desempenho razoável na tarefa de classificação do conjunto de dados. O Naive Bayes é um modelo probabilístico simples, mas poderoso, que é frequentemente utilizado em problemas de classificação, especialmente quando se lida com conjuntos de dados de texto ou com características categóricas. Uma acurácia de 57% indica que o modelo está prevendo corretamente a classe alvo para mais da metade dos exemplos no conjunto de dados de teste.


# Pipeline de pesquisa e análise de dados

## Pipeline 

Esta pipeline foi desenvolvida para realizar análises e previsões em um conjunto de dados relacionado ao risco de ataque cardíaco. Ela inclui as seguintes etapas:

1. Carregamento de Dados
A função `load_data` é responsável por carregar os dados do arquivo CSV heart_attack_prediction_dataset.csv e retornar um DataFrame Pandas contendo os dados.

2. Limpeza de Dados
A função `clean_data` realiza a limpeza dos dados, removendo colunas desnecessárias, tratando valores nulos e duplicados. Além disso, realiza transformações nos dados, como a separação da pressão sanguínea em duas colunas, diastólica e sistólica, e a transformação de variáveis categóricas em numéricas.

3. Pré-processamento de Dados
A função `preprocess_data` separa as variáveis preditoras da variável a ser prevista, normalizando as variáveis preditoras usando a função StandardScaler da biblioteca sklearn.

5. Treinamento
Modelo SVM: A função `train_svm` treina um modelo de Support Vector Machine (SVM) usando um kernel radial e pesos balanceados para lidar com classes desbalanceadas.
Regressão Linear: A função `train_linear_regression` treina um modelo de regressão linear usando as variáveis preditoras e a variável alvo.
Regressão Logística: A função `` treina um modelo de regessão logística com base nas variáveis preditoras. 
KNN: a função `classifier_1.fit(X_train, y_train)` treina um modelo de classificação consirando um númeo de vizinhos.
Randon Forest: A função `rf_model` treina o modelo randon forest.
Naive Bayes: A função `naive_bayes_model_res` treina um modelo.

7. Avaliação
Modelo SVM: A função `evaluate_model` avalia o modelo SVM usando o conjunto de teste, calculando a precisão, a matriz de confusão e o relatório de classificação.
Regressão Linear: A função `evaluate_model` avalia o modelo de regressão linear usando o conjunto de teste, calculando o erro quadrático médio (MSE).
Regressão Logística: A função `svm_model` avalia o modelo de regessão logística.
KNN: A função ` classifier_1.predict(X_test)` é usada para avaliar a predição do modelo KNN, considerano um número de vizinhos.
Randon Forest: A função `best_model` avalia o modelo randon forest.
Naive Bayes: A função `y_pred_res` avalia o desempenho do modelo. 
