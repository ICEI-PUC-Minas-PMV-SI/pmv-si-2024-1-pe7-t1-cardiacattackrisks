# Introdução

A prevenção e os cuidados relacionados a ataques cardíacos são grandes desafios para a saúde pública em todo o mundo. Compreender os fatores de risco e possíveis mitigadores é fundamental para a tomada de decisões mais assertivas, visando. Nesse contexto, a análise de dados e a descoberta de conhecimento são ferramentas essenciais para tomadas de decisão mais assertivas para melhorar a resposta aos tratamentos e à prevenção do risco. Este projeto de pesquisa e experimentação em sistemas de informação se propõe a explorar o conjunto de dados de predição de risco de ataque cardíaco para investigar a saúde do coração e seus fatores de risco.

O dataset "Heart Attack Risk Prediction Dataset" (BANERJEE, 2023) abrange uma ampla gama de atributos, como idade, níveis de colesterol, pressão arterial, hábitos de fumo, padrões de exercício, preferências alimentares e outros, com o objetivo de evidenciar possiveis interações dessas variáveis na determinação da probabilidade de um ataque cardíaco.

Com base nesse contexto, este trabalho tem como objetivo analisar e interpretar os dados desse dataset, visando identificar padrões e tendências que possam contribuir para aprimorar a prevenção e o tratamento de doenças cardíacas.

## Problema

Em um cenário do qual observa-se um aumento de casos de infarto no mundo (ESTADO DE MINAS, 2023), é imprescindível avaliar fatores que possam ser considerados de risco e ou que corroboram para a ocorrência de problemas cardíacos. Se obervada esta realidade sob a persperctiva nacional, o Brasil viu o número de casos de infarto aumentarem cerca de 25% desde 2016 a 2022, (AGÊNCIA BRASIL, 2023), o que requer mais atenção sobre a questão, dado o fato do número crescente de casos, se tornar um problema de saúde pública. Para além de entender fatores de risco para doenças cardíacas, o conhecimento dos mesmos, pode contribuir para a elaboração de estratégias de prevenção a curto, médio e longo prazo com vistas a mitigar a ocorrência de casos de infarto, por exemplo. 

É neste contexto que se insere o presente trabalho, buscando lançar luz à compreensão de fatores de risco que possam aumentar a ocorrência de ataques cardíacos, permitindo assim, traçar um perfil de pessoas mais sucetíveis a este tipo de problema de saúde. Desse modo, trazendo à compreensão, fatores de riscos e perfil de pessoas propensas à ataques cardíacos, instituições de saúde e unidades da atenção primária do Sistema Único de Saúde (SUS), por exemplo, podem criar estratégias efetivas de prevenção, campanhas educativas, atenção e foco aos grupos de pessoas com propensão a ataques cardíacos e realizar estudo demográfico para atuar diretamente com estas pessoas com a finalidade de previnir e acompanhar a população. 

## Questão de pesquisa

Com base na consideração de que, doenças cardíacas possam estar relacionadas ao contexto, hábitos e comportamentos das pessoas, questiona-se: _quais são os fatores de maior risco e que configuram em predisposição para ocorrência de ataques cardíacos nas pessoas?_

A questão de pesquisa é a base de todo o trabalho que será desenvolvido. É ela que motiva a realização da pesquisa e deverá ser adequada ao problema identificado. Ao término de sua pesquisa/experimentação, o objetivo é que seja encontrada a resposta da questão de pesquisa previamente definida.

## Objetivos preliminares

Como objetivo geral se busca experimentar e avaliar modelos de aprendizado de máquina adequados para solucionar o problema apresentado, visando desenvolver um modelo capaz de prever com precisão o risco de ataque cardíaco com base em uma ampla gama de atributos relacionados à saúde, estilo de vida e histórico médico dos pacientes. Utilizando para este trabalho uma base sólida para a investigação do padrão de características e fatores de risco associados à ocorrência de ataques cardíacos, o conjunto de dados "Heart Attack Risk Prediction Dataset".

Objetivos Específicos:

1.	Investigar padrões e correlações entre os diferentes atributos presentes no conjunto de dados "Heart Attack Risk Prediction Dataset" e a incidência de ataques cardíacos, utilizando técnicas de análise de dados que possam ser capazes de trazer um modelo eficaz e confiável para prever o risco.
2.	Identificar quais atributos exercem maior influência nas previsões de risco de ataque cardíaco feitas pelos modelos de aprendizado de máquina mais promissores, visando compreender como esses atributos se relacionam com o problema em questão e fornecendo informações relevantes para a prevenção e o manejo da condição cardíaca.

