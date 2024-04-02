# Conhecendo os dados

Nesta seção, você deverá registrar uma detalhada análise descritiva e exploratória sobre a base de dados selecionada na Etapa 1 com o objetivo de compreender a estrutura dos dados, detectar eventuais _outliers_ e também, avaliar/detectar as relações existentes entre as variáveis analisadas. 

Para isso, sugere-se que você utilize cálculos de medidas de tendência central, como média, mediana e moda, para entender a centralidade dos dados; explorem medidas de dispersão como desvio padrão e intervalos interquartil para avaliar a variabilidade dos dados; utilizem gráficos descritivos como histogramas e box plots, para representar visualmente as características essenciais dos dados, pois essas visualizações podem facilitar a identificação de padrões e anomalias; analisem a relação aparente entre as variáveis por meio de análise de correlação ou gráficos de dispersões, entre outras técnicas. 

Inclua nesta seção, gráficos, tabelas e demais artefatos que você considere relevantes para entender os dados com os quais você irá trabalhar. 


# Tabelas de Dados

O dataset _Heart Attack Risk Prediction Dataset_ (BANERJEE, 2023), apresenta em sua totalidade, **8763** registros de dados distribuídos em 26 colunas com seus respectivos atributos.

| Atributo | Contagem | Tipo |
|----------|-----------|---------|
|Patient ID  |      8763   |               object|
|Age   |      8763   |                             int64|
|Sex    |       8763   |                          object|
|Cholesterol   |       8763   |                   int64|
|Blood Pressure   |         8763   |              object|
|Heart Rate  |        8763   |                     int64|
|Diabetes |       8763   |                         int64|
|Family History  |        8763   |                 int64|
|Smoking   |      8763   |                         int64|
|Obesity |      8763   |                           int64|
|Alcohol Consumption  |      8763   |              int64|
|Exercise Hours Per Week |      8763   |         float64|
|Diet    |        8763   |                        object|
|Previous Heart Problems   |        8763   |       int64|
|Medication Use  |      8763   |                   int64|
|Stress Level  |      8763   |                     int64|
|Sedentary Hours Per Day  |     8763   |         float64|
|Income|         8763   |                          int64|
|BMI   |       8763   |                          float64|
|Triglycerides |        8763   |                   int64|
|Physical Activity Days Per Week |   8763   |      int64|
|Sleep Hours Per Day |      8763   |               int64|
|Country  |        8763   |                       object|
|Continent |         8763   |                     object|
|Hemisphere  |        8763   |                    object|
|Heart Attack Risk   |      8763   |               int64|

Em se tratando dos registros e suas medidas centrais, a tabela abaixo explicita os valores representativos de cada atributo.

|index|Age|Cholesterol|Heart Rate|Diabetes|Family History|Smoking|Obesity|Alcohol Consumption|Exercise Hours Per Week|Previous Heart Problems|Medication Use|Stress Level|Sedentary Hours Per Day|Income|BMI|Triglycerides|Physical Activity Days Per Week|Sleep Hours Per Day|Heart Attack Risk|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|count|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|8763\.0|
|mean|53\.70797672030127|259\.8772110007988|75\.02168207234965|0\.6522880292137396|0\.4929818555289284|0\.8968389820837612|0\.5014264521282665|0\.5980828483396097|10\.01428365521483|0\.4958347597854616|0\.49834531553121075|5\.469702156795618|5\.993690145051085|158263\.18190117538|28\.891445877259635|417\.67705123816046|3\.48967248659135|7\.0235079310738335|0\.3582106584503024|
|std|21\.24950880221598|80\.86327610477055|20\.550947931909413|0\.47627118494942794|0\.4999792718957312|0\.3041864253995663|0\.5000264965985919|0\.49031335817956767|5\.783745486854243|0\.5000111809674499|0\.5000257933400908|2\.859621886586074|3\.4663591739806257|80575\.19080559704|6\.319181335543781|223\.7481367993549|2\.2826873241360377|1\.9884727543508285|0\.47950184613131047|
|min|18\.0|120\.0|40\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0024423483189783|0\.0|0\.0|1\.0|0\.0012632057782457|20062\.0|18\.002336577801902|30\.0|0\.0|4\.0|0\.0|
|25%|35\.0|192\.0|57\.0|0\.0|0\.0|1\.0|0\.0|0\.0|4\.981578612387105|0\.0|0\.0|3\.0|2\.998793697970296|88310\.0|23\.422985172976116|225\.5|2\.0|5\.0|0\.0|
|50%|54\.0|259\.0|75\.0|1\.0|0\.0|1\.0|1\.0|1\.0|10\.069559015591569|0\.0|0\.0|5\.0|5\.933622031172581|157866\.0|28\.768999353101115|417\.0|3\.0|7\.0|0\.0|
|75%|72\.0|330\.0|93\.0|1\.0|1\.0|1\.0|1\.0|1\.0|15\.050017847693944|1\.0|1\.0|8\.0|9\.019124487794615|227749\.0|34\.32459386532672|612\.0|5\.0|9\.0|1\.0|
|max|90\.0|400\.0|110\.0|1\.0|1\.0|1\.0|1\.0|1\.0|19\.998709051535457|1\.0|1\.0|10\.0|11\.999313410370352|299954\.0|39\.99721081557256|800\.0|7\.0|10\.0|1\.0|

 Na análise dos dados, consta o registro de **2652** mulheres, o que corresponde a **30%** dos registros totais, ao passo que o quantitativo de homens equivale a **70%** do total de dos dados, uma vez que o sexo masculino representa **6111** registros. Estes dados estatísticos permitem dizer que existe no _dataset_ uma proporção de um registro feminino para cada dois registros masculinos. Quando separados por sexos, as comorbidades e hábitos se configuram da seguinte forma:

|  Sexo | Idade Média | Qtde. Obesas(os) | Qtde. Diabéticas(os) | Qtde. Problemas Cardíacos Anteriores | Qtde. Usa Alcool |
|-------| :---: | :---: | :---:|  :---: |  :---: |
| Feminino | 53,1 | 1325 | 1723 | 1311 | 1582 |
| `% Feminino` | xx | `50%` | `65%` | `49,4%` | `59,7%`|
| Masculino | 54 | 3069 | 3993 | 3034 | 3659 |
| `% Masculino` | xx | `50,2%` | `65,3%` | `49,6%` | `59,9%` |

## Descrição dos achados


**Tabela por Sexo**: Considerando os aspectos levantados, ao serem segregados, em sexo, os dados apresentam algumas diferenças tanto em homens como mulheres. Nesse sentido, considera-se a tabela abaixo de atributos que correspondem a atributos comportamentais, que se traduzem em hábitose cotidianos e dados de saúde e ou comorbidades presentes. A tabela ainda apresenta, a porcentagem de homens e mulheres, em relação à divisão por sexo, de cada atributo apresentado.

Nota-se uma distribuição proporcional entre as porcentagens apresentadas considerando o quantitativo de homens e mulheres. Por exemplo, a diferença de idade médias entre as mulheres e homens se faz por quase um ano. Mesmo apresentando um número menor dos registros gerais, nota-se que as mulheres apresentam índices bem semelhantes, ao serem consideradas as porcentagens, em todos os atributos acima analisados. 


----

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

