""" 
    # Módulo de Strings
    
    -> Escreva um módulo em python para tratar alguma strings e que possua as seguintes funcionalidades;
    
    1. Inverter um strings ded trás para frente
    2. Retornar apenas letras com índice par
    3. Retornar apenas letras com índice impar
"""

def invertida(palavra):
    inverso = palavra[::-1]
    return inverso

def caracter_par(string):
    return string[0::2] # 0, 2, 4, 6, 8

def impar_caracter(string):
    return string[1::2] # 1, 3, 5, 7, 9