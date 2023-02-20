from cryptography.fernet import Fernet
def acesso():
    # Gera uma chave de criptografia
    key = Fernet.generate_key()

    # Cria um objeto Fernet com a chave gerada
    fernet = Fernet(key)

    # String que será criptografada
    with open('senha.txt', 'r') as senha:
        str_senha = senha.readline()
        senha.close()
    string_original = str_senha

    # Criptografa a string
    string_criptografada = fernet.encrypt(string_original.encode()).decode()

    # Descriptografa a string
    string_descriptografada = fernet.decrypt(string_criptografada.encode()).decode()

    return string_descriptografada

