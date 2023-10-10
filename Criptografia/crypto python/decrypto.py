from cryptography.fernet import Fernet
from funcs import ler_chave, abrir_arquivo, gravar_arquivo

fernet = Fernet(ler_chave('keys.rans'))
criptografado = abrir_arquivo('teste.rans')
descriptografado = fernet.decrypt(criptografado)

gravar_arquivo('teste.png', descriptografado)