## Justificativa

Segundo a Associação Brasileira de Cardiologia, as doenças cardiovasculares, afecções do coração e da circulação, representam a principal causa de mortes no Brasil. São mais de 1100 mortes por dia, cerca de 46 por hora, 1 morte a cada 1,5 minutos (90 segundos). São mais de 1100 mortes por dia, cerca de 1 morte a cada 90 segundos, 2 vezes mais mortes que todos os tipos de câncer juntos. Muitas dessas mortes poderiam ser evitadas ou postergadas com cuidados preventivos e medidas terapêuticas. O alerta, a prevenção e o tratamento adequado dos fatores de risco e das doenças cardiovasculares podem reverter essa grave situação. Confira o cardiômetro em: (http://www.cardiometro.com.br/)
O assunto foi escolhido devido a importância do mesmo para a sociedade e a qualidade dos dados a serem avaliados. O projeto busca contribuir para a qualidade de vida da população.

## Público-Alvo

Toda a população, independente do conhecimento em tecnologia, irá se beneficiar desse estudo. Especialmente aqueles que querem adotar práticas saudáveis para evitar doenças cardíacas, como alimentação, exercícios físicos, diminuição do consumo de bebidas ou tabaco, melhoria na qualidade de sono, etc.

## Estado da arte


### 1. Identification of Cardiovascular Diseases Using Machine Learning 

#### Contexto 

A doença cardiovascular, ou doença cardíaca, é uma das principais causas de morte em todo o mundo, com um aumento contínuo previsto nas próximas décadas.  Diversos fatores de risco estão associados ao desenvolvimento de doenças cardíacas, incluindo mudanças no estilo de vida, tabagismo, dieta, atividade física, obesidade e condições bioquímicas como pressão arterial e níveis de glicose. 

Para lidar com o desafio do diagnóstico preciso e eficiente das doenças cardíacas, várias abordagens de análise de dados e algoritmos de aprendizado de máquina têm sido explorados. Um estudo recente de Louridi, Amar e Ouahidi (2019) apresentou uma investigação importante nesse campo. Os autores propuseram um modelo de identificação de doenças cardiovasculares utilizando técnicas de aprendizado de máquina. 

#### Dataset Utilizado 

No estudo de Louridi et al. (2019), foi utilizado um conjunto de dados específico para identificação de doenças cardiovasculares. Este dataset consistiu em 303 instâncias e 13 atributos relevantes para fatores de risco cardíaco. Os dados foram obtidos a partir do repositório de aprendizado de máquina da UCI, contribuído por Robert Detrano, M.D, Ph.D. 

#### Abordagens/Algoritmos Utilizados 

Para a tarefa de identificação de doenças cardíacas, os pesquisadores empregaram uma variedade de algoritmos de aprendizado de máquina, incluindo Máquinas de Vetores de Suporte (SVM), Naïve Bayes (NB) e K-vizinhos mais próximos (KNN). 

Máquinas de Vetores de Suporte (SVM): Este algoritmo foi utilizado para criar um hiperplano no espaço de características que pudesse separar os dados de forma distinta. O SVM foi configurado com um kernel linear, pois os dados mostraram-se linearmente separáveis . 

Naïve Bayes (NB): Um classificador popular de aprendizado de máquina baseado no teorema de Bayes, assumindo independência entre as características [3]. 

K-vizinhos mais próximos (KNN): Um algoritmo que utiliza a proximidade entre os vizinhos para classificação. 

#### Métricas de Avaliação 

As métricas de avaliação utilizadas pelos pesquisadores incluíram especificidade, sensibilidade e precisão. A especificidade avalia a proporção de casos negativos corretamente identificados, enquanto a sensibilidade (recall) mede a proporção de amostras positivas corretamente identificadas. Já a precisão verifica a eficiência do modelo construído. 

#### Resultados Obtidos 

Os resultados experimentais do estudo de Louridi et al. (2019) indicaram que o algoritmo SVM com kernel linear obteve a melhor precisão, atingindo um valor de 86,8% na identificação de doenças cardiovasculares. 

Esta pesquisa evidencia a importância do uso de técnicas de aprendizado de máquina na identificação e previsão de doenças cardíacas, fornecendo insights valiosos para a melhoria contínua da detecção precoce e tratamento dessas condições. 

### 2. Cardiovascular Disease Risk Assessment using Machine Learning 

#### Contexto

A avaliação do risco de DCV é crucial para garantir um diagnóstico e tratamento adequados, permitindo que os pacientes com necessidades críticas tenham acesso prioritário aos médicos e sistemas de saúde. No entanto, a complexidade dos algoritmos utilizados nesse processo muitas vezes dificulta a interpretação dos resultados pelos profissionais de saúde. Nesse sentido, o uso de abordagens de aprendizado de máquina, como a Regressão Logística, tem sido explorado como uma solução promissora para prever o risco de DCV de forma precisa e eficaz.

#### Dataset Utilizado 

No estudo realizado por Prakash, Mahesh e Gouthaman (2023), o dataset utilizado para a avaliação do risco de DCV inclui informações de vários pacientes. Um total de 13 atributos foram utilizados para treinar o modelo de Regressão Logística, tais como idade, sexo, pressão sanguínea, níveis de colesterol, entre outros. Esses atributos foram escolhidos com base em sua relevância clínica e importância como fatores de risco para DCV.

#### Abordagens/Algoritmos Utilizados 

No estudo, foi empregado o algoritmo de Regressão Logística, uma técnica de aprendizado de máquina que modela a relação entre uma variável de resultado (no caso, o risco de DCV) e variáveis independentes (como idade, sexo, pressão sanguínea, etc.). A Regressão Logística é conhecida por sua simplicidade, eficiência computacional e capacidade de fornecer probabilidades como resultados.

Parâmetros do Modelo:
Os parâmetros do modelo de Regressão Logística foram ajustados durante o treinamento usando o dataset disponível. Estes incluem os coeficientes que relacionam as variáveis independentes ao risco de DCV, bem como a função de ativação sigmoidal utilizada para calcular as probabilidades.

#### Métricas de Avaliação
Para avaliar a eficácia do modelo de Regressão Logística na predição do risco de DCV, várias métricas foram empregadas, incluindo a precisão (accuracy), que representa a proporção de previsões corretas em relação ao total de previsões feitas pelo modelo.

#### Resultados Obtidos
Os resultados do estudo indicaram que o modelo de Regressão Logística alcançou uma precisão de 86.89% na predição do risco de DCV. Essa alta precisão sugere que o modelo é capaz de identificar eficientemente pacientes com alto risco de DCV, permitindo a implementação de medidas preventivas e planos de tratamento adequados.

#### Conclusão
Em conclusão, o estudo demonstra que a utilização da Regressão Logística para a avaliação do risco de DCV é uma abordagem eficaz e promissora. A alta precisão do modelo sugere sua utilidade prática na identificação precoce e no gerenciamento do risco de DCV. Esse avanço pode contribuir significativamente para a eficiência e eficácia dos sistemas de saúde, garantindo um cuidado mais personalizado e direcionado para pacientes com necessidades específicas relacionadas à DCV.


### 3. Heart Attack Prediction Using Artificial Neural Networks 

 

#### Contexto e Problema: 

O problema abordado por Bharathi et al. (2023) é a previsão de ataques cardíacos, uma questão vital devido à sua relevância na identificação precoce de riscos cardiovasculares e intervenções preventivas. A importância desse problema reside na capacidade de desenvolver sistemas de suporte à decisão que identifiquem riscos de ataques cardíacos em estágios iniciais, permitindo intervenções precoces para reduzir a gravidade das doenças cardiovasculares. 

#### Dataset Utilizado: 

O dataset utilizado neste estudo consiste em 13 características de 1024 instâncias, incluindo informações como idade, gênero, sintomas como dor no peito e outros fatores relevantes para a previsão de ataques cardíacos. Esses dados foram coletados da UCI (University of California, Irvine), proporcionando um conjunto diversificado e rico em informações para análise. 

#### Abordagem/Algoritmos: 

Para abordar o problema, Bharathi et al. (2023) utilizaram diversas técnicas, incluindo: 

Redes Neurais Artificiais (ANN): 

 

As Redes Neurais Artificiais são estruturas de aprendizado de máquina inspiradas no funcionamento do cérebro humano. O estudo empregou modelos de ANN com diferentes configurações de camadas e neurônios, visando prever ataques cardíacos com precisão. Os parâmetros específicos das redes foram ajustados durante o treinamento para otimizar o desempenho. 

 

Algoritmo de Quantização de Vetor de Aprendizado: 

 

Este algoritmo é uma técnica de Rede Neural Artificial utilizada para quantizar dados de entrada em vetores. Em seguida, esses vetores são treinados para prever a ocorrência de ataques cardíacos. Os parâmetros do algoritmo foram ajustados para maximizar a precisão da previsão. 

 

Support Vector Machine (SVM): 

 

O SVM é um algoritmo de aprendizado de máquina utilizado para classificação e regressão. No estudo de Bharathi et al. (2023), o SVM foi empregado para treinar modelos com base nas características dos pacientes e prever a ocorrência de ataques cardíacos. Os parâmetros do SVM, como o kernel utilizado e o parâmetro de regularização, foram ajustados para melhorar a precisão da previsão. 

 

Métodos de Mineração de Dados: 

 

Além das técnicas baseadas em Redes Neurais e SVM, o estudo também explorou métodos de mineração de dados, como Naïve Bayes e kmeans. Esses métodos foram aplicados para prever a ocorrência de ataques cardíacos com base nas características dos pacientes. 

 

#### Métricas de Avaliação: 

As métricas de avaliação utilizadas para medir o desempenho dos modelos incluíram: 

Matriz de Confusão: 

 

Esta métrica é uma ferramenta comum para problemas de classificação, fornecendo uma visão geral dos resultados corretos e incorretos das previsões. 

Precisão do Modelo: 

 

A precisão do modelo foi calculada com base na matriz de confusão, representando a proporção de previsões corretas em relação ao total de previsões feitas. 

 

#### Resultados: 

Os resultados obtidos por Bharathi et al. (2023) demonstraram a eficácia das abordagens utilizadas na previsão de ataques cardíacos. As Redes Neurais Artificiais apresentaram uma precisão média de 84% a 88%, enquanto o SVM alcançou uma precisão de 87,5% em um estudo específico. Além disso, métodos de mineração de dados como Naïve Bayes e kmeans obtiveram uma precisão em torno de 93% na previsão de ataques cardíacos. 

Em resumo, o estudo evidencia que a combinação de Redes Neurais Artificiais, SVM e métodos de mineração de dados é promissora na previsão de ataques cardíacos. A escolha adequada de algoritmos e ajuste de parâmetros influenciam diretamente na precisão dos modelos, fornecendo insights valiosos para a identificação precoce de riscos cardiovasculares e intervenções preventivas eficazes. 
 


# Descrição do _dataset_ selecionado

Descrição do Dataset

O conjunto de dados "Heart Attack Risk Prediction Dataset" (BANERJEE, 2023) é uma compilação fornecida pelo cientista de dados Sourav Banerjee, destinada a facilitar o desenvolvimento e a avaliação de modelos de aprendizado de máquina para prever ataques cardíacos. Este conjunto de dados foi gerado utilizando dados sintéticos criados pelo ChatGPT, um modelo de inteligência artificial. 
Este conjunto de dados contém uma ampla gama de atributos relevantes para a saúde cardíaca e escolhas de estilo de vida, abrangendo detalhes específicos do paciente. Abaixo está a descrição detalhada de cada um dos atributos presentes no dataset:

- ID do Paciente: Identificador exclusivo para cada paciente.
- Idade: Idade do paciente (tipo: numérico).
- Sexo: Gênero do paciente (Masculino/Feminino).
- Colesterol: Níveis de colesterol do paciente (tipo: numérico).
- Pressão Arterial: Pressão arterial do paciente (sistólica/diastólica) (tipo: numérico).
- Frequência Cardíaca: Frequência cardíaca do paciente (tipo: numérico).
- Diabetes: Se o paciente tem diabetes (Sim/Não).
- História Familiar: História familiar de problemas cardíacos (1: Sim, 0: Não).
- Tabagismo: Tabagismo do paciente (1: Fumante, 0: Não fumante).
- Obesidade: Estado de obesidade do paciente (1: Obeso, 0: Não obeso).
- Consumo de Álcool: Nível de consumo de álcool pelo paciente (Nenhum/Leve/Moderado/Pesado).
- Horas de exercício por semana: Número de horas de exercício por semana (tipo: numérico).
- Dieta: Hábitos alimentares do paciente (Saudável/Médio/Não saudável).
- Problemas Cardíacos Anteriores: Problemas cardíacos anteriores do paciente (1: Sim, 0: Não).
- Uso de Medicamentos: Uso de medicamentos pelo paciente (1: Sim, 0: Não).
- Nível de Estresse: Nível de estresse relatado pelo paciente (escala de 1 a 10).
- Horas sedentárias por dia: Horas de atividade sedentária por dia (tipo: numérico).
- Renda: Nível de renda do paciente (tipo: numérico).
- IMC: Índice de Massa Corporal (IMC) do paciente (tipo: numérico).
- Triglicerídeos: Níveis de triglicerídeos do paciente (tipo: numérico).
- Dias de atividade física por semana: Dias de atividade física por semana (tipo: numérico).
- Horas de sono por dia: Horas de sono por dia (tipo: numérico).
- País: País do paciente.
- Continente: Continente onde o paciente reside.
- Hemisfério: Hemisfério onde o paciente reside.
- Risco de ataque cardíaco: Presença de risco de ataque cardíaco (1: Sim, 0: Não).

Este conjunto de dados possui 8.763 registros de pacientes em todo o mundo. Os atributos são predominantemente numéricos, com algumas variáveis categóricas.

# Canvas analítico

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/fe39e792-bc1c-44e6-8dae-49eb5895fdd3)

