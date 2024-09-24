n = int(input("Indique o número: "))
def num_perfect(n):
    sum_divisores = 0
    for i in range(1,n):
        if n % i == 0:
            sum_divisores +=i
    if sum_divisores == n:
        print("Número perfeito!")
    else:
        print("Não é um número perfeito!")
num_perfect(n)