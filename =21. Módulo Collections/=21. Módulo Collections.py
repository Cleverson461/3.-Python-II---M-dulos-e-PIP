from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista
fruits = ["Maça", "Banana", "Uva", "Pêra", "Uva", "Maça", "Laranja", "Banana", "Abacaxi", "Tangerina", "Banana",  "Uva", "Pêra", "Banana"] 

print(fruits)
print(Counter(fruits))
print()

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa23", 90.50, 8.5)
g2 = game("Resident Evil 4 Remake", 300, 10.0)

print(g1)
print(g2)
print()

# 3 - Ordenando dicionarios
studants = {"Pedro":23, "Ana":22, "Ronaldo":26, "Janaína":25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)
print()

# 4 - Utilizando fila ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)

deq.append(90)
print(deq)
deq.popleft()
deq.pop()
print(deq)