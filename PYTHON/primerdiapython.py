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



