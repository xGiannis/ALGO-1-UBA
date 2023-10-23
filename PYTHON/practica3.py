from queue import LifoQueue as Pila
 

#Ejercicio 1. Implementar en Python:

"""1. Una funci´on contarLineas(in nombre archivo : str) → int que cuenta y devuelva la cantidad de l´ıneas de texto del
archivo dado"""



#%%%%%%%%%%%%%%%%TRABAJO EN CLASE%%%%%%%%%%%%%%%%%%%:
"""jercicio 2
Dado un archivo de texto con comentarios, implementar una
funci´on clonarSinComentarios(in nombre archivo : str) que
toma un archivo de entrada y genera un nuevo archivo
(sinComentarios.txt) que tiene el contenido original sin las l´ıneas
comentadas. Para este ejercicio vamos a considerar comentarios
como aquellas l´ıneas que tienen un caracter # como primer
caracter de la l´ınea, o si no es el primer caracter, se cumple que
todos los anteriores son espacios."""
tex="patata"
print(tex[0])

def clonarSinComentarios(nombrearchivo:str):


    newtext=[]
    archivo=open(nombrearchivo,"r")
    lista=archivo.readlines()
    for i in range(len(lista)):

        if (lista[i])[0]==" ":
            if not(chequearPrimerLetra("#",lista[i])):
                newtext.append(lista[i])        
        elif (lista[i])[0]!="#":
            newtext.append(lista[i])
    archivo.close()
    salida=open("sinComentariosfuncionmia.txt","w")
    for l in newtext:
        salida.write(l)
    salida.close()



    

    print(newtext)


def chequearPrimerLetra(letra:str,texto)->bool:
    esletra=True
    for caracter in texto:
        if esletra==True:
            if caracter!=letra:
                if caracter != " ":
                    esletra=False
            else:
                return esletra
    return esletra




    

def clonarSinCommentPOSTA(nombrearchivo:str):
    archivo=open(nombrearchivo,"r")
    lineas= archivo.readlines()

    archivonuevo=[]

    for l in lineas():
        s = l.strip()

        if len(s)==0 or not ("#" == s[0]):
            archivonuevo.append(l)
    archivo.close()

    salida=open("sinComentarios.txt","w")
    for i in archivonuevo:
        salida.write()




#clonarSinComentarios("ejemploComentado.py")



"""Ejercicio 10
Dada una pila de enteros, implementar una funci´on
buscarElMaximo(in p : pila) → int que devuelva el m´aximo
elemento."""


def buscarElMaximo(pila:Pila): #LA VERFA ESTA ES IN, OSEA Q NO HAY Q MODIFICAR PILA...  HACER FUNCION Q HAGA COPIA
    p2=pila

    elemmax=pila.get()
    while not pila.empty():
        acomparar=pila.get()
        if elemmax < acomparar:
            elemmax=acomparar
    print(elemmax)
    return elemmax





#ver .split()
"""Ejercicio 19 Leer un archivo de texto y agrupar la cantidad de
palabras de acuerdo a su longitud. Implementar la funci´on
agruparPorLongitud(in nombre archivo : str) → dict que
devuelve un diccionario
{longitud en letras : cantidad de palabras}."""

def agruparPorLongitud(nombreArchivo:str)->dict:
    archivo=open(nombreArchivo,"r")
    lista=archivo.readlines()

    d={}
    

    for linea in lista:
        for palabra in linea.split():

            if len(palabra) in d:
                d[len(palabra)]=d[len(palabra)]+1
            else:
                d[len(palabra)]=1
    print(d)
    return d





#%%%%%%%%%%%%%%%%TRABAJO EN CLASE%%%%%%%%%%%%%%%%%%%: