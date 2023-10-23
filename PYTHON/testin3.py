from practica3 import *
from queue import LifoQueue as Pila
import random

def pilaOrdHasta(hasta:int):
    pila=Pila()
    for i in range(0,hasta,1):
        pila.put(i)
    return pila

def pilaOrdHastaDesord(hasta:int):
    pila=Pila()
    for i in range(hasta):
        num=random.randrange(0,hasta)

        pila.put(num)
    return pila

p=Pila()
p.put(1)
p.put(2)
p.put(5)
p.put(4)


pilaOrd=pilaOrdHasta(10)
pilaDesord=pilaOrdHastaDesord(10)

buscarElMaximo(pilaOrd)
buscarElMaximo(pilaDesord)

agruparPorLongitud("textoEjemplo.txt")

