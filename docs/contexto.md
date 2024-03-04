# Introdução

A prevenção e os cuidados relacionados a ataques cardíacos são grandes desafios para a saúde pública em todo o mundo. Compreender os fatores de risco e possíveis mitigadores é fundamental para a tomada de decisões mais assertivas, visando. Nesse contexto, a análise de dados e a descoberta de conhecimento são ferramentas essenciais para tomadas de decisão mais assertivas para melhorar a resposta aos tratamentos e à prevenção do risco. Este projeto de pesquisa e experimentação em sistemas de informação se propõe a explorar o conjunto de dados de predição de risco de ataque cardíaco para investigar a saúde do coração e seus fatores de risco.

O dataset "Heart Attack Risk Prediction Dataset" abrange uma ampla gama de atributos, como idade, níveis de colesterol, pressão arterial, hábitos de fumo, padrões de exercício, preferências alimentares e outros, com o objetivo de evidenciar possiveis interações dessas variáveis na determinação da probabilidade de um ataque cardíaco.

Com base nesse contexto, este trabalho tem como objetivo analisar e interpretar os dados desse dataset, visando identificar padrões e tendências que possam contribuir para aprimorar a prevenção e o tratamento de doenças cardíacas.

## Problema

Em um cenário do qual observa-se um aumento de casos de infarto no mundo (ESTADO DE MINAS, 2023), é imprescindível avaliar fatores que possam ser considerados de risco e ou que corroboram para a ocorrência de problemas cardíacos. Se obervada esta realidade sob a persperctiva nacional, o Brasil viu o número de casos de infarto aumentarem cerca de 25% desde 2016 a 2022, (AGÊNCIA BRASIL, 2023), o que requer mais atenção sobre a questão, dado o fato do número crescente de casos, se tornar um problema de saúde pública. Para além de entender fatores de risco para doenças cardíacas, o conhecimento dos mesmos, pode contribuir para a elaboração de estratégias de prevenção a curto, médio e longo prazo com vistas a mitigar a ocorrência de casos de infarto, por exemplo. 

É neste contexto que se insere o presente trabalho, buscando lançar luz à compreensão de fatores de risco que possam aumentar a ocorrência de ataques cardíacos, permitindo assim, traçar um perfil de pessoas mais sucetíveis a este tipo de problema de saúde. Desse modo, trazendo à compreensão, fatores de riscos e perfil de pessoas propensas à ataques cardíacos, instituições de saúde e unidades da atenção primária do Sistema Único de Saúde (SUS), por exemplo, podem criar estratégias efetivas de prevenção, campanhas educativas, atenção e foco aos grupos de pessoas com propensão a ataques cardíacos e realizar estudo demográfico para atuar diretamente com estas pessoas com a finalidade de previnir e acompanhar a população. 

## Questão de pesquisa

Com base na consideração de que, doenças cardíacas possam estar relacionadas ao contexto, hábitos e comportamentos das pessoas, questiona-se: _quais são os fatores de maior risco e que configuram em predisposição para ocorrência de ataques cardíacos nas pessoas?_

A questão de pesquisa é a base de todo o trabalho que será desenvolvido. É ela que motiva a realização da pesquisa e deverá ser adequada ao problema identificado. Ao término de sua pesquisa/experimentação, o objetivo é que seja encontrada a resposta da questão de pesquisa previamente definida.

## Objetivos preliminares

Como objetivo geral, buscamos experimentar e avaliar modelos de aprendizado de máquina adequados para solucionar o problema apresentado, visando desenvolver um modelo capaz de prever com precisão o risco de ataque cardíaco com base em uma ampla gama de atributos relacionados à saúde, estilo de vida e histórico médico dos pacientes. Utilizando para este trabalho uma base sólida para a investigação do padrão de características e fatores de risco associados à ocorrência de ataques cardíacos, o conjunto de dados "Heart Attack Risk Prediction Dataset".

