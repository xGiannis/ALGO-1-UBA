import Data.Type.Equality (TestEquality(testEquality))
{--
VEO QUE 0:[1,2,3] = [0,1,2,3]. LO SUMO A LA LISTA
POR OTRO LADO, [1,2,3] ++ [0] = [1,2,3,0]. CONCATENA LISTAS

SOLO PODEMOS USAR TAIL, HEAD Y ESTAS 2 FORMAS DE AGREGAR 

l= [1,2,3]

head(l)= 1
tail(l)= [2,3]

--}


-- vamos a implementar la funcion longitud :: [t] -> Int

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs)= 1 + longitud xs -- podia escricbir longitud (_:xs) = ...

longitud2 :: [t] -> Integer
longitud2 [] = 0
longitud2 l = 1 + longitud (tail l)


{--
Ejercicio 2.4) Definir la siguiente funcion sobre listas:
hayRepetidos :: (Eq t) => [t] -> Bool
problema hayRepetidos (s: seq〈T 〉) : B {
        requiere: { True }
        asegura: { resultado = true ↔ existen dos posiciones
                    distintas de s con igual valor }
}
--}


hayRepetidosF :: (Eq t) => [t] -> Bool
hayRepetidosF [] = False
hayRepetidosF [x] = False
hayRepetidosF (x:y:xs) | x==y = True 
                       | hayRepetidosF (x:xs) == False  = hayRepetidosF(y:xs)
                       |otherwise = True



hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [x] = False
hayRepetidos (x:y:xs) | checkRepetidos (x:y:xs) = True
                      | otherwise = checkRepetidos (y:xs)  


checkRepetidos :: (Eq t) => [t] -> Bool
checkRepetidos [x]=False
checkRepetidos (x:y:xs) | x==y = True
                        | otherwise = checkRepetidos (x:xs)



{--Ejercicio 3)
 Definir las siguientes funciones sobre listas de enteros
problema maximo (s: seq〈Z〉) : Z {
requiere: { |s| > 0 }
asegura: { resultado ∈ s ∧ todo elemento de s es menor o
igual a resultado}
}
--}


maximo :: [Integer] -> Integer
maximo [x] = x 
maximo (x:y:xs) | x>y = maximo (x:xs)
                | otherwise = maximo (y:xs)

{--
)$$$$$$$$$$$$$$$$$$$$$$$$$$     EJERCICIO 1)    $$$$$$$$$$$$$$$$$$$$$$$$$$

.2)
. ultimo :: [t] -> t seg´un la siguiente especificaci´on:

problema ultimo (s: seq⟨T⟩) : T {
        requiere: { |s| > 0 }
        asegura: { resultado = s[|s| − 1] }
}

--}


ultimo :: [t] -> t
ultimo [x] = x 
ultimo (x:xs) = ultimo xs


{--3. principio :: [t] -> [t] seg´un la siguiente especificaci´on:
problema principio (s: seq⟨T⟩) : seq⟨T⟩ {
        requiere: { |s| > 0 }
        asegura: { resultado = subseq(s, 0, |s| − 1) }
}--}

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = xs

{--
4. reverso :: [t] -> [t] seg´un la siguiente especificaci´on:
problema reverso (s: seq⟨T⟩) : seq⟨T⟩ {
        requiere: { T rue }
        asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
}

--}

reverso :: [t] -> [t]
reverso [] = []
reverso[x]= [x]
reverso (x:xs) =  reverso xs ++ [x] 


{--)$$$$$$$$$$$$$$$$$$$$$$$$$$     EJERCICIO 2)    $$$$$$$$$$$$$$$$$$$$$$$$$$
1.)
pertenece :: (Eq t) => t -> [t] -> Bool segun la siguiente especificacion:
problema pertenece (e: T, s: seq⟨T⟩) : B {
        requiere: { T rue }
        asegura: { resultado = true ↔ e ∈ s }
}
--}
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | n == x =True
                   | otherwise = pertenece n xs     



{--2.)
todosIguales :: (Eq t) => [t] -> Bool, que dada una lista devuelve verdadero s´ı y solamente s´ı todos sus elementos son iguales.

}
--}

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:xs) | x == y = todosIguales (y:xs)
                      | otherwise = False  



