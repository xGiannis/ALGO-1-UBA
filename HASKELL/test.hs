import Foreign.C (eSHUTDOWN)
--EJ 1) problema f (n: Z) : Z {
--requiere: {n = 1 ∨ n = 4 ∨ n = 16}
--asegura: {(n = 1 → result = 8) ∧ (n = 4 → result = 131) ∧ (n = 16 → result = 16)}
--}

f :: Integer -> Integer
f x     | x==1 = 8
        |x==4 = 131
        |x==16 =16

--B)g(8) = 16
--g(16) = 4
--g(131) = 1
g :: Integer ->Integer
g 8=16
g  16=4
g  131=1


--c)  partir de las funciones definidas en los ´ıtems 1 y 2, implementar las funciones parciales h = f ◦ g y k = g ◦ f
h :: Integer ->Integer
h x | x==8 = f(g 8)
    | x==16 = f(g 16)
    | x==131 = f(g 131)

k :: Integer ->Integer
k x | x==1 = g(f 1)
    | x==4 = g(f 4)
    | x==16 = g(f 16)


-- #########################Ejercicio 2)#########################
--problema absoluto (y:Z):Z{
--  requiere: {True}
--  asegura: {Res es el valor absoluto de y}        
--}

absoluto :: Integer -> Integer
absoluto y | y>=0 =y
           | y<0 = -y


