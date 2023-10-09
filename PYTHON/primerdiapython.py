import math

#BUSCAMOS DIVIDIR EL CODIGO DE PYTHON EN 3 BLOQUES
# ------------>IMPORTS
#------------>FUNCIONES
#------------>CODIGO LIBRE

#ABRIR PYTHON PONIENDO EN TERMINAL PYTHON3 
#PARA USAR EL FILE, PONER import filename
#PARA CORRER FUNCION, PRIMERDIAPYTHON.FUNCION



def daleBoca():
    print("DALEBOOOOO")

daleBoca()
daleBoca()



#Ejercicio 2. Definir las siguientes funciones y procedimientos con parametros

def esMultiploDeMIA(n,m):
    while n>m:
        n=n-m
    if n==m:
        return True
    else:
        return False                     


def esMultiploDeQUEFUNCIONA(n:int, m:int) -> bool:
    res:bool = n/m == int(n/m)
    return res



def esMultiploPOSTA(n:int, m:int):
    res: bool = n%m == 0 #---------------------->   PARA NO METER MUCHOS RETURN, ES MEJOR CREAR UNA VARIABLE Y DESPUES RETURNEAR ESO
    return res 

###################################un enchastre#########


#Ejercicio 3. Resuelva los siguientes ejercicios utilizando losoperadores lgicos and, or, not. Resolverlos sin utilizar alternativa condicional (if).

def es_nombre_largo(nombre:str) -> bool:
    longitudNombre:int= len(nombre)
    res:bool= longitudNombre>=3 and longitudNombre<=8 #tambien funciona: 3<= x <=8 
    return res

#Ejercicio 5
def devolver_el_doble_si_es_par(numero:int) -> int: #numero es un in, no usar para salida
    espar:bool= numero % 2 == 0
    res:int=numero

    if espar:
        res=res * 2

    return res    

#1.3
def imprimirunverso():
    print("la vaca lola la vaca lola\ntiene cabeza no tiene cola ")

#1.4
def raizDe2():
    raide2= math.sqrt(2)
    print(str(round(raide2,4)))
    return raide2


#1.5  perimetro: que devuelva el per´ımetro de la circunferencia de radio 1. Utilizar la biblioteca math mediante el 
# comando import math y la constante math.pi
#perimetro = 2 * pi * r

def perimetro() -> bool:
    pi= math.pi
    perimetro=2*pi
    print(str(perimetro))
    return(perimetro)  



####################EJERCICIO 2#########################

#2.1)
def imprimir_un_saludo(nombre:str) -> bool:
    print("Hola",nombre)


#2.2)
def raizCuadradaDeUnNumero(numero:int) -> float:

    if numero<0:
        res="pone un postivo broderick"
    else:
        res= math.sqrt(numero)    
        
    return res


#2.3)

def fahrenheit_a_celsius(tempfar):
    tempcelcius= ((tempfar - 32)*5)/9
    return tempcelcius


#2.4)
def imprimir_2_veces(estribillo:str) -> str:
    res=estribillo*2
    print(res)
    return res

def imprimir_las_veces_q_quieras(estribillo:str,numerodeveces:int) ->str:
    res=estribillo*numerodeveces
    print(res)
    return res


#2.6)
def es_par(numero:int) -> bool:
    return esMultiploPOSTA(numero,2)


#2.7)}
def cantidad_de_pizzas(comensales:int, mincantdeporciones:int)->int: #cada pizza tiene 8 porciones, y se prefiere q sobren
    pizzas = 1
    pizza_porcion=8
    mayorq1=pizza_porcion/(comensales*mincantdeporciones)
    while mayorq1 < 1:
        pizzas=pizzas + 1
        mayorq1=pizza_porcion*pizzas/(comensales*mincantdeporciones)

    return pizzas

def cantidadDEPIZZASBIEN(comensales:int, mincantdeporciones:int) ->int:
    res:int = round(((mincantdeporciones/8)*comensales)+0.9)
    return res




