import re 

text = str(input("Indique o texto: "))
def palindromo(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z0-9]','',texto)
    return texto == texto[::-1]
if palindromo(text):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")