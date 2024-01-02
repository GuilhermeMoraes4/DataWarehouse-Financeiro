# Importando as bibliotecas.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pandas as pd
from decouple import config 
import os

# Váriavel criada para espeficiar a pasta que será salva o arquivo csv para análise.
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# Váriavel criada para especificar o caminho do arquivo csv que será salvo o dataframe agregado.
output_csv_path = os.path.join(output_folder, "df_agregado.csv")

# Configuração do Pyspark para o projeto do DataLake
spark = SparkSession.builder \
    .appName("ETL usando PySpark") \
    .getOrCreate()

# Conexão do código ao banco de dados "FinanceDB" no MySql e leitura dos dados das quatro tabelas já criadas.
df_movimentacoes = spark.read.format("jdbc").option("url", config(url)).option("driver", "com.mysql.cj.jdbc.Driver").option("dbtable", "movimentacoes").option(config(user)).option(config(senha)).load()
df_cartoes = spark.read.format("jdbc").option("url", config(url)).option("driver", "com.mysql.cj.jdbc.Driver").option("dbtable", "cartoes").option(config(user)).option(config(senha)).load()
df_contas = spark.read.format("jdbc").option("url", config(url)).option("driver", "com.mysql.cj.jdbc.Driver").option("dbtable", "contas").option(config(user)).option(config(senha)).load()
df_associados = spark.read.format("jdbc").option("url", config(url)).option("driver", "com.mysql.cj.jdbc.Driver").option("dbtable", "associados").option(config(user)).option(config(senha)).load()

# Registro das tabelas do banco de dados como "temp views" ou "vistas temporárias".
df_movimentacoes.createOrReplaceTempView("movimentacoes")
df_cartoes.createOrReplaceTempView("cartoes")
df_contas.createOrReplaceTempView("contas")
df_associados.createOrReplaceTempView("associados")

# Etapa feita para criar as joins para unir os dados usando Spark SQL
query = """
    SELECT
        ac.nome AS nome_associado,
        ac.sobrenome AS sobrenome_associado,
        ac.idade AS idade_associado,
        m.vlr_transacao,
        m.des_transacao,
        m.data_movimento,
        c.num_cartao,
        c.nom_impresso,
        co.data_criacao,
        co.tipo_conta
    FROM movimentacoes m
    JOIN cartoes c ON m.id_cartao = c.id
    JOIN contas co ON c.id_conta = co.id
    JOIN associados ac ON c.id_associado = ac.id
"""

df_agregado = spark.sql(query)

# Função para visualizar o dataframe "df_agregado" criado acima. 
df_agregado.show()

# Transformação de df criado em Spark para pandas.
df_pandas = df_agregado.toPandas()

# Etapa feita para salvar o Dataframe em pandas como arquivo csv no caminho solicitado na váriavel acima.  
df_pandas.to_csv(output_csv_path, index=False)