#PARA LOS FORS,VAMOS A TENER Q USAR RANGES, NO COSAS RARAS
#LA IDEA ES IMITAR LOS WHILES, POR EJ, PARA USAR UN WHILE
#Q SE TERMINE CUANDO I>5: FOR I IN RANGE(0,5,1), DONDE I
#AUMENTA CON +1.                    |
#                                   |tener en cuenta
#                                   |q el for es menor estricto



#EJERCICIO 6 TEORICA
#6.2) escribir una funcion que imprima los numeros pares entre el 10 y el 40.

def del10al40par():
    i=10
    while i <= 40:
        print(i)
        i=i+2


#EJERCICIO 7 TEORICA
def del10al40parconfor():
    i:int
    for i in range(10,42,2):
        print(i)

############################AGARRO LA GUIA DESDE EL 3

#TRUCOS PRINT(): 
# \T AGREGA TAB
# \N ES NEW LINE 
# etc




#3.1)
def alguno_es_0(numero1:float,numero2:float)-> bool:
    flag=not (numero1 !=0 and numero2 !=0)
    return flag 

#3.2)
def ambos_es_0(numero1:float,numero2:float)-> bool:
    flag= numero1 ==0 and numero2 ==0
    return flag 

#3.4)
def es_bisiesto(anio:int)->bool:
    res= anio%400==0 or (anio%4==0 and anio%100!=0)
    return res


#Ejercicio 4. Usando las funciones de python min y max resolver:
"""
En una plantacion de pinos, de cada arbol se conoce la altura expresada en metros. El peso de un pino se puede estimar
a partir de la altura de la siguiente manera:
3 kg por cada centımetro hasta 3 metros,
2 kg por cada centımetro arriba de los 3 metros.
Por ejemplo:
2 metros pesan 600 kg, porque 200 * 3 = 600
5 metros pesan 1300 kg, porque los primeros 3 metros pesan 900 kg y los siguientes 2 pesan los 400 restantes.
Los pinos se usan para llevarlos a una fabrica de muebles, a la que le sirven arboles de entre 400 y 1000 kilos, un pino
fuera de este rango no le sirve a la fabrica.
Definir las siguientes funciones, deducir que parametros tendran a partir del enunciado. Se pueden usar funciones auxiliares
si fuese necesario para aumentar la legibilidad.
1. Definir la funcion peso pino
2. Definir la funcion es peso util, recibe un peso en kg y responde si un pino de ese peso le sirve a la f´abrica.
3. Definir la funcion sirve pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la f´abrica.
4. Definir sirve pino usando composicion de funciones.
"""

def peso_pino(h:int) -> int: #h esta en metros
    primerfactor= min(900,100*h*3)
    segundofactor=max(h,3)                      #me parece rebuscadisimo
    peso= primerfactor+(segundofactor-3)*2*100
    print(peso)
    return peso                 



def peso_util(kg:int) -> bool:
    sirve:bool= False
    if 1000>=kg>=400:
        sirve=True
    return sirve

def sirve_pino(h:int) -> bool:
    sirve=peso_util(peso_pino(h))
    return sirve



#Ejercicio 5. Implementar los siguientes problemas de alternativa condicional (if). Intent´a especificarlos alguno de ellos 
# (todos los que te salgan) en lenguaje semiformal y formal sin utilizar IfThenElseFi.

"""1.
2. devolver valor si es par sino el que sigue(numero). que devuelve el mismo n´umero si es par y sino el siguiente.
Analizar distintas formas de implementaci´on (usando un if-then-else, y 2 if), ¿todas funcionan?

"""
def devolver_valor_si_es_par_sino_sig(numero):
    res:int
    if es_par(numero):
        res=numero
    else:
        res=numero+1    


