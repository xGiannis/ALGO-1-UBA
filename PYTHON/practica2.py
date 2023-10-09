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
    print(res)
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
    print(res)
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

def vocales3Distintas(text:str)->bool:
    res=False
    vocales=["A","E","I","O","U","a","e","i","o","u"]
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



