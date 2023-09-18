{--
problema fibonacci (n: Z) : Z {
            requiere: { n ≥ 0 }
            asegura: { resultado = f ib(n) }
}
--}

fibonacci:: Integer ->Integer
fibonacci n | n==0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)


patternFib :: Integer -> Integer 
patternFib 0=0
patternFib 1=1
patternFib n =fibonacci(n-1) + fibonacci(n-2)

{-- EJERCICIO 2)
Implementar una funcion parteEntera :: Float -> Integer
que calcule la parte entera de un numero real positivo.
problema parteEntera (x: R) : Z {
requiere: { True }
asegura: { resultado ≤ x < resultado + 1 }
}
--}
parteEntera :: Float -> Integer
parteEntera x | 0<=x && x<1 = 0
              | otherwise = 1+ parteEntera (x-1) --sin embargo no estoy contemplandolosnegativos


parteEnteraPosta :: Float -> Integer
parteEnteraPosta x | 0<=x && x<1 = 0
                   | x>1 = 1 + parteEnteraPosta(x-1)               
                   | otherwise = -1 + parteEnteraPosta (x+1)

{-- 7)
problema todosDigitosIguales (n: Z) : B {
            requiere: { n > 0 }
            asegura: { resultado = true ↔ todos los dıgitos de n son iguales }
}

--}



todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n<10 = True
                      | otherwise = mod n 10 == div(mod n 100) 10 && todosDigitosIguales (div n 10) --se puede usar funciones aux



{--3)
determinar si el primero es divisble por el segundo. not mod and not div
--}
esDivisible :: Integer ->Integer ->Bool 
esDivisible a b | a==b = True
                | a<b = False
                | otherwise = esDivisible (a-b) b


{--4)
determinan una funcion q sume los primeros n numeros impares
--}

sumaImpares :: Integer ->Integer
sumaImpares n | n==1 || n==0  = n
              | otherwise = (2*n)- 1 + sumaImpares (n-1)
          




{--
problema iesimoDigito (n: Z, i: N) : Z {
    requiere: { n ≥ 0 ∧ 1 ≤ i ≤ cantDigitos(n) }
    asegura: { resultado = (n div 10cantDigitos(n)−i) mod 10 }
}
problema cantDigitos (n: Z) : N {
    requiere: { n ≥ 0 }
    asegura: { n = 0 → res = 1}
    asegura: { n 6 = 0 → (n div 10res−1 > 0 ∧ n div 10res = 0) }
}
--}
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = mod n 10
                 | otherwise = iesimoDigito (div n 10) i 


cantDigitos :: Integer -> Integer -- n es mayor q 0
cantDigitos n | n<10 = 1
              | otherwise = 1+ cantDigitos(div n 10) 

              -- 123 2 |23 1 |3 0


-- #####################EJERCICIOS

{--5)
Implementar la funcion medioFact :: Integer ->Integer que dado n ∈ N calcula n!! = n(n-2)(n-4)
--}

medioFact :: Integer ->Integer
medioFact n | n<=0 = 1
            |otherwise= n * medioFact(n-2)


{--6)
Especificar e implementar la funcion sumaDigitos :: Integer ->Integer que calcula la 
suma de dıgitos dun numero natural. Para esta funcion pueden utilizar div y mod--}

sumaDigitos :: Integer ->Integer
sumaDigitos n | n <10 = n
              | otherwise = ultimoDigito n + sumaDigitos(sacarUno n)


-- AYUDAS DE SACAR NUMEROS
ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

sacarUno :: Integer -> Integer
sacarUno n= div n 10
-- AYUDAS DE SACAR NUMEROS


{--7)
Implementar la funcion todosDigitosIguales :: Integer ->Bool que determina si 
todos los dıgitos de un numero natural son iguales, es decir:
--}

todosDigitosIguales2 :: Integer -> Bool
todosDigitosIguales2 n | n < 10 = True
                      | otherwise = sacarUno n == ultimoDigito(sacarUno n) && todosDigitosIguales(sacarUno n) 