{--3. todosDistintos :: (Eq t) => [t] -> Bool segun la siguiente especificacion:
problema todosDistintos (s: seq⟨T⟩) : B {
        requiere: { T rue }
        asegura: { resultado = false ↔ existen dos posiciones distintas de s con igual valor}
--}

todosDistintos :: (Eq t) => [t] -> Bool 
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:y:xs) | (x/=y) == todosDistintos (x:xs) && todosDistintos (y:xs) = True
                        | otherwise = False


{--5. quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs,
elimina la primera aparici´on de x en la lista xs (de haberla).

--}
quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x (y:xs) | x == y = xs
                | otherwise = y: quitar x xs


{--6. quitarTodos :: (Eq t ) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina todas las apariciones
de x en la lista xs (de haberlas). Es decir:
problema quitarTodos (e: T, s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { T rue }
asegura: { resultado es igual a s pero sin el elemento e. }
}

--}

quitarTodos:: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (y:xs) | e == y = quitarTodos e xs 
                     | otherwise = y : quitarTodos e xs   



{--7. eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una unica aparicion de cada elemento, 
eliminando las repeticiones adicionales

--}

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:y:xs) | chequearRepeticion (x:y:xs) = x:eliminarRepetidos (y:xs)
                           | otherwise= eliminarRepetidos (y:xs)

chequearRepeticion :: (Eq t) => [t] -> Bool
chequearRepeticion [x] = True
chequearRepeticion [] =False
chequearRepeticion (x:y:xs) | x/=y = chequearRepeticion (x:xs)
                            | otherwise = False
----------------------------------------------------------------------EL CODIGO DE ACA ARRIBA ME DESORDENA LA LISTA


eliminarRepetidos2 :: (Eq t) => [t] -> [t]
eliminarRepetidos2  [] = []
eliminarRepetidos2 s = head s : eliminarRepetidos2  (quitarTodos (head s) s)

eliminarRepetidos1 :: (Eq t) => [t] -> [t]
eliminarRepetidos1  [] = []
eliminarRepetidos1 (x:xs)= x:eliminarRepetidos1(quitarTodos x xs)
-------------------------------------------------------------------ELIMINAR REPE 1 ES EL GOD






{--8. mismosElementos :: (Eq t) => [t] -> [t] -> Bool, que dadas dos listas devuelve verdadero sı y solamente sı
ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones, es decir:

problema mismosElementos (s: seq⟨T⟩, r: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ todo elemento de s pertenece r y viceversa}
--}


--mismosElementos (x:xs) (y:ys) = eliminarRepetidos1 (x:xs) == eliminarRepetidos1 (y:ys) --Pero esto no anda si estan desordenadas

mismosElementosIZQDER ::(Eq t) => [t] -> [t] -> Bool
mismosElementosIZQDER [] _ = True
mismosElementosIZQDER s r | pertenece (head s) r = mismosElementosIZQDER (tail s) r -- me dice si los elementos de la lista de la izquierda perteneccen a la de la derecha
                          | otherwise = False

mismosElementosPosta ::(Eq t) => [t] -> [t] -> Bool
mismosElementosPosta s r = mismosElementosIZQDER s r && mismosElementosIZQDER r s


{--9. capicua :: (Eq t) => [t] -> Bool segun la siguiente especificacion:

problema capicua (s: seq⟨T⟩) : B {
        requiere: { True }
        asegura: { (resultado = true) ↔ (s = reverso(s)) }
}
--}

capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua t = t == reverso t



{--)$$$$$$$$$$$$$$$$$$$$$$$$$$     EJERCICIO 3)    $$$$$$$$$$$$$$$$$$$$$$$$$$

