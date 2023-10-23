import random
import numpy as np
#[[[[[[[[[[[[[[PRIMERA PARTE]]]]]]]]]]]]]]
#ejercicio1

"""
1. problema
pertenece (in s:seq<Z>, in e: Z) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔(existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e)}
}
Implementar al menos de 3 formas distintas este problema.
¿Si la especificaramos e implementaramos con tipos genericos, se podria usar esta misma funcion para buscar un
caracter dentro de un string?
"""

def pertenece(lista:[int],elem:int)->bool:
    res= False
    for i in range(len(lista)):
        if lista[i] == elem:
            res=True
    
    return res


def pertenece2(lista:list,elem:int)->bool:
    res:bool=False
    i=0
    while i < len(lista):
        if lista[i] == elem:
            res=True
        i+=1
    print(res)
    return res


#3, suma total

def sumaTotal(s:[int])->int:
    res:int=0
    for i in range(0,len(s),1):
        res=res+s[i]
    print(res)
    return res


"""2. 
problema divideATodos (in s:seq<Z>, in e: Z) : Bool {
requiere: {e != 0 }
asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0)}
}"""

def divideATodos(s:[int],elem:int)->bool:
    res=True
    for i in range(0,len(s),1):
        if s[i]%elem!=0:
            res=False
    print(res)
    return res

        
def divideATodosmedioraro(s:[int],elem:int)->bool:
    res=False
    contador:int=0
    for i in range(0,len(s),1):
        contador=contador+(s[i]%elem)
    if contador == 0:
        res=True
    print(res)
    return res

"""4
 problema ordenados (in s:seq<Z>) : Bool {
requiere: { T rue }
asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1]}
}"""

def ordenados(s:[int])->bool:
    res=True
    for i in range(0,len(s)-1,1):
        
        if s[i]>s[i+1]:
            res=False

    return res
            

#5. Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7.

def palabraLarga(listaPalabras:[str])->bool:
    res=False
    for i in range(0,len(listaPalabras),1):
        if len(listaPalabras[i])>7:
            res=True
    print(res)
    return res


#6. Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso contrario.

def palindromedo(texto:str)->bool:
    res=True
    for i in range(0,int(len(texto)/2),1):
        if texto[i] != texto[len(texto)-1-i]:
            res=False
    print(res)
    return res



"""
7. Analizar la fortaleza de una contrase˜na. El par´ametro de entrada de la funci´on ser´a un string con la contrase˜na a
analizar, y la salida otro string con tres posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la “˜n/ ˜N”
es considerado un caracter especial y no se comporta como cualquier otra letra.

La contrase˜na ser´a VERDE si:
a) la longitud es mayor a 8 caracteres
b) tiene al menos 1 letra min´uscula.
c) tiene al menos 1 letra may´uscula.
d ) tiene al menos 1 d´ıgito num´erico (0..9)

La contrase˜na ser´a ROJA si:
a) la longitud es menor a 5 caracteres.
En caso contrario ser´a AMARILLA."""

def seguridad(text:str)->bool:
    res:str="AMARILLo"

#CHEQUEO DE MAYUSMINUSNUM
    if len(text)>8:
        numerico:bool=False
        mayus=False
        minus=False
        for i in range(len(text)):
            if "0"<=text[i]<="9":
                numerico=True
            if text[i]<="z" and text[i]>="a":
                minus=True
            if text[i]<="Z" and text[i]>="A":
                mayus=True
        if numerico and mayus and minus:
            res= "VERDE"
#CHEQUEO DE MAYUSMINUSNUM
    if len(text)<5:
            res="ROJA"
    print(res)
    return res





def seguridad2(text:str)->bool:
    res:str="AMARILLO"
    if len(text)>8:
        if mayusminusnum(text):
            res="VERDE"

    elif len(text)<5:
        res="ROJA"
    

    print(res)
    return res


#CHEQUEO DE MAYUSMINUSNUM
def mayusminusnum(text:str)->bool:
        numerico:bool=False
        mayus=False
        minus=False
        
        for i in range(len(text)):
            if "0"<=text[i]<="9":
                numerico=True
            if text[i]<="z" and text[i]>="a":
                minus=True
            if text[i]<="Z" and text[i]>="A":
                mayus=True
        vale= numerico and mayus and minus
        return vale
#CHEQUEO DE MAYUSMINUSNUM


"""8.
 Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual.
Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de
dinero y “R” para retiro de dinero, y adem´as el monto de cada operaci´on. Por ejemplo, si la lista de tuplas es [(‘‘I’’,
2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280."""

def bancoGalicia(movimientos:[[str,int]])->int:  #el requioere evndrian a ser que mov es lista de listas de 2 elemntos, el str y el int
    res:int=0
    for mov in range(len(movimientos)):
        ior=""
        if (movimientos[mov])[0]=="I":
            res += (movimientos[mov])[1]
        else:
            res -= (movimientos[mov])[1]
    print(res)
    return res

            