{--9)
Especificar e implementar una funcion esCapicua :: Integer ->Bool que dado n ∈ N≥0 determina si n es
un numero capicua.
--}
esCapicua :: Integer ->Bool --si se lee igual de derecha a izquierda: 151, 1441, 12321
esCapicua n | n<10 = True 
            |otherwise = ultimoDigito n == darmeElPrimero n  && esCapicua(sacarElPrimero(sacarUno n )) 

sacarElPrimero :: Integer -> Integer
sacarElPrimero n = mod n (10^((cantDigitos n)-1))

darmeElPrimero :: Integer -> Integer
darmeElPrimero n = div n (10^((cantDigitos n)-1))


{--10)
 a) f1= la sumatoria de 2^i hasta n. empezando desde i = 0

problema f1 (n: Z) : Z {
    requiere: { n>0 }
    asegura: { resultado = la sumatoria de 2^i hasta n. empezando desde i = 0 }
--}

f1 :: Integer -> Integer
f1 n | n == 0 =1
     | otherwise = 2^n + f1(n-1)

{--
problema f2 (n:Z), (q:R): r{
    requiere:{n>0}
    asegura:{la sumatoria de q^i hasta n empezando en i =1}
}
--}     

f2 :: Integer -> Float -> Float
f2 n q | n==1 = q 
       | otherwise = q^n + f2 (n-1) q 


{--
problema f3 (n:Z), (q:R): r{
    requiere:{n>0}
    asegura:{la sumatoria de q^i hasta 2n empezando en i = 1}
}
--} 

f3 :: Integer -> Float -> Float
f3 n q | n==1 = q + q^2 
       | otherwise = q^(2*n) + q^((2*n)-1) + f3(n-1) q


{--
problema f4 (n:Z), (q:R): r{
    requiere:{n>0}
    asegura:{la sumatoria de q^i hasta 2n empezando en i = n}
} es lo mismo q hacer la normal, f2

ver
--} 


{--
11) Especificar e implementar una funcion eAprox :: Integer ->Float que aproxime el 
valor del numero e a partir de la siguiente sumatoria:

problema eAprox (n:Z): R{
    requeire: {n>=0}
    asegura: {aproximacion del numero e a partir de la sumatoria (1/i) desde i =0 hasta n}
}
--}

eAprox :: Integer -> Float
eAprox n | n == 0 = 1 
         | otherwise = (1/fromIntegral(factorial n) ) + eAprox (n-1)

factorial :: Integer -> Integer 
factorial n | n == 0 = 1
            | otherwise = n * factorial (n-1)

e :: Float
e = eAprox 10




{--
12) para n>0, se define an= 2+(1/2+(1/2+(1/...))) con n veces el 2.
Resulta en a1= 2, an= 2+[1/(an-1)].

definir raizDe2Aprox dado q raiz de 2 es casi an-1

problema raizDe2Aprox (n:Z): R{
        requiere:{n>0}
        asegura:{la aproximacion de raiz de 2 dado sqrt2= an-1 con an=2+[1/(an-1)]}
}

--}

raizDe2Aprox :: Integer ->Float 
raizDe2Aprox n | n==1 = 1
               | otherwise = 2+(1/(raizDe2Aprox (n-1) +1)) -1
               

{--13)
problema sumatoriaDoble (n:Z), (m:Z) : Z{
    requiere:{n>0}
    asegura:{res= la sumatoria desde i=1 a n de la sumatoria desde j=1 hasta m de i^j}
}
--}

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble n m | n == 0 = 0
                   | otherwise = sumatoriaHastaM n m + sumatoriaDoble (n-1) m


sumatoriaHastaM :: Integer -> Integer -> Integer
sumatoriaHastaM n m | m== 1 =n 
                    | otherwise = n^m + sumatoriaHastaM n (m-1)


{--14)
Especificar e implementar una funcion sumaRacionales :: Integer ->Integer ->Float
que dados dos naturales n, m sume todos los numeros racionales de la forma p/q 
con 1 ≤ p ≤ n y 1 ≤ q ≤ m, es decir:

problema sumaRacionales (n : N, m : N) : R {
requiere: {True}
asegura: { resultado =

--}

sumaRacionales :: Integer ->Integer ->Float -- veo n maneja p, y m q
sumaRacionales n m | n == 0 = 0
                   |  otherwise= sumaDenominador n m + sumaRacionales (n-1) m

sumaDenominador :: Integer -> Integer -> Float
sumaDenominador n m | m ==0 = 0
                    | otherwise =  (fromIntegral n/ fromIntegral m) + sumaDenominador n (m-1)



{--16=
Recordemos que un entero p > 1 es primo si y solo si no existe un entero k tal 
que 1 < k < p y k divida a p.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a) Implementar menorDivisor :: Integer ->Integer que calcule el menor divisor (mayor que 1)
de un natural n pasado como parametro.


--}

menorDivisor :: Integer ->Integer
menorDivisor n | n==1 = 1 
               | otherwise= menorDivisorAux n 2

menorDivisorAux :: Integer -> Integer -> Integer 
menorDivisorAux n y | esDivisible n y = y
                    | otherwise = menorDivisorAux n (y+1)

{--
b) Implementar la funcion esPrimo :: Integer ->Bool que indica si un numero natural
 pasado como parametro es primo.

--}

esPrimo :: Integer ->Bool 
esPrimo n | menorDivisor n == n = True
          | otherwise= False  
       
{--
c) Implementar la funcion sonCoprimos :: Integer ->Integer ->Bool que dados dos
 numeros naturales indica si no tienen algun divisor en comun mayor estricto que 1.

--}


sonCoprimos :: Integer ->Integer ->Bool
sonCoprimos n m | n == m = False
                | otherwise = not(comparteDivisor n m 2)

comparteDivisor :: Integer ->Integer->Integer -> Bool
comparteDivisor n m z | z>n || z>m = False -- si z pasa a ser mayor q el numero, ya esta, no hay mas divisores en comun. ambos empiezan desde 2. 
                      | otherwise= (esDivisible n z && esDivisible m z)|| comparteDivisor n m (z+1)  


{--
d) ) Implementar la funcion nEsimoPrimo :: Integer ->Integer que devuelve el n-esimo
 primo (n ≥ 1). Recordar que el primer primo es el 2, el segundo es el 3, el tercero es el 5, etc.

--}

nEsimoPrimo :: Integer ->Integer
nEsimoPrimo 1 = 2 
nEsimoPrimo n = n


primoEntre2y5 :: Integer -> Integer -> Integer 
primoEntre2y5 n i | esPrimo i = primoEntre2y5 n i+1 


{--17)
Implementar la funcion esFibonacci :: Integer ->Bool segun la siguiente especificacion:
problema esFibonacci (n: Z) : Bool {
    requiere: { n ≥ 0 }
    asegura: { resultado = true ↔ n es algun valor de la secuencia de Fibonacci definida en el ejercicio 1}
}
--}


esFibonacci :: Integer ->Bool
esFibonacci 1 = True 
esFibonacci n =perteneceAlaSerie n 2

perteneceAlaSerie :: Integer -> Integer -> Bool
perteneceAlaSerie n i | fibonacci i > n = False 
                      | fibonacci i == n = True 
                      | otherwise = perteneceAlaSerie n (i+1)  


{--Ejercicio 18)
Implementar una funcion mayorDigitoPar :: Integer ->Integer segun la siguiente especificacion
problema mayorDigitoPar (n: N) : N {
    requiere: { True }
    asegura: { resultado es el mayor de los dıgitos pares de n. Si n no tiene ningun dıgito par, entonces resultado es -1.
}
--}

mayorDigitoPar :: Integer ->Integer
mayorDigitoPar n | n < 10 && even n = n
                 | n < 10 && odd n = -1
                 | even (ultimoDigito n) = devolverDigitoMayorPar (ultimoDigito n) (sacarUno n) ((cantDigitos n) -1)
                 | otherwise = mayorDigitoPar (sacarUno n)

devolverDigitoMayorPar :: Integer -> Integer -> Integer-> Integer 
devolverDigitoMayorPar n m i | i == 0 = n
                             | even (ultimoDigito m) == compararPares n (ultimoDigito m) = devolverDigitoMayorPar n b (i-1)
                             | odd (ultimoDigito m) = devolverDigitoMayorPar n b (i-1)
                             | otherwise= devolverDigitoMayorPar (ultimoDigito m) b (i-1)
                             where b = sacarUno m


