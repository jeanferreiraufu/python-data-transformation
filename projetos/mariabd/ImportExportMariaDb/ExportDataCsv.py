import pandas as pd
from sqlalchemy import create_engine

# Configurações do banco de dados (exemplo)
DB_HOST = 'example_host'
DB_PORT = 3306
DB_USER = 'example_user'
DB_PASSWORD = 'example_password'
DB_NAME = 'example_db'
TABLE_NAME = 'example_table'

# String de conexão com o banco de dados
database_connection = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Consulta SQL de exemplo
sql_query = """
SELECT 
    a.col1 AS codigo_lancamento,
    a.col2 AS codigo_lancamento_lote,
    LPAD(a.col3, 7, '0') AS ic_reduzido,
    a.col4 AS ic,
    YEAR(a.col5) AS exercicio,
    a.col6 AS data_emissao,
    'REAL' AS moeda,
    a.col7 AS controle,
    a.col8 AS nome_contribuinte,
    a.col9 AS cpf_cnpj_contribuinte,
    a.col10 AS nome_contribuinte_2,
    a.col11 AS cpf_cnpj_contribuinte_2,
    CAST(a.col12 AS DECIMAL(14, 2)) AS imovel_area_terreno,
    CAST(a.col13 AS DECIMAL(14, 2)) AS imovel_valor_m2_terreno,
    CAST(a.col14 AS DECIMAL(14, 2)) AS imovel_testada,
    CAST(a.col15 AS DECIMAL(14, 2)) AS imovel_area_construida,
    CAST(fat_table_pred.col1 AS DECIMAL(14, 2)) AS imovel_valor_m2_construcao,
    CAST(fat_table_terr.col1 AS DECIMAL(12, 4)) AS imovel_fracao_ideal,
    CAST(a.col16 AS DECIMAL(14, 2)) AS imovel_valor_venal_territorial,
    CAST(fat_table_pisc.col1 AS DECIMAL(14, 2)) AS imovel_area_piscina,
    CAST(fat_table_pisc.col2 AS DECIMAL(14, 2)) AS imovel_valor_m2_piscina,
    a.col17 AS imovel_com_sub_unidades,
    IF(a.col18 = 'S', 'Predial', IF(a.considera_area_edificada = 'N', 'Territorial', '')) AS imovel_tipo_edificacao,
    CAST(a.col19 AS DECIMAL(14, 2)) AS imovel_valor_venal_predial,
    CAST(a.col20 AS DECIMAL(14, 2)) AS imovel_valor_venal_imovel,
    CAST(a.col21 AS DECIMAL(5, 4)) AS imovel_aliquota,
    CAST(a.col22 AS DECIMAL(14, 2)) AS imovel_valor_itu,
    CAST(a.col23 AS DECIMAL(14, 2)) AS imovel_valor_ipu,
    CAST(a.col24 AS DECIMAL(14, 2)) AS imovel_valor_iptu,
    CAST(a.col25 AS DECIMAL(14, 2)) AS imovel_valor_tsu,
    a.col26 AS imovel_quadra,
    a.col27 AS imovel_lote,
    CAST(a.col28 AS DECIMAL(14, 2)) AS imovel_valor_total_anual,
    (SELECT MAX(fat_table_parcelas.parcela) FROM fat_table_parcelas WHERE fat_table_parcelas.id_principal = a.id_principal AND fat_table_parcelas.parcela_ultima NOT IN (0)) AS imovel_quantidade_parcelas,
    CAST((SELECT valorprincipal FROM fat_table_parcelas WHERE fat_table_parcelas.id_principal = a.id_principal AND fat_table_parcelas.parcela_ultima NOT IN (0) LIMIT 1) AS DECIMAL(14, 2)) AS imovel_valor_parcela
FROM
    lancamento a
    INNER JOIN lancamento_carne ilc ON ilc.imovel_inscricao = a.imovel_inscricao 
    LEFT JOIN lancamento_auxiliar j ON a.codigo = j.id_lancamento AND j.status = 'A'
    LEFT JOIN fat_table_parcelas d ON a.id_principal = d.id_principal AND a.id_principal <> 0 AND a.id_principal IS NOT NULL 
    LEFT JOIN banco_arrc_convenio g ON g.codigo = d.id_banco_arrc_convenio
    LEFT JOIN lancamento_reducao AS lanc_reducao ON a.codigo = lanc_reducao.cod_lancamento AND lanc_reducao.status = 'A'
    LEFT JOIN imovel_reduc AS imovel_reduc ON lanc_reducao.cod_imovel_reducao = imovel_reduc.codigo AND imovel_reduc.status = 'A'
WHERE 
    ilc.exercicio = 2024 
    AND ilc.arquivo = '2024-PARCELA-10-LOTE-1' 
    AND a.id_principal > 0
    AND a.id_principal IS NOT NULL
    AND a.status = 'A'
    AND a.id_principal NOT IN (SELECT id_principal FROM lancamento_restricao WHERE status = 'A' AND id_principal = a.id_principal)
    AND YEAR(a.data_exercicio) = ilc.exercicio
GROUP BY 
    a.codigo, d.id_principal, d.parcela, d.parcela_ultima 
ORDER BY 
    a.correspondencia_cidade, a.correspondencia_bairro, a.correspondencia_logradouro, a.id_principal, d.parcela_ultima, d.parcela;
"""

# Função para executar a consulta e gerar um arquivo CSV
def execute_query_and_generate_csv(database_connection, sql_query, csv_file_path, csv_config):
    # Crie a conexão com o banco de dados
    engine = create_engine(database_connection)

    # Execute a consulta e obtenha os dados em um DataFrame
    df = pd.read_sql_query(sql_query, engine)

    # Salve o DataFrame como um arquivo CSV
    df.to_csv(csv_file_path, **csv_config)

    print(f'Arquivo CSV gerado em: {csv_file_path}')

# Caminho do arquivo CSV de exemplo
csv_file_path = './example_output.csv'

# Configurações do arquivo CSV
csv_config = {
    'sep': ';',
    'encoding': 'windows-1252',
    'index': False,
    'quoting': 1,
    'quotechar': '"',
    'doublequote': True
}

# Exemplo de uso
execute_query_and_generate_csv(database_connection, sql_query, csv_file_path, csv_config)