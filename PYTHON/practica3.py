from queue import LifoQueue as Pila
 

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
    print(textoreemplazo)
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

promedioEstudiante("825/22")













