""" 
    * Advinhe o Número
     -> Escreva um programa em Python que gera um número aleatótio para que o usuario tente acertar o numero. Algumas sugestoes para o programa:
      
      1 - Utilizar um laço de repeticao para que o programa execute para sair do programa. 
      2 - Utilizar o modulo random para gerar valores aleatorios dentro de um intervalo. Ex: 1  a 10.
      3 - Lê o número que o usuario digitar via input e comparar se é o mesmo que o programa sorteou. 
"""
import random

num_aleatorio = random.randint(1, 10)
# print(num_aleatorio)
done = True

while done:
    usuario = int(input('Digite um numero entre 1 a 10: '))
    if usuario == num_aleatorio:
        print(f'Parabens voce acertou o numero premiado {num_aleatorio}, voce digitou {usuario}')
        done = False
    else:
        print('Tente Novamente!')