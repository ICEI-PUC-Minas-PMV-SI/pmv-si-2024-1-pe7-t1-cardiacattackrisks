# Implantação da solução

Dentre os provedores testados — Azure, AWS e Google Cloud — foi escolhido o Azure por conta do desempenho satisfatório, facilidade de implantação, compatibilidade com o Docker e, principalmente, a parceria com a PUC Minas.

Primeiramente, foi criada uma aplicação chamada HeartAttackRiskPrediction no ambiente cloud. Para tanto, foi criada uma máquina Linux na região East US.

Não foi necessária a criação de banco de dados.

Foi criado um container Docker dentro da aplicação na plataforma Microsoft Azure. O código foi hospedado na plataforma Docker Hub, em um repositório privado chamado puc_minas.

Por fim, a aplicação foi publicada com acesso público. A plataforma Azure gerou uma assinatura e ficou disponível pelo endereço https://heartattackriskprediction.azurewebsites.net/

Configurações básicas: Máquina Linux, Infraestrutura compartilhada, 1 GB de memória, SKU gratuito e região East US.

# Apresentação da solução

Em conclusão, a análise comparativa dos modelos KNN, SVM, Regressão Logística, Random Forest e Naive Bayes para a previsão de ataques cardíacos revelou desempenhos variados. O Random Forest obteve a maior acurácia (64%), seguido pelo KNN (60,4%). Embora o SVM e a Regressão Logística apresentem acurácia moderada, suas precisões indicam um desempenho razoável na identificação de verdadeiros positivos. O Naive Bayes, com uma acurácia de 57%, também mostrou ser uma escolha viável. Cada modelo possui suas vantagens e limitações e a escolha do modelo ideal dependerá das especificidades do conjunto de dados e dos requisitos da aplicação.

Também é importante observar que todos os modelos podem ser evoluídos. Talvez, com mais experiência do grupo e tempo, os modelos possam apresentar resultados mais satisfatórios, colaborando com o curso da sociedade no tratamento e prevenção de ataques cardíacos.<video controls src="apresentacao-aplicacao.mp4" title="Title"></video>


## Descrição da Solução

A solução consiste em uma aplicação web para previsão de risco de ataque cardíaco. Utilizamos modelos de machine learning (KNN, Random Forest e SVM) para fazer as previsões com base em dados de saúde fornecidos pelos usuários. A aplicação inclui um front-end em HTML, CSS e JavaScript e um back-end em Flask (Python).
