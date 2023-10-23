from practica2 import *

listaVacia=[]
lista=[1,2,3,4,5,6]
listaNoOrd=[2,1,5,92,3]
listaRepetida=[2,3,6,1,3,5,2]
listaPar=[2,4,6,8]

listanumeros=[1,2,3,4]
listaINT=[123,14,3,9,1]

listaPalabras=["hola","buenas","SCHIARETTI"]


#PARTE1
#EJERCICIO1
pertenece(lista,4)
pertenece(lista,8)
pertenece(listaNoOrd,5)
pertenece(listaRepetida,3)
pertenece(listaVacia,5)
print("")

pertenece2(lista,6)
pertenece2(lista,8)
pertenece2(listaNoOrd,5)
pertenece2(listaRepetida,3)
print("")

#EJERCICIO3
sumaTotal(lista)
sumaTotal(lista)
sumaTotal(listaNoOrd)
sumaTotal(listaRepetida)
print("")

#EJERCICIO2
divideATodosmedioraro(lista,5)
divideATodosmedioraro(listaPar,2)
print("")
divideATodos(lista,5)
divideATodos(listaPar,2)
print("")

#EJEERCICIO4
ordenados(lista)
ordenados(listaPar)
ordenados(listaNoOrd)
ordenados(listaVacia)
print("")

#EJERCIICO 5
palabraLarga(listaPalabras)
print("")

#EJERCIICO 6
palindromedo("hola aloh")
palindromedo("que dizex")
print("")



text="patocuack"
#EJERCICIO 7
seguridad("pato")
seguridad("patocuack1")
seguridad("PATOcuack1")
print("")

seguridad2("pato")
seguridad2("patocuack1")
seguridad2("PATOcuack1")
print("")

#EJERCICIO 8
bancoGalicia([("I",2000), ("R", 20),("R", 1000),("I", 300)])


#PARTE 2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#EJERCICIO 1

print(listanumeros)
paresPor0(listanumeros)
print(listanumeros)
print("")


print(listaINT)
paresPor0IN(listaINT)
print(paresPor0IN(listaINT))
print(listaINT)
print("")
print("")

sinVocales(text)
print("")

reemplazaVocales(text)
print("")

daVueltaStr(text)
print("it should say",text[::-1])
print("")

eliminarRepetidos("pattoccuack")
print("")

aprobado([4,4,4])
aprobado([7,7,7])
aprobado([7,5,3])
aprobado([8,5,4])
print("")



#EJERCICIO 4 (HAY INPUTS ASI Q DESPUES DE TESTEAR LOS COMENTO)
#nombresEstudiantes()

#sube()

#sieteYmedio()


#EJERCICIO 5
listaListas=[listaNoOrd,lista,listaPar]

#perteneceACadauno(listaListas,1)

matriz=[[1,2],[1,5],[3,4]]
notmatriz=[[1,2,3],[21,2],[1,5]]
matriz3X3=[[5,5,1],[1,1,1],[9,5,1]]

esMatriz(matriz)
esMatriz(notmatriz)
esMatriz(matriz3X3)
print("")

filasOrdenadas(matriz)
filasOrdenadas(matriz3X3)





