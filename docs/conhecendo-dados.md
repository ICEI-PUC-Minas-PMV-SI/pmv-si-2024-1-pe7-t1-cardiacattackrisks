# Conhecendo os dados

Nesta seção, você deverá registrar uma detalhada análise descritiva e exploratória sobre a base de dados selecionada na Etapa 1 com o objetivo de compreender a estrutura dos dados, detectar eventuais _outliers_ e também, avaliar/detectar as relações existentes entre as variáveis analisadas.

Para isso, sugere-se que você utilize cálculos de medidas de tendência central, como média, mediana e moda, para entender a centralidade dos dados; explorem medidas de dispersão como desvio padrão e intervalos interquartil para avaliar a variabilidade dos dados; utilizem gráficos descritivos como histogramas e box plots, para representar visualmente as características essenciais dos dados, pois essas visualizações podem facilitar a identificação de padrões e anomalias; analisem a relação aparente entre as variáveis por meio de análise de correlação ou gráficos de dispersões, entre outras técnicas. 

Inclua nesta seção, gráficos, tabelas e demais artefatos que você considere relevantes para entender os dados com os quais você irá trabalhar. 


O dataset _Heart Attack Risk Prediction Dataset_ (BANERJEE, 2023), apresenta em sua totalidade, **8763** registros de dados distribuídos em 26 colunas com seus respectivos atributos. 

Na análise dos dados, consta o registro de **2652** mulheres, o que corresponde a **30%** dos registros totais, ao passo que o quantitativo de homens equivale a **70%** do total de dos dados, uma vez que o sexo masculino representa **6111** registros. Estes dados estatísticos permitem dizer que existe no _dataset_ uma proporção de um registro feminino para cada dois registros masculinos.

Em se tratando dos registros e suas medidas centrais, a tabela abaixo explicita os valores representativos de cada atrributo numérico.

| |Idade|Colesterol|Frequência Cardíaca|Hora Exercício/Semana|Nível Estresse|Horas Sedentárias/Dia|Renda| IMC |Triglicerídios|Dias Atividade Física|Horas Sono/Dia|
|-|-----|-----------|--------------|--------------|----------------|-----------------------|----| ---| ----| ----| -----|
|Média| 53,7 | 259,9 |  75  | 1,18 |  5,4  |  1,16  | 158.263,18 |   | 417,7 |  3,4 | 10 |
|Moda| 90 | 235 | 94 |     |  2 |    |  22.527,80 |    | 799 | 3 | 10 |
|Mínimo| 18 | 120 | 40 | 1,48 | 1 |   | 20.062,00 |    | 30 | 0 | 4 |
|Máximo| 90 | 400 | 110 | 7,9 | 10 |   | 299.954,00 |   | 800 | 7 | 10 |

## Descrição dos achados

A partir da análise descrita e exploratória realizada, descreva todos os achados considerados relevantes para o contexto em que o trabalho se insere. Por exemplo: com relação à centralidade dos dados algo chamou a sua atenção? foi possível identificar correlação entre os atributos?

## Ferramentas utilizadas

Existem muitas ferramentas diferentes que podem ser utilizadas para fazer a análise dos dados. Nesta seção, descreva as ferramentas/tecnologias utilizadas e sua aplicação.

### Rascunho

#### Qual a relação com idade?
- Idade e Risco de ataque cardíaco

##### Possiveis correlacoes com idade
- Idade e Colesterol
- Idade e Pressão Arterial
- Idade e IMC
- Idade e Triglicerídeos
- Idade e Horas de exercício por semana
- Idade e Horas sedentárias por dia
- Idade e Renda
- Idade e Nível de Estresse
- Idade e Horas de sono por dia

#### Qual a relação com atividade fisica?
- Horas de exercício por semana e Risco de ataque cardíaco
- Horas sedentárias por dia e Risco de ataque cardíaco

##### Possiveis correlacoes com atividade fisica
- Horas de exercício por semana e Horas sedentárias por dia
- Horas de exercício por semana e Renda
- Horas de exercício por semana e Nível de Estresse
- Horas de exercício por semana e Horas de sono por dia
- Horas sedentárias por dia e Renda
- Horas sedentárias por dia e Nível de Estresse
- Horas sedentárias por dia e Horas de sono por dia
- Nível de Estresse e Horas de sono por dia

#### Renda influencia?
- Renda e Risco de ataque cardíaco

##### Possiveis correlacoes com atividade fisica
- Renda e Nível de Estresse
- Renda e Horas de sono por dia

#### Fatores de saude influencia?
- Colesterol e Risco de ataque cardíaco
- Pressao Arterial e Risco de ataque cardíaco
- IMC e Risco de ataque cardíaco
- Triglicerideos e Risco de ataque cardíaco

##### Possiveis correlacoes com saude
- Colesterol e Pressão Arterial
- Colesterol e IMC
- Colesterol e Triglicerídeos
- Colesterol e Horas de exercício por semana
- Colesterol e Horas sedentárias por dia
- Colesterol e Renda
- Colesterol e Nível de Estresse
- Colesterol e Horas de sono por dia
- Pressão Arterial e IMC
- Pressão Arterial e Triglicerídeos
- Pressão Arterial e Horas de exercício por semana
- Pressão Arterial e Horas sedentárias por dia
- Pressão Arterial e Renda
- Pressão Arterial e Nível de Estresse
- Pressão Arterial e Horas de sono por dia
- IMC e Triglicerídeos
- IMC e Horas de exercício por semana
- IMC e Horas sedentárias por dia
- IMC e Renda
- IMC e Nível de Estresse
- IMC e Horas de sono por dia
- Triglicerídeos e Horas de exercício por semana
- Triglicerídeos e Horas sedentárias por dia
- Triglicerídeos e Renda
- Triglicerídeos e Nível de Estresse
- Triglicerídeos e Horas de sono por dia

