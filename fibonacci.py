n = int(input("Indique um número para a sequência: "))
memo = {}

def fibonacci(num):
    if num in memo:
        return memo[num]  # Retorna o resultado armazenado
    if num == 0:
        return 0  # Caso base
    elif num == 1:
        return 1  # Caso base
    else:
        # Calcula e armazena o resultado
        memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return memo[num]

# Chama a função e imprime o resultado
print(fibonacci(n))
