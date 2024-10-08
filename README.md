# Cotacao de Moedas: PROJETO END-TO-END COM PYTHON

Criação de um software para extrair a cotação de moedas utlizando a API do Awesomeapi e análise exploratória de dados (EDA) com pandas no Jupyter Notebook.

## TECNOLOGIAS USADAS:
- Pycharm 2023.3.2
- Python 3.9
  - customtkinter==5.2.2
  - requests==2.31.0
  - os==3.9
  - pandas==2.1.4
  - tinydb==4.8.0
  - pillow==10.2.0
  - Babel==2.14.0
  - pyinstaller==6.0.0
 
## BIBLIOTECAS INSTALADAS
```bash
pip install customtkinter
pip install requests
pip install pandas
pip install tinydb
pip install pyinstaller==6.0.0
pip install pillow
pip install Babel
```
## DESENVOLVIMENTO
- No PyCharm é criado o ambiente virtual venv;
- Com o customtkinter é criado o visual do software, um combobox com as moedas que podem ser escolhidas (USD, EUR e BTC) e um botão de salvar cotação;
- Ao clicar no botão aparecerá uma mensagem de dados salvos, caso algum erro na solicitação aconteça aparecerá uma mensagem avisando sobre o erro;
- A consulta é feita através da API Awesomeapi que é atualizado a cada 30 segundos com a biblioteca requests fazendo a requisição;
- Os dados são salvos em um arquivo json com o auxilio do Tinydb que é um banco de dados prático e de fácil manipulação.

## TRANSFORMANDO EM UM EXECUTÁVEL
- No terminal deverá ser digitado o seguinte comando:
```bash
pyinstaller --onefile --windowed --icon=icone.ico main.py
```
- Será criado um único arquivo, sem janela de comando com um ícone personalizado.
## ARTIGO
[PROJETO END-TO-END COM PYTHON](https://www.linkedin.com/pulse/projeto-end-to-end-com-python-yara-de-oliveira-rufino-mngaf/?trackingId=VB57nJKLRR2uJ9E1%2FSf6Jg%3D%3D)
## REFERÊNCIAS
[Janelas Bonitas no Python - Sistema de Login com CustomTkinter](https://www.youtube.com/watch?v=rQLO1m8oia4) <p>
[Criar Janelas Para seu Código com PySimpleGUI](https://www.youtube.com/watch?v=Ol3n_BR4v70)

## DOCUMENTAÇÃO
[Tinydb](https://tinydb.readthedocs.io/en/latest/) | [Pandas](https://pandas.pydata.org/docs/) | [Customtkinter](https://customtkinter.tomschimansky.com/documentation/) | [PyInstaller](https://pyinstaller.org/en/stable/) | [Requests](https://requests.readthedocs.io/en/latest/) | [Babel](https://babel.pocoo.org/en/latest/) | [Awesomeapi](https://docs.awesomeapi.com.br/api-de-moedas)
