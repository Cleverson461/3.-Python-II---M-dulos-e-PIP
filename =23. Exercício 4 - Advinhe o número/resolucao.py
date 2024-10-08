import random

done = False

while not done:
    print('O que voce deseja fazer? ')
    print('1. Adivinhar o numero: ')
    print('2. Sair! ')
    
    choice = input('> ')
    
    if choice == '1':
        print('===== Advinhe um número de 1 a 10 =====')
        number = int(input('Digite um numero de 1 a 10: '))
        result = random.randint(1, 10)
        
        if number == result:
            print('Parabens. voce acertou!')
        else:
            print(f'Tente novemente. O numero sorteado foi {result}')
    elif choice == '2':
        done = True
    else:
        print('Opção invalida. Escolha uma opcao entre 1 e 2')