compararPares :: Integer -> Integer -> Bool
compararPares n m = n>= m





{--
Ejercicio 19. Implementar la funicion esSumaInicialDePrimos :: Int ->Bool segun la siguiente especificacion:

problema esSumaInicialDePrimos (n: Z) : B {
     requiere: { n ≥ 0 }
      asegura: { resultado = true ↔ n es igual a la suma de los m primeros numeros primos, para alg´un m.}
}
--}

esSumaInicialDePrimos :: Integer ->Bool
esSumaInicialDePrimos n | n==1 = False
                        | otherwise= formadoPorP n 2 2

formadoPorP :: Integer -> Integer -> Integer-> Bool
formadoPorP n i i2 | n== i = True 
                   | n < i = False
                   | otherwise = formadoPorP n (i + nEsimoPrimo i2) (i2+1)




{--Ejercicio 20). Especificar e implementar la funcion tomaValorMax :: Int ->Int ->Int que dado un n´umero entero n1 ≥ 1
y un n2 ≥ n1 devuelve algun m entre n1 y n2 tal que sumaDivisores(m) = max{sumaDivisores(i) | n1 ≤ i ≤ n2}
--}

sumaDivisores :: Integer -> Integer
sumaDivisores x | x==1 = 1 
                | otherwise = sumaConIndiceDivisores x 1 

sumaConIndiceDivisores :: Integer -> Integer -> Integer
sumaConIndiceDivisores x i | i == x = x 
                           | mod x i == 0 = i+sumaConIndiceDivisores x (i+1)
                           | otherwise = sumaConIndiceDivisores x (i+1)  



tomaValorMax :: Integer ->Integer ->Integer
tomaValorMax n1 n2 | n1 == n2 = max (sumaDivisores n1) (sumaDivisores n2)
                   | otherwise = ciclarMaxindice n1 n2 (n1+1)

ciclarMaxindice :: Integer ->Integer ->Integer->Integer
ciclarMaxindice n1 n2 i | n1 > n2 || i > n2 = n1
                        | sumaDivisores n1 > sumaDivisores (i) = ciclarMaxindice n1 n2 (i+1)
                        | otherwise = ciclarMaxindice i n2 (i+1)




{--Ejercicio 21)
Especificar e implementar una funcion pitagoras :: Integer ->Integer ->Integer ->Integer que dados
m, n , r ∈ N≥0, cuente cuantos pares (p, q) con 0 ≤ p ≤ m y 0 ≤ q ≤ n satisfacen que p^2 + q^2 <= r^2

 Por ejemplo:
pitagoras 3 4 5 -> 20
pitagoras 3 4 2 ->6
--}


{--pitagoras :: Integer ->Integer ->Integer ->Integer
pitagoras 0 0 _ = 1
pitagoras _ (-1) _ = 0
pitagoras n m r = sumatoriaNM n m r n

sumatoriaNM :: Integer -> Integer-> Integer-> Integer-> Integer
sumatoriaNM n m r i | m < 0 = 0 
                    | n < 0 = sumatoriaNM i (m-1) r i
                    | n^2 + m^2 <= r^2 = 1 + sumatoriaNM (n-1) m r i        --PREGUNTAR RELEVANCIA DE RESOLVERLO DE LA FORMA FUNCIONAL EXPLICITA O CON VARIABLE "i" EN PARCIAL
                    | otherwise = sumatoriaNM (n-1) m r i --}

pitagoras :: Integer ->Integer ->Integer ->Integer
pitagoras 0 0 _ = 1
pitagoras _ (-1) _ = 0
pitagoras n m r = sumatoriaNM n m r + pitagoras n (m-1) r

sumatoriaNM :: Integer -> Integer-> Integer-> Integer
sumatoriaNM n m r | m < 0 = 0 
                  | n < 0 = 0
                  | n^2 + m^2 <= r^2 = 1 + sumatoriaNM (n-1) m r 
                  | otherwise = sumatoriaNM (n-1) m r 


 



