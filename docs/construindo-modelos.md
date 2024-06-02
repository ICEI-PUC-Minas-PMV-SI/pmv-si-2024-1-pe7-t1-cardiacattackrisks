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

## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelos modelos construídos, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade de cada um deles. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecendo relação com os objetivos previamente propostos. 

# Pipeline de pesquisa e análise de dados

1. Objetivo
O objetivo é identificar e prever a ocorrência de ataques cardíacos e a predisposição ao acomentimento cardíaco.

2. Pré-processamento
Carregar o Dataset: Leitura dos dados do dataset. Escalonamento: Normalização dos dados numéricos utilizando StandardScaler. Codificação de Categorias: Transformação de variáveis categóricas usando OneHotEncoder.

3. Treinamento
KNeighborsClassifier: ajustar o modelo com os parâmetros de KNN. Random Forest Classifier: ajustar o modelo com os parâmetros. Regressão Logística: Ajuste do modelo com regularização e número máximo de iterações.

3. Avaliação
Divisão de Dados: Separação dos dados em conjuntos de treino e teste. Treinamento e Previsão: Ajuste dos modelos e previsão no conjunto de teste. Métricas de Desempenho: Cálculo de acurácia, precisão, recall, F1-Score, ROC AUC, matriz de confusão e relatório de classificação.