# Referências

AGÊNCIA BRASIL. Casos de infarto aumentam 25% no Brasil, em 6 anos. Portal R7 [online], publicado em 03 ago. 2023. Disponível em: <https://noticias.r7.com/saude/casos-de-infarto-aumentam-25-no-brasil-em-6-anos-03082023> Acesso em 27 fev. 2024. 

BANERJEE, Sourav. Heart Attack Risk Prediction Dataset: Unlocking Predictive Insights with Multifaceted Synthetic Heart Attack Dataset. Kaggle [online], publicado em nov. 2023. Disponível em: <https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset>. Acesso em 29 fev. 2024.

ESTADO DE MINAS. Aumentam casos de infarto em todo o mundo; alerta OMS. Estado de Minas [online], publicado em 25 jul. 2023. Disponível em: <https://www.em.com.br/app/noticia/saude-e-bem-viver/2023/07/25/interna_bem_viver,1524784/aumentam-casos-de-infarto-em-todo-o-mundo-alerta-oms.shtml> Acesso em 27 fev. 2024. 


N. Louridi, M. Amar and B. E. Ouahidi, "Identification of Cardiovascular Diseases Using Machine Learning," 2019 7th Mediterranean Congress of Telecommunications (CMT), Fez, Morocco, 2019, pp. 1-6, doi: 10.1109/CMT.2019.8931411. keywords: {Heart;Diseases;Support vector machines;Machine learning algorithms;Machine learning;Classification algorithms;Blood pressure;Heart disease;Support vector machine (SVM);Naïve Bayes (NB);K-nearest neighbors (KNN);Normalization},  Acesso em 04 mar. 2024.

N. Prakash, M. Mahesh and P. Gouthaman, "Cardiovascular Disease Risk Assessment using Machine Learning," 2023 International Conference on Inventive Computation Technologies (ICICT), Lalitpur, Nepal, 2023, pp. 249-256, doi: 10.1109/ICICT57646.2023.10133957. keywords: {Training;Machine learning algorithms;Medical services;Machine learning;Prediction algorithms;Risk management;Cardiovascular diseases;Cardiovascular Disease;Logistic Regression;Machine Learning;Risk Assessment}, Acesso em 05 mar. 2024.

N. N. Bharathi, M. F. Shaik, T. Poojita, T. Sravanthi, M. Rafi and I. R. Raja, "Heart Attack Prediction Using Artificial Neural Networks," 2023 9th International Conference on Advanced Computing and Communication Systems (ICACCS), Coimbatore, India, 2023, pp. 304-308, doi: 10.1109/ICACCS57279.2023.10112664. keywords: {Heart;Decision support systems;Sociology;Decision making;Artificial neural networks;Cardiac arrest;Organizations;ANN;Heart attack prediction;Jupiter Lab}, Acesso em 05 mar. 2024.








> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
