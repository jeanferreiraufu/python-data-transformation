# python-data-transformation
Repositório para armazenamento de Scripts Python para Transformação de Dados

# Resumo do Código

- **Importação de Módulos**:
  - `csv`
  - `pymysql`

- **Configurações do Banco de Dados**:
  - `DB_HOST`
  - `DB_PORT`
  - `DB_USER`
  - `DB_PASSWORD`
  - `DB_NAME`
  - `TABLE_NAME`

- **Funções**:
  - `conectar_banco()`: Conecta ao banco de dados.
  - `registro_existe(conn, valor_coluna1, valor_coluna2)`: Verifica se um registro existe.
  - `inserir_registro(conn, valor_coluna1, valor_coluna2)`: Insere um novo registro.
  - `atualizar_arquivo_por_registro(param_valor)`: Função para atualizar um arquivo por registro
  - `execute_query_and_generate_csv(database_connection, sql_query, csv_file_path, csv_config)`: Função para executar a consulta e gerar um arquivo CSV

- **Função Principal**:
  - `processar_arquivo_csv()`: Processa o arquivo CSV e insere registros no banco de dados.

- **Execução**:
  - Chama `processar_arquivo_csv()` para iniciar o processamento.