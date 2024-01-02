# Importando as bibliotecas.
import random
from faker import Faker
import mysql.connector
from mysql.connector import errorcode
from decouple import config 

# Configurações para conectar no banco de dados, deve-se usar as configurações do seu banco de dados instalado na sua instância local.
db_config = {
    'user': config('user'),
    'password': config('senha'),
    'host': config('host') ,
    'database': 'FinanceDB',
}

# Bloco para realizar a conexão ao banco de dados no MySQL criado. 
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro: Usuário ou senha incorretos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Erro: Banco de dados não existe")
    else:
        print(err)
    exit(1)

# Linha de código para chamar a função Faker para criarmos dados ficticios para inserção dentro do banco de dados.
fake = Faker() 

# Função num_rows para selecionar o número de dados a serem inseridos no banco.
num_rows = 4000000

for _ in range(num_rows):

    # Tabela associados
    nome = fake.first_name()
    sobrenome = fake.last_name()
    idade = random.randint(18, 100)
    email = fake.email()
    cursor.execute("INSERT INTO associados (nome, sobrenome, idade, email) VALUES (%s, %s, %s, %s)",
                   (nome, sobrenome, idade, email))
    associado_id = cursor.lastrowid

    # Tabela contas
    tipos_conta = ['Conta Corrente', 'Conta Poupança']
    tipo_conta = random.choice(tipos_conta)
    data_criacao = fake.date_time_between(start_date="-1y", end_date="now")
    cursor.execute("INSERT INTO contas (tipo_conta, data_criacao, id_associado) VALUES (%s, %s, %s)",
                   (tipo_conta, data_criacao, associado_id))
    conta_id = cursor.lastrowid

    # Tabela cartoes
    num_cartao = fake.credit_card_number(card_type="mastercard")
    nom_impresso = fake.name()
    cursor.execute("INSERT INTO cartoes (num_cartao, nom_impresso, id_conta, id_associado) VALUES (%s, %s, %s, %s)",
                   (num_cartao, nom_impresso, conta_id, associado_id))
    cartao_id = cursor.lastrowid

    # Descrições padronizadas para seleção na tabela Movimentações, isso foi feito para evitar a limitação da biblioteca, faker, para evitar que a coluna des_transacao, gere coisas sem sentido.
descricoes_padronizadas_movimentacoes = [
    "Transação feita para pagamento de contas",
    "Compra feita em loja de roupas",
    "Saque realizado no caixa eletrônico",
    "Transferência entre contas",
    "Pagamento de fatura do cartão de crédito",
    "Recebimento de salário",
    "Investimento em ações",
    "Compra de mantimentos no supermercado",
    "Pagamento de mensalidade",
    "Transferência para conta de investimentos",
    "Compra de eletrônicos",
    "Pagamento de aluguel",
    "Recebimento de transferência",
    "Investimento em fundo de renda fixa",
    "Compra de passagens aéreas"
]

    # Tabela movimentacoes
    vlr_transacao = round(random.uniform(1, 1000), 2)
    data_movimento = fake.date_time_between(start_date="-1y", end_date="now")
    des_transacao = random.choice(descricoes_padronizadas_movimentacoes)

    cursor.execute("INSERT INTO movimentacoes (vlr_transacao, data_movimento, des_transacao, id_cartao) VALUES (%s, %s, %s, %s)",
                   (vlr_transacao, data_movimento, des_transacao, cartao_id))

# Commit e fecha a conexão com o banco de dados.
conn.commit()
cursor.close()
conn.close()

print(f"Inseridos {num_rows} registros em todas as tabelas.") # Print para retornar quantos registros foram inseridos no banco.