#9. Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas y False en caso contrario
vocales=["A","E","I","O","U","a","e","i","o","u"]
def vocales3Distintas(text:str)->bool:
    res=False
    
    contadorVocales=0
    for i in range(len(vocales)):
        for j in range(len(text)):
            if text[j]==vocales[i]:
                contadorVocales +=1
                vocales[i]=""
    if contadorVocales>=3:
        res=True

    print(res)
    return res


vocales3Distintas("PATOCUACK")


#[[[[[[[[[[[[[[SEGUNDA PARTE]]]]]]]]]]]]]]
#EJERCICIO 2

"""1. 
Dada una lista de n´umeros, en las posiciones pares borra el valor original y coloca un cero. Esta funci´on modifica el
par´ametro ingresado, es decir, la lista es un par´ametro de tipo inout."""



def paresPor0(lista:list)->list:
    for i in range(len(lista)):
        if i%2==0:
            lista[i]=0

"""
2. Lo mismo del punto anterior pero esta vez sin modificar la lista original, devolviendo una nueva lista, igual a la anterior
pero con las posiciones pares en cero, es decir, la lista pasada como par´ametro es de tipo in."""

def paresPor0IN(lista):
    res=lista.copy()
    for i in range(len(res)):
        if i%2==0:
            res[i]=0
    return res

"""3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios,
sino que borra la vocal y concatena a continuaci´on.
"""

def sinVocales(text:str)->str:      #veo q no se pueden asignar nuevos valores a los strings (osea, a cada letra).
    res=""
    for i in range(len(text)):
        if not pertenece(vocales,text[i]):
            res+= text[i]
            
    print(res)
    return res

"""4. problema reemplazaVocales (in s:seq<Char>) : seq<Char> {
requiere: { T rue }
asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’) ∨
(¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i] ) ) }
}
"""

#la espeficifacion no esta hecha para las vocales en mayuscula, de igual manera tengo la lista de vocales ya hecha con ambas. Uso esa

def reemplazaVocales(text:str)->str:
    res:str=""
    for i in range(len(text)):
        if pertenece(vocales,text[i]):
            res+=" "
        else:
            res+=text[i]
    print(res)
    return res


"""5. problema daVueltaStr (in s:seq<Char>) : seq<Char> {
requiere: { T rue }
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| − i − 1]}
}"""

def daVueltaStr(text:str)->str:
    res=""
    for i in range(0,len(text)):
        res+=text[-(1+i)]
    print(res)
    return res



"""6. problema eliminarRepetidos (in s:seq<Char>) : seq<Char> {
requiere: { T rue }
asegura: {(|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
(0 ≤ i, j < |res| ∧ i 6= j) → res[i] 6= res[j])}
}"""
def eliminarRepetidos(text:str)->str:
    res=""
    
    for i in range(len(text)):
        serepite:bool=False
        for j in range(i+1,len(text)):
            if text[i]==text[j]:
                serepite=True
        if serepite==False:
            res+=text[i]
    print(res)
    return res

#Ejercicio 3
"""Ejercicio 3. Implementar una funci´on para conocer el estado de aprobaci´on de una materia a partir de las notas obtenidas
por un/a alumno/a cumpliendo con la siguiente especificaci´on:
problema aprobado (in notas: seqhZi) : Z {
requiere: {|notas| > 0}
requiere: {Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10)}
asegura: {res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7}
asegura: {res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio est´a entre 4 (inclusive) y 7}
asegura: {res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4}
}"""

def aprobado(notas:[int])->int:
    res:int=0
    sumaDeParciales=0
    instanciaRecuperacion=False

    for i in range(len(notas)):
        sumaDeParciales+=notas[i]
        if notas[i]<4:
            instanciaRecuperacion=True

    promedio=sumaDeParciales/len(notas)
    if promedio >=4 and instanciaRecuperacion==False:
        if promedio>=7:
            res=1
        else:
            res=2
    else:
        res=3
    print(res)
    return res


#Ejercicio 4. Vamos a elaborar programas interactivos (usando la funcion input()) que nos permita solicitar al usuario informaci´on cuando usamos las funciones.

"""1. Implementar una funci´on para construir una lista con los nombres de mis estudiantes. La funci´on solicitar´a al usuario
los nombres hasta que ingrese la palabra “listo”. Devuelve la lista con todos los nombres ingresados.
"""

def nombresEstudiantes():
    listaAlumnos=[]
    ingreso=""
    while ingreso!="listo":
        ingreso=input("Ingrese nombre del estudiante/a/0. Para terminar escriba listo.")
        if ingreso!="listo":
            listaAlumnos.append(ingreso)

    print(listaAlumnos)
    return listaAlumnos



"""2. Implementar una funci´on que devuelve una lista con el historial de un monedero electr´onico (por ejemplo la SUBE).
El usuario debe seleccionar en cada paso si quiere:
“C” = Cargar cr´editos,
“D” = Descontar cr´editos,
“X” = Finalizar la simulaci´on (terminar el programa).
En los casos de cargar y descontar cr´editos, el programa debe adem´as solicitar el monto para la operaci´on. Vamos a
asumir que el monedero comienza en cero. Para guardar la informaci´on grabaremos en el historial tuplas que representen
los casos de cargar (“C”, monto a cargar) y descontar cr´edito (“D”, monto a descontar).
"""