--b)
--{problema MaximoAbsoluto (x:Z),(y:Z):Z{
--          requiere: {True}
--          asegura: {Res devuelve el maximo
--                  valor entre los dos valores absolutos
--                  de x e y}
--}
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y | x==y =absoluto(x)
                   | absoluto(x) > absoluto(y) = absoluto(x)
                   | otherwise = absoluto(y)


--c)
--{problema maximo3 (x:Z),(y:Z),(a:Z):Z{
--          requiere: {True}
--          asegura: {Res devuelve el maximo
--                  entre x,y,a}
--}

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y a   |x>=y && x>=a  =x
                |y>=x && x>=a =y
                |a>=x && a>=y =a


--d)
--{problema algunoEs0 (x:R),(y:R):R{
--          requiere: {x e y deben ser racionales}
--          asegura: {Res devuelve True si alguno es 0,
--                    False de lo contrario}
--}

algunoEs0 :: Integer -> Integer -> Bool
algunoEs0 x y | x==0 || y==0 = True
              | otherwise = False

algunoes0Patter :: Integer -> Integer -> Bool
algunoes0Patter 0 _ = True
algunoes0Patter _ 0 = True
--algunoes0Patter 0 0 = True
algunoes0Patter x y = False

--e)
--{problema ambosSon0 (x:R),(y:R):R{
--          requiere: {x e y deben ser racionales}
--          asegura: {Res devuelve True si ambos es 0,
--                    False de lo contrario}
--}

ambosSon0 :: Integer -> Integer -> Bool
ambosSon0 x y | x==0 && y==0 = True
              | otherwise = False

ambosSon0Pattern :: Integer -> Integer -> Bool
ambosSon0Pattern 0 0 = True
ambosSon0Pattern x y = False

--f)
--{problema mismoIntevalo (x:R),(y:R):R{
--          requiere: {True}
--          asegura: {Res devuelve True si ambos numeros estan
--                      en el mimso intervalo}
--}

mismoIntervalo :: Integer -> Integer -> Bool
mismoIntervalo x y | x<=3 && y<=3  = True
                   | x>7 && y>7 = True
                   | x>3 && y>3 && x<=7 && y<=7 = True
                   | otherwise = False

mismoIntervalo2 :: Integer -> Integer -> Bool
mismoIntervalo2 x y | x<=3 && y<=3  || x>7 && y>7 || x>3 && y>3 && x<=7 && y<=7 = True
                    | otherwise = False

--g)
--{problema sumaDistintos (x:Z),(y:Z),(a:Z):Z{
--          requiere: {True}
--          asegura: {Res devuelve la suma de las variables
--                      no repetidas entregadas (3)}
--          asegura: {Si las 3 variables son iguales, Res devuelve x}
--}

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y a |x==y && a==x = x  --               ####div (x + y + a)  3 == x = x######### <---Esta funcion serviria si estoy tratando con float. 
--                                                                                  asumo q para un problema de enteros, seria complicarse decidir lo anterior.
                    |x==y = x+a
                    |x==a = x+y 
                    |y==a = x+y
                    |otherwise = x+y+a


--h)
--{problema esMultiploDe (x:Z),(y:Z):Z{
--          requiere: {x e y tienen que ser positivos}
--          asegura: {Res devuelve True si x es multiplo de y ----> x=yk con k perteneciente a naturales}
--          
--}

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y | y==0 = False 
                 | mod x y ==0 = True
                 | otherwise = False 

--i)
--{problema digitoUnidades (x:Z):Z{
--          requiere: {x tiene que ser positivos}
--          asegura: {Res devuelve el digito de unidades}
--          
--}

digitoUnidades :: Integer -> Integer
digitoUnidades x |x<10 =x 
                 |x>10 = x - ((div x 10) * 10)

{--j) digitoDecenas: dado un numero natural, extrae su dıgito de las decenas.
{
problema digitoDecenas (x:Z):Z {
        requiere: {x tiene q ser positivo}
        asegura: {devolver el digito de decenas si lo tiene}

--}


digitoDecenas :: Integer -> Integer
digitoDecenas x | x<10 = 0
                | otherwise = div (mod x 100) 10



{-- #########################Ejercicio 3)#########################
Ejercicio 3. Implementar una funcion estanRelacionados :: Integer ->Integer ->Bool
problema estanRelacionados (a:Z, b:Z) : Bool {
requiere: {a != 0 ∧ b != 0}
asegura: {(res = true) ↔ a ∗ a + a ∗ b ∗ k = 0 para algun k ∈ Z con k != 0)}
}
--}

estanRelacionados :: Integer-> Integer-> Bool
estanRelacionados x y | mod x y==0 = True       -- El problema es ver si x no es coprimo con y. 
                      | otherwise = False

-- #########################Ejercicio 4)#########################

{--
a) probelma prdInt (x:seq<R>), (y:seq<R>): R {
            requiere: {True}
            asegura: {res sera el producto interno entre x,y}
--}
prdInt :: (Float, Float) -> (Float, Float) -> Float
prdInt x y =  fst x * fst y + snd x * snd y

{-- b)
problema todoMenor (x:seq<R>), (y:seq<R>) : Bool{
        requiere:{True}
        asegura:{res devuelve True si cada coord de la primera tupla
                es mayor q la de la segunda}
--}

todoMenor :: (Float,Float) -> (Float,Float) -> Bool
todoMenor x y = fst x < fst y && snd x < snd y  

{-- c)
problema distanciaPuntos (x:seq<R>), (y:seq<R>) : R{
        requiere:{True}
        asegura:{res devuelve la dist entre x e y}
--}
distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float  
distanciaPuntos x y = sqrt((fst y - fst x)**2 + (snd y-snd x)**2)

{-- d)
problema sumaTerna (x:seq<Z>): Z{
        requiere:{True}
        asegura:{res devuelve la sumatoria de los elementos de la terna x}
--}
-- %%%%%%%%%%%%%%BUSCADOR DE TERNAS%%%%%%%%%%%%%%%%%
priTerna :: (Integer, Integer, Integer) -> Integer
priTerna (x,_,_) = x

segTerna :: (Integer, Integer, Integer) -> Integer
segTerna (_,x,_) = x 


terTerna :: (Integer, Integer, Integer) -> Integer
terTerna (_,_,x) = x    
-- %%%%%%%%%%%%%%BUSCADOR DE TERNAS%%%%%%%%%%%%%%%%%

sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (a,b,c) = a+b+c-- ? necesito una funcionq  me busque el tercero...

{-- e)
problema sumarSoloMultiplos (terna:seq<Z>), (n:Z): Z{
        requiere:{n > 0}
        asegura:{res devuelve la sumatoria de los elementos de la terna x multiplos de n}
--}

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n = a -a*((mod a n) ^ 0 )  + b- b* (mod b n)^0 + c-c*(mod c n)^0          -- hay q escribir linea para cada caso, me bajo. 

{-- e)
problema posPrimerPar (terna:seq<Z>): Z{
        requiere:{debe haber algun numero par en terna}
        asegura:{res devuelve 4 si todos los elementos de terna son pares}
        asegura:{res devuelve la posicion del primer numero par}
--}
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a,b,c) | even a && even b && even c = 4
                     | even a = 0
                     | even b = 1
                     | even c = 2

{-- e)
problema crearPar (x:a), (y:b): seq<a,b>{
        requiere:{True}
        asegura:{res devuelve una tupla formada por x e y}
--}

crearPar :: a->b->(a,b)
crearPar x y = (x,y)

{-- e)
problema invertir (tupla:seq<a,b>): seq<a,b>{
        requiere:{True}
        asegura:{res devuelve tupla con el orden de sus elmentos invertidos}
--}                 

invertir :: (a,b) -> (b,a)
invertir (x,y) = (y,x)

-- #########################Ejercicio 5)#########################

