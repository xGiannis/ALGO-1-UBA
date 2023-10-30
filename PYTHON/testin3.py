from practica3 import *
from queue import LifoQueue as Pila
import random



p=Pila()
p.put(1)
p.put(2)
p.put(5)
p.put(4)


sampleText="textoEjemplo.txt"
textomodificable="textoejemplo2.txt"


#buscarElMaximo(pilaOrd)
#buscarElMaximo(pilaDesord)

#agruparPorLongitud("textoEjemplo.txt")


#contarLineas("textoEjemplo.txt")
#reverso(sampleText)

#agregarFrase(textomodificable,"Las abuelas de plaza de mayo\nExijen libertad!")

#agregarFrasePrincipio(textomodificable,"In the beggining...\n")


#promedioEstudiante2("825/22")


#PILAS¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡
print("")
print("")
print("")

pilaOrd=pilaOrdHasta(10)
pilaDesord=pilaOrdHastaDesord(10,0,20)
#cantidadElementos(pilaDesord)

#buscarElMaximo(pilaDesord)

"""
estaBienBalanceada("2 + 2")
print("")
estaBienBalanceada("3*5+(22)/4)")
estaBienBalanceada("((2x33)/32)")
"""

#evaluar_postfix("2 2 + 10 * 2 -")


#COLA¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡

colaDesord=colaAlAzar(10,0,20)

#cantidadElementos(colaDesord)
#print("")
#maximoCola(colaDesord)


def hacerCarton():
    carton=[]
    for i in range(15):
        num=random.randint(0,99)
        while num in carton:
            num=random.randint(0,99)
        carton.append(num)
    print(carton)
    return carton


carton=hacerCarton()
bolillero=secuenciaBingo()

jugarCartonBingo(carton,bolillero)