def sube()->list:

    carga:int=0
    historial:list=[]
    operacion:str=""
    while operacion!="X":
        operacion=input("C para cargar, D para descontar, X para finalizar: \n")
        if operacion=="C" or operacion=="D":
            cargarSube(historial,operacion)
    print(historial)
    return historial

def cargarSube(historial:list,operacion:str):
    credito:int=0
    if operacion=="C":
        credito=int(input("cuanto cargas broderick: "))
        historial=historial.append(credito)
    else:
        credito=int(input("cuanto descargas broderick: "))
        historial=historial.append(-credito)



"""3. Vamos a escribir un programa para simular el juego conocido como 7 y medio. El mismo deber´a generar un n´umero
aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deber´a luego preguntarle al usuario si desea seguir sacando otra “carta”
o plantarse. En este ´ultimo caso el programa debe terminar. Los n´umeros aleatorios obtenidos deber´an sumarse seg´un
el n´umero obtenido salvo por las “figuras” (10, 11 y 12) que sumar´an medio punto cada una. El programa debe ir
acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la funci´on devuelve
el historial de “cartas” que hizo que el usuario gane o pierda. Para generar n´umeros pseudo-aleatorios entre 1 y 12
utilizaremos la funci´on random.randint(1,12). Al mismo tiempo, la funci´on random.choice() puede ser de gran
ayuda a la hora de repartir cartas.
"""
    
#lo voy a hacer de 2 formas. una con random.randint y otra con random.choice

def sieteYmedio():
    carta=sacarCarta()
    suma=0
    historial:list=[]

    print("Jugaremos al site y medio! El objetivo es acercarse lo maximo posible al siete y medio sin pasarse. Las figuras valen medio punto y se juega sin 8 y 9. \n")
     
    teparas:str=""

    while teparas!="PARA" and suma<=7.5:
        carta=sacarCarta()
        historial.append(carta)

        suma+=carta


        print("Sacaste un "+str(carta))
        teparas=input("Queres otra mas? PARA para parar, o ingrese lo que desee para recibir otra carta\n")

    print(historial)
    if suma <= 7.5:
        print("En esta ronda acumulaste un total de: "+str(suma)+" Puntos.\n Felicitaciones!")
    else:
        print("Has perdido! Drafteaste una suma de cartas mayor que 7.5")
    return historial




        



def sacarCarta():
    carta:int=8
    while carta == 8 or carta==9:
        carta=random.randint(1,12)
    if carta== 10 or carta== 11 or carta== 12:
        carta=0.5
    return carta


# Ejercicio 5 Implementar las siguientes funciones sobre listas de listas:

"""1. problema perteneceACadaUno (in s:seq<seq<Z>>, in e:Z, out res: seq<Bool>) {
requiere: { T rue }
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ pertenece(s[i], e))}
}
Nota: Reutilizar la funci´on pertenece() implementada previamente para listas"""


def perteneceACadauno(s:[list],e:int)->[bool]:

    flags:[bool]=[]

    for i in range(len(s)):
        if pertenece(s[i],e):
            flags.append(True)
        else:
            flags.append(False)
    print(flags)
    return flags
        

    
"""2. problema esMatriz (in s:seq<seq<Z>>) : Bool {
requiere: { T rue }
asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|)}
}
"""

def esMatriz(s:[[int]])->bool:  #basically, cada "fila" (lista) tiene q tener la misma cantidad de elementos, mayor q 0
    res:bool=True

    for i in range(len(s)):
        if len(s[i])!=len(s[0]) and res==True:
            res=False
    print(res)
    return res



"""3. problema filasOrdenadas (in m:seq<seq<Z>>, out res: seq<Bool>) {
requiere: { esMatriz(m)}
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
}
"""

def filasOrdenadas(m:[[int]]):
    res=True
    for i in range(len(m)):
        if not(ordenados(m[i])) and res==True:
            res=False
    print(res)
    return res



"""4. Implementar una funci´on que tome un entero d y otro p y eleve una matriz cuadrada de tama˜no d con valores generados
al azar a la potencia p. Es decir, multiplique a la matriz generada al azar por s´ı misma p veces. Realizar experimentos
con diferentes valores de d. ¿Qu´e pasa con valores muy grandes?

Nota 1: record´a que en la multiplicaci´on de una matriz 
cuadrada de dimensi´on d por si misma cada posici´on se calcula
como 

Nota 2: para generar una matriz cuadrada de dimensi´on d con 
valores aleatorios hay muchas opciones de implementaci´on, 
analizar las siguientes usando la biblioteca numpy 
(ver recuadro):"""






def crearYelevar(d:int,p:int): #D ES TAMAÑANO, P ES ELEVADO A LA CUANTO
    m = np.random.randint(0,10, (d, d))
    print("Esta es la matriz no elevada: ")
    print(m)
    mElevada=m**p
    print("Esta es la matriz elevada: ")
    print(mElevada)

crearYelevar(2,2) #Cuando voy elevando los valores arranca a hacer cuaqlueri cosa




    
