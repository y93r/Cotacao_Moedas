import customtkinter
import requests
import os
import pandas as pd
import tinydb
from babel import numbers

# Função para fazer a requisição na API
def pegar_cotacoes():
    codigo_moeda = lista.get()
    if not codigo_moeda:
        mensagem.configure(text="Por favor, selecione uma moeda.")
        return
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao.raise_for_status()
        requisicao_dic = requisicao.json()
        codigo = requisicao_dic[f'{codigo_moeda}BRL']['code']
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        valor_alto = requisicao_dic[f'{codigo_moeda}BRL']['high']
        valor_baixo = requisicao_dic[f'{codigo_moeda}BRL']['low']
        data = requisicao_dic[f'{codigo_moeda}BRL']['create_date']

        # Recuperar os dados solicitados
        dados = []
        # Adicionar os dados à lista
        dados.append({
            'Data': data,
            'Código': codigo,
            'Cotação': cotacao,
            'Valor Mais Alto': valor_alto,
            'Valor Mais Baixo': valor_baixo
        })

        # Criar um DataFrame com os dados
        df = pd.DataFrame(dados)

        # Nome da pasta a ser criada
        nome_pasta = r'Caminho_a_ser_salvo_\Projeto'

        # Verificar se a pasta não existe e, se não existir, criar
        if not os.path.exists(nome_pasta):
            os.makedirs(nome_pasta)

        # Criar o caminho para o arquivo ser salvo
        caminho_arquivo = r'Caminho_a_ser_salvo_\Projeto\Cotacao.json'

        # Converte o DataFrame para um dicionário
        dados_dict = df.to_dict(orient='index')

        # Cria um banco de dados
        db = tinydb.TinyDB(caminho_arquivo)

        # Cria uma tabela chamada "dados"
        tabela = db.table("dados")

        # Insere o documento no banco de dados
        tabela.insert_multiple(dados_dict.values())

        apagar_dado()
    except requests.exceptions.RequestException as e:
        mensagem.configure(text=f"Erro na requisição: {e}")
    except KeyError:
        mensagem.configure(text="Erro ao acessar os dados da cotação.")
    except Exception as e:
        mensagem.configure(text=f"Ocorreu um erro: {e}")

#Função para apagar a lista e confirmar os dados salvos
def apagar_dado():
    codigo_moeda = lista.get()
    mensagem.configure(text=f'Dados de {codigo_moeda} salvo com sucesso!')
    lista.set("")

# ==== INTERFACE ===
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("300x200")
janela.title("COTAÇÃO DE MOEDAS")
janela.resizable(False, False)# Impede a redimensionamento horizontal e vertical

# Lista de Moedas
lbl0 = customtkinter.CTkLabel(janela, text="MOEDAS")
lbl0.grid(column=0, row=2, padx=10, pady=10, sticky='NSEW')
moedas = ['USD','EUR','BTC']
lista = customtkinter.CTkComboBox(janela,values=moedas, state="readonly")
lista.grid(column=1, row=2, padx=10, pady=10, sticky='NSEW')

# Botão Salvar
botao_salvar = customtkinter.CTkButton(janela,text='Salvar Cotação', command=pegar_cotacoes)
botao_salvar.grid(column=1, row=3, padx=10, pady=10, sticky='NSEW')

# Confirmação de dados salvos
mensagem = customtkinter.CTkLabel(janela, text="")
mensagem.grid(column=0, row=4, columnspan=2, padx=10, pady=10, sticky='NSEW')

janela.mainloop()
