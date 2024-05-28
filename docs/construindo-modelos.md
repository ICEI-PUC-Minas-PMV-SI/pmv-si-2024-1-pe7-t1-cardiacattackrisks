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

* Tratamento de dados desbalanceados: se as classes de interesse forem desbalanceadas, considere técnicas como _oversampling_, _undersampling_ ou o uso de algoritmos que lidam naturalmente com desbalanceamento.


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
```python

O resultado impresso foi:

```python
Acurácia Média: 0.63
Desvio Padrão dos Scores: 0.00
```

O que nos indica que a acurácia média foi de 63% com um desvio padrão de 0, signficando que o modelo é estável.

* Monitoramento Contínuo: atualize e adapte o pré-processamento conforme necessário ao longo do tempo, especialmente se os dados ou as condições do problema mudarem.

* Entre outras....

Avalie quais etapas são importantes para o contexto dos dados que você está trabalhando, pois a qualidade dos dados e a eficácia do pré-processamento desempenham um papel fundamental no sucesso de modelo(s) de aprendizado de máquina. É importante entender o contexto do problema e ajustar as etapas de preparação de dados de acordo com as necessidades específicas de cada projeto.

# Descrição dos modelos

* Modelo KNN

Considerando o modelo KNN como algoritmo de _machine learning_, este, traz a possibilidade de classificar cada amostra de um conjunto de dados avaliando sua distância em relação aos vizinhos mais próximos. Se os vizinhos mais próximos forem majoritariamente de uma classe, a amostra em questão será classificada nesta categoria.

Neste sentido, apresenta-se o modelo avaliado, abaixo:
```python
#Selecionando variáveis importantes pro modelo
X = data[['Sex', 'Age', 'Cholesterol', 'Heart Rate','Diabetes', 'Family History','Dyastolic Pressure','Systolic Pressure',
                        'Smoking', 'Obesity','Alcohol Consumption', 'Diet', 'Exercise Hours Per Week',
                        'Previous Heart Problems', 'Medication Use', 'Triglycerides', 'Sleep Hours Per Day']]

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

Criou-se quatro possibilidades de vizinhos para avaliar qual a melhor alternativa. Escolheu-se 3, 5, 7 e 12 vizinhos.
```python
classifier_12 = KNeighborsClassifier(n_neighbors=11)
```

Assim, treinamos o modelo KNN relacionado ao cenário de treinamento.
```python
classifier_11.fit(X_train, y_train)
```

E então, criou-se o algoritmo para fazer a predição dos resultados dos testes.
```python
y_pred_12 = classifier_11.predict(X_test)
```

Por fim, escolheu-se as métricas de avaliação das performances dos cenários do modelo criado.
```python
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

Sendo este, o resultado final:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/de03b9f4-46b9-42e8-9db1-4141002dfabd)

Conclui-se que:
* Verdadeiros Positivos (87): São indivíduos com previsão correta de
risco de ataque cardíaco.
* Verdadeiros Negativos (962): Estes são indivíduos corretamente previstos como não correndo risco de ataque cardíaco.
* Falsos Positivos (180): São indivíduos com previsão incorreta de risco de ataque cardíaco.
* Falsos Negativos (524): São indivíduos com previsão incorreta de não correrem risco de ataque cardíaco.

A precisão de 0,598 indica que quando o modelo prevê que um indivíduo corre risco de ter um ataque cardíaco, **ele está correto em cerca de 59,8% das vezes.**


___
Nesta seção, conhecendo os dados e de posse dos dados preparados, é hora de descrever os algoritmos de aprendizado de máquina selecionados para a construção dos modelos propostos. Inclua informações abrangentes sobre cada algoritmo implementado, aborde conceitos fundamentais, princípios de funcionamento, vantagens/limitações e justifique a escolha de cada um dos algoritmos. 

Explore aspectos específicos, como o ajuste dos parâmetros livres de cada algoritmo. Lembre-se de experimentar parâmetros diferentes e principalmente, de justificar as escolhas realizadas.

Como parte da comprovação de construção dos modelos, um vídeo de demonstração com todas as etapas de pré-processamento e de execução dos modelos deverá ser entregue. Este vídeo poderá ser do tipo _screencast_ e é imprescindível a narração contemplando a demonstração de todas as etapas realizadas.

# Avaliação dos modelos criados

## Métricas utilizadas

* Modelo KNN

Para o Modelo KNN, dentre as possibilidades de utilização de métricas, tem-se: distância euclidiana, distância de Manhattan, distância de Minkowski e distância de Hamming. Sendo a distância euclidiana a que mede a distância entre dois pontos (de consulta e o de medição), e dada sua facilidade de aplicação, escolheu-se esta, para avaliação métrica do modelo proposto. Os dados seguem abaixo:

```python
def dist_euclidiana(p1, p2):
# Calcula a distância euclidiana entre dois pontos no espaço multidimensional.
  p1 = np.array(p1)
  p2 = np.array(p2)

# Calcula a diferença entre os pontos
  diferenca = p1 - p2

# Eleva ao quadrado cada elemento da diferença
  quadrado_diferenca = diferenca ** 2

# Soma os elementos quadrados
  soma_quadrados = quadrado_diferenca.sum()

# Calcula a raiz quadrada da soma dos quadrados
  distancia = math.sqrt(soma_quadrados)

  return distancia

point_a = [1, 2, 3]
point_b = [4, 5, 6]
distance = dist_euclidiana(point_a, point_b)
print("Distância entre os pontos:", distance)
```

Sendo assim, o valor encontrado foi de: *5.196152422706632*, considerada uma distância curta e válida entre os pontos.

____
Nesta seção, as métricas utilizadas para avaliar os modelos desenvolvidos deverão ser apresentadas (p. ex.: acurácia, precisão, recall, F1-Score, MSE etc.). A escolha de cada métrica deverá ser justificada, pois esta escolha é essencial para avaliar de forma mais assertiva a qualidade do modelo construído. 

## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelos modelos construídos, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade de cada um deles. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecendo relação com os objetivos previamente propostos. 

# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes. 
