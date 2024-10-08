import math 

# 1 - Acessar o número Pi
print(math.pi)
print(f'{math.pi:.2f}')

print()
print(30 * '-')
print()
# 2 - Acessar o número de Euler
print(math.e)
print(f'{math.e:.2f}')

print()
print(30 * '-')
print()
# 3 - Arredondando números para cima e para baixo
num1 = 10.4
print(math.ceil(num1))
print(math.floor(num1))

print()
print(30 * '-')
print()

# 4 - Fatorial de um número
num2 = int(input('Digite um número para o fatorial: '))
print(math.factorial(num2))

print()
print(30 * '-')
print()

# 5 - Potência de números
print(math.pow(5, 5))

print()
print(30 * '-')
print()

# 6 - Raiz quadrada de um número
print(math.sqrt(169))

print()
print(30 * '-')
print()

# 7 - MDC
mdc = math.gcd(20, 70) # 25 / 100 = 1 / 4
print(mdc)

print()
print(30 * '-')
print()

# 8 - Logaritmo
print(math.log(10))