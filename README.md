# API-para-tarefas

## Visão geral

O objetivo do sistema é realizar a gestão de tarefas colaborativas, por meio da criação, edição e atribuição das tarefas por meio da API. O contexto de uso do sistema é em algum onde envolva de preferencia mais de uma pessoa onde tenha de se distruir tarefas e organiza-las.

## Ferramentas que iremos utilizar:
- pytest
- PlantUML
- PostGreSQL

## Decisões arquiteturais:

Decidimos utilizar um Monolito em camadas por sua maior facilidade de separar as responsabilidades técnicas. Assim poderiamos separar o time de modo eficiente. Foi escolhido fazer o monolito com 4 camadas para manter um nível de organização sátisfatorio.

### Arquitetura:

- Presentation: É a visualização do sistema, ou seja, as rotas URL presentes. Se comunica com o workflow para pegar os dados nécessarios.
- Workflow: Faz a parte lógica enviando os dados para o presentation e utilizando as classes construidas no Model.
- Model: Cria classes com as regras de négocio que irão ser utilizadas no workflow. Utiliza os dados pegos do Persistence.
- Persistence: Se comunica com o banco de dados e envia os dados nécessarios para a criação das classes.