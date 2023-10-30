from queue import Queue as Cola
from queue import LifoQueue as Pila
import random


#Ejercicio 1. Implementar en Python:

"""1. Una funcion contarLineas(in nombre archivo : str) → int que cuenta y devuelva la cantidad de l´ıneas de texto del
archivo dado"""

def contarLineas(archivo:str)->int:
    archivo=open(archivo,"r")

    lineas:list=archivo.readlines()
    archivo.close()
    cantLineas:int=0
  
    for i in lineas:
        cantLineas=cantLineas+1
    print(cantLineas)
    return cantLineas










##$$$$$$$$$$$$$$$$$TRABAJO EN CLASE$$$$$$$$$$$:
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





#$$$$$$$$$$$$$$$$$TRABAJO EN CLASE$$$$$$$$$$$:


"""Ejercicio 3. Dado un archivo de texto, implementar una funci´on que escribe un archivo nuevo llemado reverso.txt que tiene
las mismas l´ıneas que el original, pero en el orden inverso.
Ejemplo: si el archivo original es

Esta es la primera linea .
Y esta es la segunda .

debe generar:

Y esta es la segunda .
Esta es la primera linea .
"""



def reverso(file):


    archivo=open(file,"r")
    lineas1=archivo.readlines()
    archivo.close()

    reversofile=open("reverso.txt","w")
    print(lineas1)                         #VEO Q LA ULTIMA ORACION NO TIENE SALTO DE LINEA, ASI QUE METERLE A LA PRIMERA UN +\N

    for i in range(len(lineas1)):
        
        bkwrdsLineas=lineas1[len(lineas1)-1-i]
        if i==0:
            reversofile.write(bkwrdsLineas+"\n")
        elif i==len(lineas1)-1:
        
            bkwrdsLineas=sacarBarraN(bkwrdsLineas)

            reversofile.write(bkwrdsLineas)
            
        else:
            reversofile.write(bkwrdsLineas)
    archivo.close()
    reversofile.close()
#Medio q se me enquilombo. voy a intnetar usar readline()

def sacarBarraN(texto:str):
    textoreemplazo=""
    for i in range(len(texto)):
        if not(texto[i]== "\n"):
            textoreemplazo += texto[i]
        else:
            break
    return textoreemplazo


"""Ejercicio 4. Dado un archivo de texto y una frase, implementar una funci´on que la agregue al final del archivo original (sin
hacer una copia).
"""

def agregarFrase(file,frase:str):
    archivo=open(file,"a")
    archivo.write(frase)
    archivo.close()

"""Ejercicio 5. idem, pero agregando la frase al comienzo del archivo original (de nuevo, sin hacer una copia del archivo)."""


def agregarFrasePrincipio(file,frase:str):      #PARA ESTE PROBLEMA SE PODRIA USAR PUNTERO, PERO NO LO VIMOS. PREGUNTAR
    archivo=open(file,"r")
    lineasOriginales=archivo.readlines()
    archivo.close()

    nuevasLineas=[]
    nuevasLineas.append(frase)
    for i in lineasOriginales:
        nuevasLineas.append(i)


    archivo=open(file,"w")
    for linea in nuevasLineas:
        archivo.write(linea)
    
"""Ejercicio 6. Implementar una funci´on que lea un archivo en modo binario y devuelva la lista de palabras legibles, donde vamos
a definir una palabra legible como:
secuencias de texto formadas por numeros, letras mayusculas/minusculas y los caracteres ‘ ’(espacio) y ‘ ’(gui´on bajo)
que tienen longitud >= 5

Una vez implementada la funci´on, probarla con diferentes archivos binarios (.exe, .zip, .wav, .mp3, etc).
Referencia: https://docs.python.org/es/3/library/functions.html#open
Para resolver este ejercicio se puede abrir un archivo en modo binario ‘b’. Al hacer read() vamos a obtener
una secuencia de bytes, que al hacer chr(byte) nos va a devolver un caracter correspondiente al byte
le´ıdo.
"""

def leerPalabrasLegibles(nombreArchivo:str):
    res=[]
    archivo= open(nombreArchivo,"rb")
    contenido = archivo.read()

    texto = contenido.decode("utf-8", errors="ignore") #decodear el texto
    
    

    palabras= texto.split()


    for palabra in palabras:
        if esValida(palabra) and len(palabra)>=5:
            res.append(palabra)
    archivo.close()
    print(res)
    return res