"""
3.
devolver el doble si es multiplo3 el triple si es multiplo9(numero). En otro caso devolver el n´umero original. 
Analizar distintas formas de implementaci´on (usando un if-then-else, y 2 if, usando alguna opci´on de operaci´on
l´ogica), ¿todas funcionan?.

"""        

def devolver_el_doble_para3_o_para9(numero:int) ->int:
    res:int=numero
    if numero%3==0 and not numero%9==0:
        res= numero *2
    elif numero%9==0:
        res=numero*3
    print(res)
    return res
    

def devolver_el_doble_para3_o_para9OPC2(numero):
    res=numero
    if numero%3==0:
        if numero%9==0:
            res=numero*3
        else:
            res=numero*2
    print(res)
    return res

    
"""4.
 lindo nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga “Tu
nombre tiene muchas letras!” y sino, “Tu nombre tiene menos de 5 caracteres”.
"""
def lindo_nombre(nombre:str) ->str:
    respuesta:str=""
    if len(nombre)>=5:
        respuesta="Tu nombre tiene muchas letras!"
    else: respuesta="Tu nombre tiene menos de 5 caracteres"
    print(respuesta)
    return respuesta

"""5.
elRango(numero) que imprime por pantalla “Menor a 5” si el n´umero es menor a 5, “Entre 10 y 20” si el n´umero est´a
en ese rango y “Mayor a 20” si el n´umero es mayor a 20.
"""
def elRango(numero:int):
    printear=""
    if numero<=20:
        if numero<5:
            printear="Menor a 5"
        elif numero>=10:
            printear="Entre 10 y 20"
    else:
        printear="Mayor a 20"
    print(printear)

"""6.
En Argentina una persona del sexo femenino se jubila a los 60 a˜nos, mientras que aquellas del sexo masculino se jubilan
a los 65 a˜nos. Quienes son menores de 18 a˜nos se deben ir de vacaciones junto al grupo que se jubila. Al resto de
las personas se les ordena ir a trabajar. Implemente una funci´on que, dados los par´ametros de sexo (F o M) y edad,
imprima la frase que corresponda seg´un el caso: “And´a de vacaciones” o “Te toca trabajar”.
"""

def trabajo_o_vacaciones(sexo:str,edad:int)->str:
    destino:str
    if edad<18 or edad>=65:
        destino="VACAS"
    else:
        if edad>=60 and sexo=="F":
            destino="VACAS"
        else:
            destino="alaburar"
    print(destino)
    return destino


#Ejercicio 6. Implementar las siguientes funciones usando repetici´on condicional while:

"""3.
Escribir una funcion que imprima la palabra “eco” 10 veces.
"""

def eco10():
    i=0
    while i <10:
        print("eco")
        i=i+1


"""4.
Escribir una funci´on de cuenta regresiva para lanzar un cohete. Dicha funci´on ir´a imprimiendo desde el n´umero que
me pasan por par´ametro (que ser´a positivo) hasta el 1, y por ´ultimo “Despegue”.

"""
def rocket_lauch(T:int):
    while T>=1:
        print(T)
        T=T-1
    print("DESPEGUE!")

"""5.
Hacer una funci´on que monitoree un viaje en el tiempo. Dicha funci´on recibe dos par´ametros, “el a˜no de partida” y
“alg´un a˜no de llegada”, siendo este ´ultimo par´ametro siempre m´as chico que el primero. El viaje se realizar´a de a saltos
de un a˜no y la funci´on debe mostrar el texto: “Viaj´o un a˜no al pasado, estamos en el a˜no: <a˜no>” cada vez que se
realice un salto de a˜no.
"""

def maquinadeltiempo_DeA1(anioP:int,anioF:int):
    print("Viajare al pasado, estoy en el año",anioP)
    while anioP != anioF:
        anioP=anioP-1
        print("Viajo un año al pasado... Estamos en el año",anioP)