Objetivos Específicos:

1.	Investigar padrões e correlações entre os diferentes atributos presentes no conjunto de dados "Heart Attack Risk Prediction Dataset" e a incidência de ataques cardíacos, utilizando técnicas de análise de dados que possam ser capazes de trazer um modelo eficaz e confiável para prever o risco.
2.	Identificar quais atributos exercem maior influência nas previsões de risco de ataque cardíaco feitas pelos modelos de aprendizado de máquina mais promissores, visando compreender como esses atributos se relacionam com o problema em questão e fornecendo informações relevantes para a prevenção e o manejo da condição cardíaca.

## Justificativa

Segundo a Associação Brasileira de Cardiologia, as doenças cardiovasculares, afecções do coração e da circulação, representam a principal causa de mortes no Brasil. São mais de 1100 mortes por dia, cerca de 46 por hora, 1 morte a cada 1,5 minutos (90 segundos). São mais de 1100 mortes por dia, cerca de 1 morte a cada 90 segundos, 2 vezes mais mortes que todos os tipos de câncer juntos. Muitas dessas mortes poderiam ser evitadas ou postergadas com cuidados preventivos e medidas terapêuticas. O alerta, a prevenção e o tratamento adequado dos fatores de risco e das doenças cardiovasculares podem reverter essa grave situação. Confira o cardiômetro em: (http://www.cardiometro.com.br/)

## Público-Alvo

Toda a população, independente do conhecimento em tecnologia, irá se beneficiar desse estudo. Especialmente aqueles que querem adotar práticas saudáveis para evitar doenças cardíacas, como alimentação, exercícios físicos, diminuição do consumo de bebidas ou tabaco, melhoria na qualidade de sono, etc.

## Estado da arte

Nesta seção, deverão ser descritas outras abordagens identificadas na literatura que foram utilizadas para resolver problemas similares ao problema em questão. Para isso, faça uma pesquisa detalhada e identifique, no mínimo, 3 trabalhos que tenham utilizado dados em contexto similares e então, detalhe: detalhe e contextualize o problema, descreva o _dataset_ utilizado, detalhe quais abordagens/algoritmos foram utilizados (e seus parâmetros), identifique as métricas de avaliação empregadas e fale sobre os resultados obtidos. 

> **Links Úteis**:
> - [Google Scholar](https://scholar.google.com/)
> - [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)
> - [Science Direct](https://www.sciencedirect.com/)
> - [ACM Digital Library](https://dl.acm.org/)

# Descrição do _dataset_ selecionado

Descrição do Dataset

O conjunto de dados ["Heart Attack Risk Prediction Dataset"](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset) é uma compilação fornecida pelo cientista de dados Sourav Banerjee, destinada a facilitar o desenvolvimento e a avaliação de modelos de aprendizado de máquina para prever ataques cardíacos. Este conjunto de dados foi gerado utilizando dados sintéticos criados pelo ChatGPT, um modelo de inteligência artificial. 
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

Nesta seção, você deverá estruturar o seu Canvas Analítico. O Canvas Analítico tem o papel de registrar a organização das ideias e apresentar o modelo de negócio.

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Referências

AGÊNCIA BRASIL. Casos de infarto aumentam 25% no Brasil, em 6 anos. Portal R7 [online], publicado em 03 ago. 2023. Disponível em: <https://noticias.r7.com/saude/casos-de-infarto-aumentam-25-no-brasil-em-6-anos-03082023> Acesso em 27 fev. 2024. 

ESTADO DE MINAS. Aumentam casos de infarto em todo o mundo; alerta OMS. Estado de Minas [online], publicado em 25 jul. 2023. Disponível em: <https://www.em.com.br/app/noticia/saude-e-bem-viver/2023/07/25/interna_bem_viver,1524784/aumentam-casos-de-infarto-em-todo-o-mundo-alerta-oms.shtml> Acesso em 27 fev. 2024. 

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
