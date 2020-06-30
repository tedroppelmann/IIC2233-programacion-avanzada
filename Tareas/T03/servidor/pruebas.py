
from itertools import cycle

lista = [1,2,3,4,5]
invertir = lista[::-1]
ciclo = cycle(invertir)

print(invertir)

turno = next(ciclo)


while 3 != turno:
    turno = next(ciclo)

print(turno)