"""6.
Implementar de nuevo la funci´on de monitoreo de viaje en el tiempo, pero desde el a˜no de partida hasta lo m´as cercano
al 384 a.C., donde conoceremos a Arist´oteles. Y para que sea m´as r´apido el viaje, ¡vamos a viajar de a 20 a˜nos en cada
salto!

"""
def tiempoHaciaAristoteles_DeA20(anioP:int):
    anioF=-384
    print("Viajare al pasado, estoy en el año",anioP)
    while anioP > anioF+20:
        anioP=anioP-20
        if anioP <0:
            print("Viajo un año al pasado... Estamos en el año",str(anioP*(-1))+"a.c")


        else:
            print("Viajo un año al pasado... Estamos en el año",anioP)
    edadAristoteles=(anioF-anioP)*(-1)
    edadAristotelesposta=str(edadAristoteles)
    print("llegamos, Aristoteles deberia tener "+edadAristotelesposta+" años")


#Ejercicio 7. Implementar las funciones del ejercicio 6 utilizando for num in range(i,f,p):. Recordar que la funci´on
# range para generar una secuencia de n´umeros en un rango dado, con un valor inicial i, un valor final f y un paso p.

"""1.
. Escribir una funci´on que imprima los n´umeros del 1 al 10.
"""
def al10for():
    for i in range(1,11):

      print(i)

"""
 Escribir una funci´on que imprima los n´umeros pares entre el 10 y el 40.
"""
def paresdel10al40FOR():
    for i in range(10,41,2):
        print(i)

"""3.
Escribir una funcion que imprima la palabra “eco” 10 veces.
"""
def eco10FOR():
    eco="eco"
    for i in range(0,10,1):
        print(eco)

"""4.
Escribir una funci´on de cuenta regresiva para lanzar un cohete. Dicha funci´on ir´a imprimiendo desde el n´umero que
me pasan por par´ametro (que ser´a positivo) hasta el 1, y por ´ultimo “Despegue”.

"""
def rocket_lauchFOR(t:int):
    for i in range(0,t,):
        print(t)
    print("DESPEGUE!")
    
"""5.
Hacer una funci´on que monitoree un viaje en el tiempo. Dicha funci´on recibe dos par´ametros, “el a˜no de partida” y
“alg´un a˜no de llegada”, siendo este ´ultimo par´ametro siempre m´as chico que el primero. El viaje se realizar´a de a saltos
de un a˜no y la funci´on debe mostrar el texto: “Viaj´o un a˜no al pasado, estamos en el a˜no: <a˜no>” cada vez que se
realice un salto de a˜no.
"""
def maquinadeltiempo_DeA1FOR(aniop,aniof):
    print("VIAJARE AL PASADO, ESTOY EN EL AÑO",aniop)
    for i in range(aniof,aniop):
        aniop=aniop-1
        print("Viajo un año al pasado... Estamos en el año",aniop)

"""6.
Implementar de nuevo la funci´on de monitoreo de viaje en el tiempo, pero desde el a˜no de partida hasta lo m´as cercano
al 384 a.C., donde conoceremos a Arist´oteles. Y para que sea m´as r´apido el viaje, ¡vamos a viajar de a 20 a˜nos en cada
salto!

"""
def tiempoHaciaAristoteles_DeA20FOR(anioP:int):
    anioF=-384
    print("VIAJARE AL PASADO, ESTOY EN EL AÑO",anioP)
    for i in range(anioF+20, anioP, 20):
        anioP=anioP-20
        if anioP<0:
            print("Viajo 20 años al pasado, estamos en el año:",(anioP*-1))
        else:
            print("Viajo 20 años al pasado, estamos en el año:",anioP)

    edadAristoteles=(anioF-anioP)*(-1)
    edadAristotelesposta=str(edadAristoteles)
    print("llegamos, Aristoteles deberia tener "+edadAristotelesposta+" años")


#########################EJERCICIO 8


aver=type(tiempoHaciaAristoteles_DeA20)
print(aver)