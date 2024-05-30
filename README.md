# Cotacao_Moedas

Este é um software para extrair a cotação de moedas utlizando a API do Awesomeapi.

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


## REFERÊNCIAS
[Janelas Bonitas no Python - Sistema de Login com CustomTkinter](https://www.youtube.com/watch?v=rQLO1m8oia4)

[Criar Janelas Para seu Código com PySimpleGUI](https://www.youtube.com/watch?v=Ol3n_BR4v70)

## DOCUMENTAÇÃO
[Tinydb](https://tinydb.readthedocs.io/en/latest/) | [Pandas](https://pandas.pydata.org/docs/) | [Customtkinter](https://customtkinter.tomschimansky.com/documentation/) | [PyInstaller](https://pyinstaller.org/en/stable/) | [Requests](https://requests.readthedocs.io/en/latest/) | [Awesomeapi](https://docs.awesomeapi.com.br/api-de-moedas)
