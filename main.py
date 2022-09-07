import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC82e9a64f2d7cc28e111149f89e95263c"
# Your Auth Token from twilio.com/console
auth_token  = "e4d2c6c2fa1281ce6005cb5e44992ede"
client = Client(account_sid, auth_token)

diretorio = 'C:\\Users\\danie\\OneDrive\\Área de Trabalho\\Cursos\Python - Teste SMS\\Arquivos\\'
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:    
    df_tabela_vendas = pd.read_excel(diretorio + f'{mes}.xlsx')    
    if (df_tabela_vendas['Vendas'] > 55000).any():
        vendedor = df_tabela_vendas.loc[df_tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = df_tabela_vendas.loc[df_tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        #print(f'No mês de {mes} o {vendedor} vendeu {vendas}')
        message = client.messages.create(
            to="+5511987246275", 
            from_="+15305615453",
            body=f'No mês de {mes} o {vendedor} vendeu {vendas}')
        print(message.sid)
