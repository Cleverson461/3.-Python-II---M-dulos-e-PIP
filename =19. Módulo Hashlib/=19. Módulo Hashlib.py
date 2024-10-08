import hashlib 

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Algoritmos disponiveis de acordo com o SO
print(hashlib.algorithms_guaranteed)
print(30 * '=')
print()


# 3 - Utilizando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
print()

message = 'A melhor forma de prever o futuro é criá-lo'.encode()
algorithm.update(message)
print(algorithm.hexdigest())
print()

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest)