<h1>Processo de Data Lake - Empresa Financeira</h1>

## Descrição do projeto 

<p align="justify">
  O objetivo deste projeto é criar um Data Lake para otimizar a agregação de informações e acelerar a tomada de decisões por parte dos gestores e diretores.
</p>

## Funcionalidades

:heavy_check_mark: Modelagem de Banco de Dados

:heavy_check_mark: Ingestão de Dados

:heavy_check_mark: ETL Distribuído

:heavy_check_mark: Exportação CSV


## Pré-requisitos

<dl>MySQL "https://dev.mysql.com/downloads/mysql/"</dl>
<dl>Python "https://www.python.org/downloads/"</dl>
<dl>Visual Studio Code "https://code.visualstudio.com/download"</dl>
<dl>Apache Spark "https://spark.apache.org/downloads.html"</dl>



## Como rodar os testes

# Criação do Banco de Dados SiCooperativeDB

<p>Execute o MySQL e inicie o servidor local.</p>
<p>Execute o script Arquitetura_BancoDeDados_SQL.sql para criar o database FinanceDB e suas tabelas com relacionamentos.</p>

# Inserção de Dados no Banco de Dados SiCooperativeDB

<p>Abra o arquivo Insercao_De_Dados.py.</p>
<p>Instale as bibliotecas random, faker e decouple.</p>
<p>Configure a variável db_config com as informações de usuário, senha e host do MySQL na sua instância local.</p>
<p>Configure a variável num_rows para a quantidade de linhas que gostaria de inserir no banco criado (foi utilizado para o exemplo 4 milhões.).</p>
<p>Execute o código em Python para gerar os dados aleátórios dentro do banco de dados.</p>

# Execução do ETL e Exportação do Arquivo para Análise 

<p>Abra o arquivo ETL_Spark_Exportacao_CSV.py.</p>
<p>Instale as bibliotecas Pandas e PySpark.</p>
<p>Altere as configurações das variáveis url, user e password nos dataframes: df_movimentacoes, df_cartoes, df_contas e df_associados.</p>
<p>Execute o código em Python para gerar o CSV com as informações, é possível alterar as colunas e informações que serão expressas no arquivo CSV alterando o SELECT e os JOINS da variável Query.</p>
<p>Obs: Como entusiasta da área de B.I., além da área de engenharia de dados, recomendo que este CSV seja utilizado agora, juntamente com o software de visualização de dados como Power BI ou Tableau, para a criação de insights. Por fim, envie-o aos tomadores de decisão.</p>


<p>Certifique-se de instalar todas os pré-requisitos e bibliotecas, além de configurar corretamente as propriedades do banco de dados.

## Desenvolvedor :octocat:
Guilherme Moraes

