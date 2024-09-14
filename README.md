# python-data-transformation
Repositório para armazenamento de Scripts Python para Transformação de Dados

# Resumo do Código

Os códigos em Python realizam a importação e exporação de dados de arquivos CSVs para tabelas em um banco de dados MariaDB. Aqui está um resumo das principais funcionalidades:

Importação de Módulos: Importa os módulos csv e pymysql.
Configurações do Banco de Dados: Define as configurações de conexão ao banco de dados, como host, porta, usuário, senha, nome do banco de dados e nome da tabela.
Função conectar_banco: Conecta ao banco de dados usando as configurações definidas.
Função registro_existe: Verifica se um registro já existe na tabela com base em dois valores de coluna.
Função inserir_registro: Insere um novo registro na tabela se ele não existir.
Função processar_arquivo_csv:
Abre o arquivo CSV responsaveis.csv.
Lê o arquivo linha por linha, ignorando o cabeçalho.
Para cada linha, verifica se o registro já existe no banco de dados.
Se o registro não existir, insere um novo registro.
Fecha a conexão com o banco de dados.
Execução Principal: Chama a função processar_arquivo_csv para iniciar o processamento do arquivo CSV.


- **Importação de Módulos Python**:
  - `csv`
  - `pymysql`