def esValida(palabra:str) -> bool: #ver q no cuenta los _ ni los ? ni las . , etc. Arreglarlo
    res=True

    for i in range(len(palabra)):
        if palabra[i] not in [1,2,3,4,5,6,7,8,9]:
            if  not('a' <= palabra[i] <= 'z'):
                if not('A' <= palabra[i] <= 'Z'):
                    if not palabra[i]==" " and not palabra[i]=="_":
                        res=False



    return res
#palabrasLegiblesBinario("textoEjemplo.txt")
#VER 8 Y 9


leerPalabrasLegibles("textobinario.txt")
#preguntar              FUNCIONA PARA TEXTO NORMAL, NOT BINARIO PONELEEEEEEE


"""Ejercicio 7. Implementar una funci´on que lea un archivo de texto separado por comas (comma-separated values, o .csv) que
contiene las notas de toda la carrera de un grupo de alumnos y calcule el promedio final de un alumno dado. La funci´on
promedioEstudiante(in lu : str) → float. El archivo tiene el siguiente formato:
nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
"""




def promedioEstudiante(lu : str) -> float:
    
    archivo=open("notas.csv","r")

    notasPosta=archivo.readlines()

    print(notasPosta)
    sumadenotas=0
    cantnotas=0
    notas=[]
    #ESTA LINEA ME DESTRUYE PERO ES NECESARIA
    for i in range(len(notasPosta)):
        notas.append(sacarBarraN(notasPosta[i]))
    #ESTA LINEA ME DESTRUYE PERO ES NECESARIA

    print(notas)
    for nota in notas:
        
        esLu=True
        cantcomas=0
        primerComa=False
        for i in range(len(nota)): #MENOS 1 EVITA SALTO DE LINEA PERO LA ULTIMA LINEA NO TIENE, LA PUTA MADREEEEEEEEEEEEE
            
            if esLu:

                if nota[i]!=",":
                    if not primerComa:
                        if nota[i]!=lu[i]:
                            esLu=False
                else:
                    cantcomas+=1 
                    primerComa=True
            
                if len(nota)-1==i:
                    cantnotas+=1
                    print(nota[i-1])
                    if nota[i-1]==",":
                        sumadenotas+=int(nota[i])
                    else:
                        sumadenotas+=10




        


    print(cantnotas)
    print(sumadenotas)
    promedio=sumadenotas/cantnotas
    print(promedio)
    return promedio


def promedioEstudiante2(lu):

    archivo=open("notas.csv","r")

    notasPosta=archivo.readlines()

    notas:[list]=[]
    #ESTA LINEA ME DESTRUYE PERO ES NECESARIA
    for i in range(len(notasPosta)):
        notareemplazo=notasPosta[i].split(",")
        notareemplazo[3]=sacarBarraN(notareemplazo[3])
        notas.append(notareemplazo)
    #ESTA LINEA ME DESTRUYE PERO ES NECESARIA
   
    sumadenotas=0
    cantnotas=0
    

    for nota in notas:
        if nota[0]==lu:
            cantnotas+=1
            sumadenotas+=int(nota[3])


    print(sumadenotas)
    print(cantnotas)
    if cantnotas!=0:

        promedio=sumadenotas/cantnotas
    else:
        promedio=0
    print(promedio)

    return promedio 

promedioEstudiante2("825/22")


#PILAS
#Ejercicio 8 ya lo hice creo
def pilaOrdHasta(hasta:int):
    pila=Pila()
    for i in range(0,hasta,1):
        pila.put(i)
    return pila

def pilaOrdHastaDesord(n,desde,hasta):
    pila=Pila()
    for i in range(n):

        num=random.randint(desde,hasta)

        pila.put(num)
    
    return pila



"""Ejercicio 9. Implementar una funci´on cantidad elementos(in p : pila) → int que, dada una pila, cuente y devuelva la cantidad de elementos que contiene.
 No se puede utilizar la funici´on LifoQueue.qsize(). Si se usa get() para recorrer la pila, esto
modifica el par´ametro de entrada. Y como la especificaci´on dice que es de tipo in hay que restaurarla."""

def cantidadElementos(p:Pila) ->int:
    pinicial=p
    lista=[]
    size=0

    
    while not p.empty():
        num=p.get()
        print(num)
        lista.append(num)
        size+=1
    for i in lista:
        p.put(i)


    print(p==pinicial)

    print(size)
    return size


