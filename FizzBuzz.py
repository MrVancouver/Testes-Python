def fizzbuzz():
    n1 = int(input("Indique o primeiro número: "))
    n2 = int(input("Indique o segundo número: "))
    n2 = n2+1
    for i in range(n1, n2):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Chama a função para executar o FizzBuzz
fizzbuzz()
