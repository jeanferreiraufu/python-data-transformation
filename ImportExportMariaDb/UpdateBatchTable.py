# Dependências: sqlalchemy, pandas

from sqlalchemy import create_engine, text
import pandas as pd

# Configurações do banco de dados

DB_HOST = '99.99.99.99'
DB_PORT = 5000
DB_USER = 'dbuser'
DB_PASSWORD = 'dbpassword'
DB_NAME = 'dbname'
TABLE_NAME = 'tabelaname'

stringConexao = "'mysql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + ":" + str(DB_PORT) + "/" + DB_NAME + "';"

# Função para atualizar um arquivo por registro
def atualizar_arquivo_por_registro(param_valor):
    # Substitua com as informações da sua conexão e código SQL
    engine = create_engine(stringConexao)

    # Sua consulta SQL
    consulta_sql = """
        SELECT a.col1, a.col2, b.col3, b.col4
        FROM tabela1 a
        INNER JOIN tabela2 b ON b.col1 = a.col1 
            AND b.col4 = 2024 
        WHERE a.col3 > 0 
        LIMIT 15000;
    """

    # Execute a consulta e obtenha os dados em um DataFrame
    df = pd.read_sql_query(text(consulta_sql), engine)

    # Verifique se há resultados
    if not df.empty:
        # Construa a query de atualização
        query_atualizacao = "UPDATE " + TABLE_NAME + " SET gerado = 0, arquivo = :parametro_valor WHERE col2 = 2024 and col1 = :param_col1"

        # Execute a query de atualização para cada registro
        with engine.connect() as conexao:
            for _, linha in df.iterrows():
                col1 = linha['col1']
                conexao.execute(text(query_atualizacao), parametro_valor=param_valor, param_col1=col1)

        print(f"Arquivo atualizado com sucesso para {len(df)} registros.")
    else:
        print("Nenhum registro encontrado para atualização.")

# Exemplo de uso
parcelas = 10
lote = "PARCELAS-" + str(parcelas) + "-LOTE"

atualizar_arquivo_por_registro(lote)



