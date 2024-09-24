texto = str(input("Digite o seu texto: "))

def sub(text):
    produto = []
    
    for carac in text:
        if carac in "aeiouAEIOU":
            produto.append("*")
        else:
            produto.append(carac)
    return ''.join(produto)
print(sub(texto))