"""Ejercicio 10. Dada una pila de enteros, implementar una funci´on buscar el maximo(in p : pila) → int que devuelva el m´aximo
elemento."""

def buscarElMaximo(p:Pila)->int:
    elementos=desarmarYarmarPila(p)
    print(elementos)
    for i in elementos:
        esmasgrande=True

        for j in elementos:
            if i<j:
                esmasgrande=False
        
        if esmasgrande:
            mayor=i
    print(mayor)
    return mayor
        


#aux
def desarmarYarmarPila(p:Pila)->list:
    lista=[]
    while not p.empty():
        num=p.get()
        lista.append(num)
    for i in lista:
        p.put(i)

    return lista
#aux



"""Ejercicio 11. Implementar una funci´on esta bien balanceada(in s : str) → bool que dado un string con una formula aritm´etica sobre los enteros, 
diga si los par´entesis estan bien balanceados. Las f´ormulas pueden formarse con:
los numeros enteros
las operaciones basicas +, −, x y /
parentesis
espacios
Entonces las siguientes son formulas aritm´eticas con sus par´entesis bien balanceados:
1 + ( 2 x 3 = ( 2 0 / 5 ) )
10 * ( 1 + ( 2 * ( =1)))
Y la siguiente es una formula que no tiene los par´entesis bien balanceados:
1 + ) 2 x 3 ( ( )
"""

def estaBienBalanceada(s):
    p=Pila()#PILA DE CARACTERES
    for i in s:
        p.put(i)

    operadores= ["x","/","+","-","*"]
    parentesisA=0
    parentesisB=0

    res=True
    while not p.empty():
        e=p.get()       #ABIEROTS NUNCA MAYOR QUE CERRADOS

        print(e)
        if e ==")":
            parentesisB+=1
        if e=="(":
            parentesisA+=1


        if parentesisA>parentesisB:
            res=False

        
        #operadores
        if e in operadores:
            if operadoractivo:
                res=False
                print("Uso de 2 operadores seguidos")
            else:
                operadoractivo=True
                
        else:
            operadoractivo=False
        
        #operadores

        if e not in ["1","2","3","4","5","6","7","8","9"]:
            if e not in operadores:
                if e not in [" ","(",")"]:
                    print("Uso de parametros no adecuados")
                    res=False

    print("parentesisA:",parentesisA)
    print("parentesisB:",parentesisB)
    if parentesisA==parentesisB and res==True:
        res=True
    else:
        res=False
    print(res)
    return res


"""Ejercicio 12. La notaci´on polaca inversa, tambi´en conocida como notaci´on postfix, es una forma de escribir expresiones matem´aticas
 en la que los operadores siguen a sus operandos. Por ejemplo, la expresi´on “3 + 4” se escribe como “3 4 +” en notaci´on
postfix. Para evaluar una expresi´on en notaci´on postfix, se puede usar una pila.
Escribe una funci´on en Python que tome una expresi´on en notaci´on postfix y la eval´ue. La expresi´on estar´a representada
como una cadena de caracteres, donde los operandos y operadores estar´an separados por espacios. Para simplificar el problema,
s´olo vamos a considerar los operandos ‘+’, ‘-’, ‘*’ y ‘/’(suma, resta, multiplicaci´on y divisi´on), los operadores son n´umeros.
Para resolver este problema, se recomienda seguir el siguiente algoritmo:
1. Dividir la expresi´on en tokens (operandos y operadores) utilizando espacios como delimitadores.
2. Recorre los tokens uno por uno.
a) Si es un operando, agr´egalo a una pila.
b) Si es un operador, saca los dos operandos superiores de la pila, apl´ıcale el operador y luego coloca el resultado en la
pila.
3. Al final de la evaluaci´on, la pila contendr´a el resultado de la expresi´on.
Ejemplo de uso:
expresion = "3 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
print(resultado) # Deber´ıa devolver 33"""


def evaluar_postfix(string:str)->int:
    p=Pila()

    ecuacion=string.split(" ")
    print(ecuacion)
    operadores=["+","-","/","*"]
    for i in ecuacion:
        if i in operadores:
            xD=int(p.get())
            xI=int(p.get())
            if i == "+":
                calc=xI+xD
            elif i == "-":
                calc=xI-xD
            elif i =="/":
                calc=xI/xD
            elif i =="*":
                calc=xI*xD
            
            p.put(str(calc))

        else:
            p.put(i)

    res=p.get()
    print(res)
    return res





