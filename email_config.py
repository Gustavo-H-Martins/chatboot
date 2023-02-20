import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from accesskey import acesso
def retorno_email (email_contato:str = 'gustavogalo22@hotmail.com', nome:str = '', telefone:str= ''):
    # informações do remetente
    alias_email = "Gustavo Lopes - LM Tech <gustavojoana10@gmail.com>"
    remetente_email = 'gustavojoana10@gmail.com'
    remetente_senha = acesso()

    # informações do destinatário
    destinatario_email = email_contato
    nome = nome
    telefone = telefone
    # corpo do email
    corpo = f"""Olá {nome}, espero que esteja bem!
    {os.linesep}Recebi seu contato através do meu autochat, 
    {os.linesep}espero que tenha tido uma boa experiência!
    {os.linesep}o motivo do meu contato é para além de verificar sua experiência, buscar entender,
    {os.linesep}se eu poderia ser útil de alguma forma, de todo modo me coloco à inteira disposição.
    {os.linesep}
    {os.linesep}O telefone {telefone} é válido para contato?
    {os.linesep}
    {os.linesep}Encarecidamente:
    {os.linesep} Gustavo Henrique Lopes - Engenheiro de Dados
    contato: 31 - 9 82273761
     https://github.com/Gustavo-H-Martins """

    # criação do objeto MIMEText
    mensagem = MIMEText(corpo)

    # criação do objeto MIMEMultipart e adição do objeto MIMEText como parte do corpo
    email = MIMEMultipart()
    email['From'] = alias_email
    email.attach(mensagem)

    # definição do assunto do email
    email['Subject'] = 'Retorno de sua visita ao AutoChat Gustavo Lopes'

    # criação do objeto SMTP e login com as informações do remetente
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(remetente_email, remetente_senha)

    # envio do email
    smtp.sendmail(remetente_email, destinatario_email, email.as_string())

    # encerramento da conexão com o servidor SMTP
    smtp.quit()