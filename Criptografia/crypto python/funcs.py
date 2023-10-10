from cryptography.fernet import Fernet

def gerar_chave():
    key = Fernet.generate_key()

    with open('keys.rans', 'wb') as filekey:
        filekey.write(key)

    return key

def ler_chave(caminho):
    with open(caminho, 'rb') as filekey:
        key = filekey.read()
    return key

def abrir_arquivo(caminho):
    with open(caminho, 'rb') as arquivo:
        conteudo = arquivo.read()
        return conteudo
    
def gravar_arquivo(caminho, conteudo):
    with open(caminho, 'wb') as arquivo:
        arquivo.write(conteudo)
        print("arquivo gravado")