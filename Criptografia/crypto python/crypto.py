from cryptography.fernet import Fernet
from funcs import gerar_chave, abrir_arquivo, gravar_arquivo


chave = gerar_chave()
fernet = Fernet(chave)

arquivo = abrir_arquivo('meg.png')

criptografado = fernet.encrypt(arquivo)

gravar_arquivo('teste.rans', criptografado)
