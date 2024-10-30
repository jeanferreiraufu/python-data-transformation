# Python Data Transformation

Este projeto é destinado à transformação de dados utilizando Python.

- Foco inicial em ETL (Python e MariaDB)
- Visao Computacional 
  - Contribuidor: [Henrique Moreira Amorin](https://henrique-moreira.github.io/)
  - Biliotecas: Keras, OpenCV, kaggle, scikit-learn, scikit-image, matplotlib, Numpy, Pandas.
  - Segmentação de Imagens: 
    - Parâmetros de limiarização adaptativa em diferentes espaços de cores (HSV, YUV, etc.)
    - Avaliação dos Descritores de Imagem: 
      - GLCM - Matriz de coocorrência de níveis de cinza
      - Haralick - característica específica da textura da imagem
    - Avaliação do desempenho dos Classificadores (Random Forest, SVM)
    - Avaliação de Performance: Jaccard, Pearson

## Estrutura do Projeto

- **src/**: Contém o código-fonte do projeto.
- **data/**: Diretório onde os datasets são armazenados.
- **notebooks/**: Jupyter notebooks para análise e experimentação.
- **tests/**: Testes unitários para o código-fonte.

## Requisitos

- Python 3.x
- Bibliotecas listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
    ```powershell
    git clone https://github.com/seu-usuario/python-data-transformation.git
    ```
2. Navegue até o diretório do projeto:
    ```powershell
    cd python-data-transformation
    ```
3. Crie um ambiente virtual e ative-o:
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate
    ```
4. Instale as dependências:
    ```powershell
    pip install -r requirements.txt
    ```

## Uso

Descreva aqui como utilizar o projeto, incluindo exemplos de comandos e scripts.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.