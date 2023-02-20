# Python - Chatboot para responder questões do meu portifólio de skils
import os
from datetime import datetime
from email_config import retorno_email

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Este é o link do meu GitHub:\033[1m https://github.com/Gustavo-H-Martins \033[0m{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} Muito simples, basta seguir o link:\033[1m https://www.linkedin.com/in/gustavo-henrique-lopes-martins-361789192/ \033[0m{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Você me encontra no e-mail:\033[1m gustavojoana10@gmail.com\033[0m estarei disponível!{os.linesep}')    
    elif resposta == '4': 
        print(f"""{nome}, pode me fornecer seu email, ou um contato? """)
        email = input("Seu melhor e-mail para contato: ")
        os.linesep
        telefone = input("Telefone para contato: ")
        if len(email) < 10:
            email = 'gustavogalo22@hotmail.com'
        retorno_email(email_contato= email, nome= nome, telefone= telefone)

    else:
        print("""
        No momento estou em desenvolvimento, 
        portanto ainda não tenho mais opções de respostas.
        """)    


def start():
    # Apresentar o chatbot
    # Definir horário e printar saudação inicial.

    agora = datetime.now()
    if agora.hour < 12:
        print('Olá, bom dia!')
    elif agora.hour >= 12 & agora.hour < 18:
        print('Olá, boa Tarde!')
    elif agora.hour > 18:
        print('Olá, boa noite!')
    
    print(f'Bem vindo autochat - \033[1mGustavo Martins LM Tech \033[0m{os.linesep}')

    # Pedir o nome
    nome = input(f'Por gentileza, digite seu nome: ')
    # Oferecer um menu de opções
    contador = 0
    print("O que gostaria de saber hoje? ")
    while True:
        
        if contador == 0:
            
            resposta = input(
                f"""
                {os.linesep}\033[1m[1]\033[0m - Como acesso o seu Github? 
                {os.linesep}\033[1m[2]\033[0m - Como acesso o seu LinkedIn? 
                {os.linesep}\033[1m[3]\033[0m - Como entro em contato com você?
                {os.linesep}\033[1m[4]\033[0m - Quero que entre em contato para maiores informações.

        - """)
            
            # Processar a resposta enviada
            processar_resposta(resposta, nome)
        else :
            continuar = input(f"""Gostaria de continuar esta conversa por aqui? 
            {os.linesep}\033[1m[1]\033[0m - Sim
            {os.linesep}\033[1m[2]\033[0m - Não 
            {os.linesep} """)
            if continuar == '1':
                contador = 0
            else:
                print(f"""
                {os.linesep}
                {os.linesep}
                {os.linesep}
                {os.linesep} Obrigado pelo seu momento! 
                {os.linesep} Para mais informações me mande um e-mail : gustavojoana10@gmail.com
                {os.linesep} Será um prazer te responder! 
                {os.linesep}""")

        contador += 1 


if __name__ =='__main__':
    start()