1. sumatoria :: [Integer] -> Integer segun la siguiente especificacion:
problema sumatoria (s: seq⟨Z⟩) : Z {
        requiere: { True }
        asegura: { resultado =LA SUMATORIA DE LOS ELEMENTOS DE S , OSEA, SUM DE i=0 HASTA N = MODULO(S) - 1

--}

sumatoria :: [Integer] -> Integer
sumatoria [] = 0 
sumatoria (x:y:xs)= x + sumatoria (y:xs) -- por que funcion esto si supuestamente (x:y:xs) significa la lsita de al menos 2 elementos?


{--2. productoria :: [Integer] -> Integer segun la siguiente especificaci´on:
problema productoria (s: seq⟨Z⟩) : Z {
        requiere: { T rue }
        asegura: { resultado =
--}

productoria :: [Integer] -> Integer 
productoria []= 1
productoria (x:xs) = x * productoria (xs)


{--4. sumarN :: Integer -> [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {|resultado| = |s| ∧ cada posicion de resultado contiene el valor que hay en esa posici´on en s sumado
n }
--}
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ []= []
sumarN 0 l = l 
sumarN n (x:xs) = (x+n) : sumarN n xs

{--5. sumarElPrimero :: [Integer] -> [Integer] segun la siguiente especificaci´on:
problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN(s[0], s) }
}
Por ejemplo sumarElPrimero [1,2,3] da [2,3,4]
--}
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

{--6. sumarElUltimo :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN(s[|s| − 1], s) }
}
--}
sumarElUltimo :: [Integer] -> [Integer] 
sumarElUltimo [] = []
sumarElUltimo (x:xs) = (x + ultimo (x:xs)) : sumarElUltimo xs


{--7. pares :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {resultado s´olo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
}
Por ejemplo pares [1,2,3,5,8,2] da [2,8,2]
--}
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | even x = x:pares xs
             | otherwise = pares xs

{--8. multiplosDeN :: Integer -> [Integer] -> [Integer] que dado un numero n y una lista xs, devuelve una lista
con los elementos de xs m´ultiplos de n.
--}

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x: multiplosDeN n xs 
                      | otherwise = multiplosDeN n xs  

{--9. ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente.
--}
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:y:xs) | decimeSiEsElMasChico(x:y:xs) = x: ordenar (y:xs)
                 | otherwise = ordenar (y:xs)  -- NO LO HICE
--
decimeSiEsElMasChico :: [Integer] -> Bool
decimeSiEsElMasChico [] = True
decimeSiEsElMasChico [x] = True
decimeSiEsElMasChico (x:y:xs) = x<y && decimeSiEsElMasChico (x:xs)



--)$$$$$$$$$$$$$$$$$$$$$$$$$$     EJERCICIO 4)    $$$$$$$$$$$$$$$$$$$$$$$$$$--
{-- Definir las siguientes funciones sobre listas de caracteres, interpretando una palabra como una secuencia de
caracteres sin blancos:
--}


{--sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la primera
lista por un solo blanco en la lista resultado.

text= 'h','o','l','a'
--}
sacarBlancosRepetidos :: [Char] ->[Char] 
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x]=[x]
sacarBlancosRepetidos (x:y:xs) | x == y && x == ' ' = sacarBlancosRepetidos (y:xs)
                               | otherwise = x:sacarBlancosRepetidos (y:xs)

--2. contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que tiene.

contarPalabras :: [Char] -> Integer
contarPalabras [x] = 1
contarPalabras []= 0
contarPalabras l | head(tail(sacarBlancosRepetidos l )) == ' ' && head(sacarBlancosRepetidos l) /=' ' = 1+contarPalabras(tail l) --necesitoq  no se considere el espacio final
                 | otherwise = contarPalabras (tail l)


-- LA IDEA ESTA BIEN PERO PUEDE SER MEJOR




contarPalabras2:: [Char] -> Integer
contarPalabras2 [] =  0
contarPalabras2 l = cuentePalabras( sacarEspacioInicioFin (sacarBlancosRepetidos l ))

sacarEspacioInicioFin :: [Char] -> [Char]
sacarEspacioInicioFin []= []
sacarEspacioInicioFin[' ']=[]
sacarEspacioInicioFin (x:xs) | x == ' '= sacarEspacioFin xs 
                             | otherwise = x: sacarEspacioFin xs    


sacarEspacioFin :: [Char] -> [Char] 
sacarEspacioFin [] = []
sacarEspacioFin [x] | x==' ' = []
sacarEspacioFin (x:xs) = x:sacarEspacioFin xs



cuentePalabras :: [Char] -> Integer
cuentePalabras [] = 0
cuentePalabras [x] = 1
cuentePalabras (x:xs) | x == ' ' = 1 + cuentePalabras xs 
                      | otherwise = cuentePalabras xs  


-- palabras :: [Char] -> [[Char]], que dada una lista arma una nueva lista con las palabras de la lista original
palabras :: [Char] -> [[Char]]
palabras [] = []

