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
```Phyton
from google.colab import files
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import geopandas as gpd
```

No _dataset_, a coluna cujo atributo corresponde ao ID, não terá valor de análise para os fatores de risco da ocorrência de ataques cardíacos, visto que, nesta, estão representados apenas dados para fim de identificação de pacientes, logo não sendo necessária sua utilização para analisar os dados. A imagem abaixo, demonstra o _dataset_ com a coluna 'Patient ID' excluída. 

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/cb88b123-207a-4185-b1da-e537edf3f3e6)

Com relação a dados duplicados e ou a atributos cujos valores estejam nulos, a contagem foi de zero, o que permite concluir que todos os 8763 registros não são nulos.

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/ee9ad668-c7a5-4f56-913a-2a21e9aaedf0)

* Transformação de Dados: normalize/padronize: torne os dados comparáveis, normalizando ou padronizando os valores para uma escala específica; codifique variáveis categóricas: converta variáveis categóricas em uma forma numérica, usando técnicas como _one-hot encoding_.

Como forma de padronização, as colunas que possuem valores cujas casas decimais são grandes, foram reduzidas para apenas uma, facilitando a leitura dos dados.

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/67bfae26-050f-4359-b9d6-cbf2dc82494a)

* _Feature Engineering_: crie novos atributos que possam ser mais informativos para o modelo; selecione características relevantes e descarte as menos importantes.

A coluna 'Blood Pressure' consta em um mesmo registro, a pressão diastólica e sistólica. Nesse contexto, é importante segregá-las de forma a garantir a melhor visualização dos dados, bem como análise dos mesmos. Assim, cirou-se novos atributos definidos em 'Systolic Pressure' e 'Dyastilic Pressure', excluindo a coluna anterior de 'Blood Pressure'.

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/de55d3dc-a34c-4607-8f33-43448aa01dd1)

* Tratamento de dados desbalanceados: se as classes de interesse forem desbalanceadas, considere técnicas como _oversampling_, _undersampling_ ou o uso de algoritmos que lidam naturalmente com desbalanceamento.

* Separação de dados: divida os dados em conjuntos de treinamento, validação e teste para avaliar o desempenho do modelo de maneira adequada.
  
* Manuseio de Dados Temporais: se lidar com dados temporais, considere a ordenação adequada e técnicas específicas para esse tipo de dado.
  
* Redução de Dimensionalidade: aplique técnicas como PCA (Análise de Componentes Principais) se a dimensionalidade dos dados for muito alta.

* Validação Cruzada: utilize validação cruzada para avaliar o desempenho do modelo de forma mais robusta.

* Monitoramento Contínuo: atualize e adapte o pré-processamento conforme necessário ao longo do tempo, especialmente se os dados ou as condições do problema mudarem.

* Entre outras....

Avalie quais etapas são importantes para o contexto dos dados que você está trabalhando, pois a qualidade dos dados e a eficácia do pré-processamento desempenham um papel fundamental no sucesso de modelo(s) de aprendizado de máquina. É importante entender o contexto do problema e ajustar as etapas de preparação de dados de acordo com as necessidades específicas de cada projeto.

# Descrição dos modelos

Nesta seção, conhecendo os dados e de posse dos dados preparados, é hora de descrever os algoritmos de aprendizado de máquina selecionados para a construção dos modelos propostos. Inclua informações abrangentes sobre cada algoritmo implementado, aborde conceitos fundamentais, princípios de funcionamento, vantagens/limitações e justifique a escolha de cada um dos algoritmos. 

Explore aspectos específicos, como o ajuste dos parâmetros livres de cada algoritmo. Lembre-se de experimentar parâmetros diferentes e principalmente, de justificar as escolhas realizadas.

Como parte da comprovação de construção dos modelos, um vídeo de demonstração com todas as etapas de pré-processamento e de execução dos modelos deverá ser entregue. Este vídeo poderá ser do tipo _screencast_ e é imprescindível a narração contemplando a demonstração de todas as etapas realizadas.

# Avaliação dos modelos criados

## Métricas utilizadas

Nesta seção, as métricas utilizadas para avaliar os modelos desenvolvidos deverão ser apresentadas (p. ex.: acurácia, precisão, recall, F1-Score, MSE etc.). A escolha de cada métrica deverá ser justificada, pois esta escolha é essencial para avaliar de forma mais assertiva a qualidade do modelo construído. 

## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelos modelos construídos, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade de cada um deles. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecendo relação com os objetivos previamente propostos. 

# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes. 
