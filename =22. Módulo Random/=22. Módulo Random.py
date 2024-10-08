import random 

# 1 - Seleciona valor aleatorio de uma lista
list1 = [7, 6, 4, 3, 2, 1]
print(random.choice(list1))
print()

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)
print()

# 3 - Seleciona caractere aleatório de uma string
name = 'Curso Python'
r2 = random.choice(name)
print(r2)
print()

# 4 - Seleciona mais de um valor aleatório
# Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 4))
print()

s = 'Olá mundo!'
print(random.sample(s, 2))
