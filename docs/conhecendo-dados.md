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

No que tange às correçlações existentes entre as variávies, apresenta-se a tabela abaixo:

|index|Age|Cholesterol|Heart Rate|Diabetes|Family History|Smoking|Obesity|Alcohol Consumption|Exercise Hours Per Week|Previous Heart Problems|Medication Use|Stress Level|Sedentary Hours Per Day|Income|BMI|Triglycerides|Physical Activity Days Per Week|Sleep Hours Per Day|Heart Attack Risk|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Age|1\.0|-0\.00910701063969283|-0\.003844012945154017|-0\.014105213434238437|0\.008352546721025391|0\.39489091432012563|-0\.008140253421264306|-0\.006665596017035381|0\.0012056390050572136|0\.0008683616281732993|0\.0009803087037097943|0\.01830664566131858|0\.017280133983942306|-0\.0017327898671284717|-0\.0026118461704087844|0\.003414956659505406|0\.0013836678541333308|-0\.002184703739210194|0\.006403187125318214|
|Cholesterol|-0\.00910701063969283|1\.0|0\.0003149083294174119|-0\.01342760041373878|-0\.02160793026829518|0\.016341607914692493|-0\.014842648384970633|-0\.007261000606739182|0\.021517135566493085|-0\.006070178664482526|-0\.0009054425310133762|-0\.0244871110905082|0\.01891449191488843|6\.750208105444798e-06|0\.017291873784807475|-0\.0054537211761552535|0\.016055935475689797|0\.004456228582613036|0\.019339677892136278|
|Heart Rate|-0\.003844012945154017|0\.0003149083294174119|1\.0|0\.006763748530514302|-0\.013469587368609438|-0\.012330643382874333|0\.012724882179678553|0\.003458671942186603|0\.008276329316321948|-0\.00495590664577289|0\.009243998960559325|-0\.0045467685551276935|-0\.010232048377512735|0\.004873477440965434|0\.0052985747591283786|0\.012243694801044923|0\.0008343816729779274|0\.0018112469090847078|-0\.004251201581482037|
|Diabetes|-0\.014105213434238437|-0\.01342760041373878|0\.006763748530514302|1\.0|-0\.013843696963916373|0\.0005265323111556662|0\.012865760916360432|0\.005551206265933688|-0\.007013831184794394|0\.0008667310980527645|-0\.002655845045281188|0\.006719133528641532|0\.004705295940829123|-0\.0007589880801512673|-0\.002851836528283682|0\.010431358333307888|-0\.002411115064070384|-0\.012457271231808485|0\.017225295711578884|
|Family History|0\.008352546721025391|-0\.02160793026829518|-0\.013469587368609438|-0\.013843696963916373|1\.0|0\.01174828751525645|-0\.0014436141147544266|0\.01270131671673075|-0\.006377756223496969|-0\.0045680681791916596|0\.0009806962553440145|0\.015636554055179164|0\.0025611570219822993|-0\.0004012909952765952|-0\.011492146986037254|-0\.0019035517685535965|0\.009561448898569469|-0\.011198796568115916|-0\.0016519219073440718|
|Smoking|0\.39489091432012563|0\.016341607914692493|-0\.012330643382874333|0\.0005265323111556662|0\.01174828751525645|1\.0|0\.003968986023640297|0\.01275374980970103|-0\.00014988467243006956|-0\.0005743183605064951|-0\.0108769653242532|-0\.001756728181935342|0\.015311044719433583|0\.003096448036283063|0\.0076700789119769726|0\.004650031244345169|-0\.006465490622961278|-0\.005424471808788942|-0\.004051279234429711|
|Obesity|-0\.008140253421264306|-0\.014842648384970633|0\.012724882179678553|0\.012865760916360432|-0\.0014436141147544266|0\.003968986023640297|1\.0|-0\.02419541962978427|0\.002098948855734409|0\.00515919373879229|-0\.006267007873328741|0\.010625928437455787|-0\.0013332556334754752|-0\.003870405712281179|-0\.006058377957165032|0\.0014669466618646575|0\.005337384661184674|-0\.005313826619546813|-0\.013317552629224043|
|Alcohol Consumption|-0\.006665596017035381|-0\.007261000606739182|0\.003458671942186603|0\.005551206265933688|0\.01270131671673075|0\.01275374980970103|-0\.02419541962978427|1\.0|-0\.008514320376097837|0\.010395191612836226|0\.003338743753621287|-0\.005022997344944325|-0\.012828145768808193|-0\.02239570930818525|0\.010562454598823481|0\.006168607326112215|0\.0015934493120343524|-0\.000843415134960416|-0\.013777698296075043|
|Exercise Hours Per Week|0\.0012056390050572136|0\.021517135566493085|0\.008276329316321948|-0\.007013831184794394|-0\.006377756223496969|-0\.00014988467243006956|0\.002098948855734409|-0\.008514320376097837|1\.0|0\.005252545708932432|-0\.007119349875900455|-0\.009102419439617421|0\.008755601050657352|-0\.02341384725611319|0\.003776921494648434|0\.0017169490772933798|0\.007725186144341243|-0\.0012453363467734041|0\.011132824046918467|
|Previous Heart Problems|0\.0008683616281732993|-0\.006070178664482526|-0\.00495590664577289|0\.0008667310980527645|-0\.0045680681791916596|-0\.0005743183605064951|0\.00515919373879229|0\.010395191612836226|0\.005252545708932432|1\.0|0\.005336105746312259|-0\.017628581671840584|-0\.002694457155499742|-0\.00328056021779952|0\.015717920745041355|-0\.019029379874370988|0\.008536726813356208|0\.004460445894838307|0\.00027356445110160834|
|Medication Use|0\.0009803087037097943|-0\.0009054425310133762|0\.009243998960559325|-0\.002655845045281188|0\.0009806962553440145|-0\.0108769653242532|-0\.006267007873328741|0\.003338743753621287|-0\.007119349875900455|0\.005336105746312259|1\.0|0\.0008628768045902195|0\.02251303525274429|-0\.003463922358786042|0\.009514070353552765|-0\.01109535948087322|-0\.01113889547173548|-0\.020392583163618524|0\.0022344065306512013|
|Stress Level|0\.01830664566131858|-0\.0244871110905082|-0\.0045467685551276935|0\.006719133528641532|0\.015636554055179164|-0\.001756728181935342|0\.010625928437455787|-0\.005022997344944325|-0\.009102419439617421|-0\.017628581671840584|0\.0008628768045902195|1\.0|-0\.005397240902611481|-0\.002760451380170691|-0\.0032504472153539986|-0\.003921302511495453|0\.007404630242506285|-0\.01420540684311088|-0\.004111321714589336|
|Sedentary Hours Per Day|0\.017280133983942306|0\.01891449191488843|-0\.010232048377512735|0\.004705295940829123|0\.0025611570219822993|0\.015311044719433583|-0\.0013332556334754752|-0\.012828145768808193|0\.008755601050657352|-0\.002694457155499742|0\.02251303525274429|-0\.005397240902611481|1\.0|0\.003510620966801087|-2\.356073530539069e-05|-0\.005784608692504882|-0\.006178011547176589|0\.004792012622490198|-0\.005612974941699512|
|Income|-0\.0017327898671284717|6\.750208105444798e-06|0\.004873477440965434|-0\.0007589880801512673|-0\.0004012909952765952|0\.003096448036283063|-0\.003870405712281179|-0\.02239570930818525|-0\.02341384725611319|-0\.00328056021779952|-0\.003463922358786042|-0\.002760451380170691|0\.003510620966801087|1\.0|0\.008835837654686556|0\.010738559194557558|0\.00013027331760071906|-0\.006598343257861144|0\.009627602189392775|
|BMI|-0\.0026118461704087844|0\.017291873784807475|0\.0052985747591283786|-0\.002851836528283682|-0\.011492146986037254|0\.0076700789119769726|-0\.006058377957165032|0\.010562454598823481|0\.003776921494648434|0\.015717920745041355|0\.009514070353552765|-0\.0032504472153539986|-2\.356073530539069e-05|0\.008835837654686556|1\.0|-0\.00596360701960391|0\.008110374843879052|-0\.010030409695144208|2\.0279030747163066e-05|
|Triglycerides|0\.003414956659505406|-0\.0054537211761552535|0\.012243694801044923|0\.010431358333307888|-0\.0019035517685535965|0\.004650031244345169|0\.0014669466618646575|0\.006168607326112215|0\.0017169490772933798|-0\.019029379874370988|-0\.01109535948087322|-0\.003921302511495453|-0\.005784608692504882|0\.010738559194557558|-0\.00596360701960391|1\.0|-0\.007556419234625556|-0\.029215971122791867|0\.010471454380795617|
|Physical Activity Days Per Week|0\.0013836678541333308|0\.016055935475689797|0\.0008343816729779274|-0\.002411115064070384|0\.009561448898569469|-0\.006465490622961278|0\.005337384661184674|0\.0015934493120343524|0\.007725186144341243|0\.008536726813356208|-0\.01113889547173548|0\.007404630242506285|-0\.006178011547176589|0\.00013027331760071906|0\.008110374843879052|-0\.007556419234625556|1\.0|0\.014033437852993148|-0\.005013511103457075|
|Sleep Hours Per Day|-0\.002184703739210194|0\.004456228582613036|0\.0018112469090847078|-0\.012457271231808485|-0\.011198796568115916|-0\.005424471808788942|-0\.005313826619546813|-0\.000843415134960416|-0\.0012453363467734041|0\.004460445894838307|-0\.020392583163618524|-0\.01420540684311088|0\.004792012622490198|-0\.006598343257861144|-0\.010030409695144208|-0\.029215971122791867|0\.014033437852993148|1\.0|-0\.018528217440292413|
|Heart Attack Risk|0\.006403187125318214|0\.019339677892136278|-0\.004251201581482037|0\.017225295711578884|-0\.0016519219073440718|-0\.004051279234429711|-0\.013317552629224043|-0\.013777698296075043|0\.011132824046918467|0\.00027356445110160834|0\.0022344065306512013|-0\.004111321714589336|-0\.005612974941699512|0\.009627602189392775|2\.0279030747163066e-05|0\.010471454380795617|-0\.005013511103457075|-0\.018528217440292413|1\.0|

# Mapa de Calor 
![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-cardiacattackrisks/assets/81273377/15d3f696-87f2-468d-946e-74a2dad81d0d)

## Descrição dos achados


 Na análise dos dados, consta o registro de **2652** mulheres, o que corresponde a **30%** dos registros totais, ao passo que o quantitativo de homens equivale a **70%** do total de dos dados, uma vez que o sexo masculino representa **6111** registros. Estes dados estatísticos permitem dizer que existe no _dataset_ uma proporção de um registro feminino para cada dois registros masculinos. Quando separados por sexos, as comorbidades e hábitos se configuram da seguinte forma:

|  Sexo | Idade Média | Qtde. Obesas(os) | Qtde. Diabéticas(os) | Qtde. Problemas Cardíacos Anteriores | Qtde. Usa Alcool |
|-------| :---: | :---: | :---:|  :---: |  :---: |
| Feminino | 53,1 | 1325 | 1723 | 1311 | 1582 |
| `% Feminino` | xx | `50%` | `65%` | `49,4%` | `59,7%`|
| Masculino | 54 | 3069 | 3993 | 3034 | 3659 |
| `% Masculino` | xx | `50,2%` | `65,3%` | `49,6%` | `59,9%` |

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