#COLAS

"""Ejercicio 13. Usando la funci´on generar nros al azar() definida en la secci´on anterior, implementar una funci´on que arme
una cola de enteros con los numeros generados al azar. """
def colaAlAzar(n,desde,hasta):
    cola=Cola()
    for i in range(n):
        num=random.randint(desde,hasta)
        cola.put(num)
    return cola

"""
Ejercicio 14. Implementar una funci´on cantidad elementos(in c : cola) → int que, dada una cola, cuente y devuelva la
cantidad de elementos que contiene. Comparar con la versi´on usando pila. No se puede utilizar la funci´on Queue.qsize()."""

def cantidadElementosCOLA(c:Cola):
    cinicial=c
    lista=[]
    size=0

    
    while not c.empty():
        num=c.get()
        print(num)
        lista.append(num)
        size+=1
    for i in lista:
        c.put(i)


    print(c==cinicial)

    print(size)
    return size   


"""Ejercicio 15. Dada una cola de enteros, implementar una funci´on buscar el maximo(in c : cola) → int que devuelva el m´aximo
elemento. Comparar con la versi´on usando pila.
"""
def maximoCola(c:Cola)->int:
    elementos=desarmarYarmarCola(c)
    print(elementos)
    for i in elementos:
        esmasgrande=True

        for j in elementos:
            if i<j:
                esmasgrande=False
        
        if esmasgrande:
            mayor=i
    print(mayor)
    return mayor

#aux
def desarmarYarmarCola(c:Cola)->list:
    lista=[]
    while not c.empty():
        num=c.get()
        lista.append(num)
    for i in lista:
        c.put(i)

    return lista
#aux

"""Ejercicio 16. Bingo: un cart´on de bingo contiene 12 n´umeros al azar en el rango [0, 99].
1. implementar una funci´on armar secuencia de bingo() → Cola[int] que genere una cola con los n´umeros del 0 al 99
ordenados al azar.
2. implementar una funci´on jugar carton de bingo(in carton : list[int], in bolillero : cola[int]) → int que toma un
cart´on de Bingo y una cola de enteros (que corresponden a las bolillas numeradas) y determina cual es la cantidad de
jugadas de ese bolillero que se necesitan para ganar.
"""


def secuenciaBingo():
    cola=Cola()
    numeros=[]

    for i in range(0,100): #PRUEBO CON 10 PRIMERO
        num=random.randint(0,99)
        while num in numeros:
            num=random.randint(0,99) #TAL VEZ ESTO TARDE AÑOS
        numeros.append(num)




        cola.put(num)

    print("")
    return cola

print("\n\n\n")


def jugarCartonBingo(carton:list,bolillero:Cola): #carton tiene 15 numeros
    jugada=0
    print(len(carton))
    fichascarton=15
    
    while fichascarton!=0:
        
        bola=bolillero.get()
        print(bola)
        jugada+=1
        print(bola in carton)
        if bola in carton:
            fichascarton=fichascarton-1
    print(jugada)
    return jugada
        



"""Ejercicio 17. Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atenci´on
para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la mas urgente
y requiere atenci´on inmediata) junto con su nombre y la especialidad medica que le corresponde.
Implementar la funci´on n pacientes urgentes(in c : Cola[(int, str, str)]) → int que devuelve la cantidad de pacientes de
la cola que tienen prioridad en el rango [1, 3]."""
#PONGO EN PAUSA COLA PARA REPASAR BIBLIOTECAS







#4. Diccionarios

"""Ejercicio 20. Volver a implementar la funci´on que calcula el promedio de las notas de los alumnos, pero ahora devolver un
diccionario {libreta universitaria : promedio} con los promedios de todos los alumnos.
"""



def promedioEstudiante2LIBRETAPOSTA():

    archivo1=open("notas.csv","r")

    notasPosta=archivo1.readlines()



    lus:[list]=[]
    #ESTA LINEA ME DESTRUYE PERO ES NECESARIA
    for i in range(len(notasPosta)):
        notareemplazo=notasPosta[i].split(",")
        if notareemplazo not in lus:

            lus.append(notareemplazo[0])
    #ESTA LINEA ME DESTRUYE PERO ES NECESARIA
   
    d={}
    
    for lu in lus:
        d[lu]=promedioEstudiante2(lu)

    print(d)
    return d
        
#promedioEstudiante2LIBRETAPOSTA()