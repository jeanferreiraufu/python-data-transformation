import csv
import pymysql

# Configurações do banco de dados
DB_HOST = '99.99.99.99'
DB_PORT = 5000
DB_USER = 'dbuser'
DB_PASSWORD = 'dbpassword'
DB_NAME = 'dbname'
TABLE_NAME = 'tabelaname'

# Função para conectar ao banco de dados
def conectar_banco():
    return pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)

# Função para verificar se um registro existe na tabela
def registro_existe(conn, valor_coluna1, valor_coluna2):
    cursor = conn.cursor()
    query = f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE imovel_inscricao = %s AND nuCpf = %s"
    cursor.execute(query, (valor_coluna1, valor_coluna2))
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0

# Função para inserir um registro na tabela
def inserir_registro(conn, valor_coluna1, valor_coluna2):
    cursor = conn.cursor()
    query = f"INSERT INTO {TABLE_NAME} (imovel_inscricao, nuCpf, cdTipoCpf, responsavel, responsavelprincipal) VALUES (%s, %s, 2, 'P', 2)"
    #print(query);
    cursor.execute(query, (valor_coluna1, valor_coluna2))
    conn.commit()
    cursor.close()

# Abrir o arquivo CSV e processar cada linha
def processar_arquivo_csv():
    with open('responsaveis.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv, delimiter=';')
        next(reader)  # Pula o cabeçalho do CSV

        conn = conectar_banco()

        for linha in reader:
            valor_coluna1 = int(linha[0])
            valor_coluna2 = int(linha[1])

            if not registro_existe(conn, valor_coluna1, valor_coluna2):
                inserir_registro(conn, valor_coluna1, valor_coluna2)

        conn.close()

# Chamar a função principal para processar o arquivo CSV
processar_arquivo_csv()