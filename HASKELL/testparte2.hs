{--
#########################Ejercicio 5)#########################
problema todosMenores ((n1,n2,n3) : Z X Z X Z) : Bool {
        requiere: {True}
        asegura: {(res = true) ↔ ((f(n1) > g(n1)) ∧ (f(n2) > g(n2)) ∧ (f(n3) > g(n3))))}

problema f (n: Z) : Z {
    requiere: {T rue}
    asegura: {(n ≤ 7 → res = n^2) ∧ (n > 7 → res = 2n − 1)}

problema g (n: Z) : Z {
        requiere: {True}
        asegura: {Si n es un numero par, entonces res = n/2, en caso contrario, res = 3n + 1}
--}

todosMenores :: (Integer, Integer, Integer) ->Bool
todosMenores (n1, n2, n3) = f n1 > g n1 && f n2 > g n2 && f n3 > g n3


f :: Integer -> Integer
f n | n<= 7 = n^2
    | n > 7 = 2*n-1

g :: Integer -> Integer
g n | even n = n `div` 2 
    | otherwise = 3*n + 1 

-- #########################Ejercicio 6)#########################


{--
problema bisiesto (anio: Z) : Bool {
        requiere: {True}
        asegura: {res = false ↔ anio no es multiplo de 4 o anio es multiplo de 100 pero no de 400}
--}

bisiesto :: Integer -> Bool
bisiesto anio | mod anio 4 /= 0 = False
              | mod anio 100 == 0 && mod anio 400 /= 0 = False
              | otherwise = True

{--7)
problema distanciaManhattan (p: seq<RxRxR>), (q:seq<RxRxR>) : R{
        requiere: {True}
        asegura: {res = sumatoria hasta 2 desde i=0 del 
                    valor absoluto entre la diferencia de
                    p indice i, q inidce i}
--}

distanciaManhattan:: (Float, Float, Float) ->(Float, Float, Float) ->Float
distanciaManhattan (a,b,c) (d,e,f) = sqrt((a-d)**2) + sqrt((b-e)**2) + sqrt((c-f)**2)

{--8)
problema comparar (a:Z), (b:Z) : R{
        requiere: {True}
        asegura: {res = 1 si y solo si sumaUltimosDosDigitos(a)<sumaUltimosDosDigitos(b)}
        asegura: {res = -1 si y solo si suma UltimosDosDigitos(a) > sumaUltimosDosDigitos(b)}
        asegura: {res = 0 si y solo si sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b)}
}
problema sumaUltimosDosDigitos (x: Z) : Z {
    requiere: {True}
    asegura: {res = (x mod 10) + ((x/10) mod 10)}
}              
--}
comparar :: Integer ->Integer ->Integer
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10

{--9)

a) 
f1 :: Float -> Float
f1 n | n == 0 = 1
     | otherwise = 0
--------------------> dado un n real, f1 devuelve 1 si n=0 o 0 si n!=0.

---especificacion--->problema f1 (n:R):R{
                            requiere: {True}
                            asegura: {res = 1 si n es igual a 0 o 0 si n es !=0}
}

b)
f2 :: Float -> Float
f2 n | n == 1 = 15
     | n == -1 = -15    
--------------------> dado un n real, f1 devuelve 15 si n=1 o -15 si n=-1

---especificacion--->problema f2 (n:R):R{
                            requiere: {n tiene q ser 1 o -1}
                            asegura: {res=15 si n=1}        ##########PREGUNTAR SI METER TODO EN UN ASEGURA####
                            asegura: {res=-15 si n=-1}
}

c)
f3 :: Float -> Float
f3 n | n <= 9 = 7
     | n >= 3 = 5
--------------------> {dado un n real, f3 devuelve 7 si n es menor o igual a 9. pero si n es mayor o igual a 3, devuelve 5. 
                      esto es lo q dice la funcion visto a ojo. Sin embargo, la funcion verdaderamente hace lo siguiente>:
                      si n es menor o igual q 9, devuelve 7. si n es mayor o igual q 3, vemnos q tambien es menor o igual q 9. 
                      Luego, como la premisa n menor o igual q 9 esta primero, devolvera 7. f3 solo devuelve 5 si n es mayor que 9,
                      ya que en ese caso n no es mayor o igual que 9 y n es mayor o igual que 3.}

---especificacion---> problema f3 (n:Z): Z:{
                            requiere: {True}
                            asegura: {res=7 si n<=9}
                            asegura: {res=5 si n>3}
}

d)
f4 :: Float -> Float -> Float
f4 x y = ( x + y )/2
--------------------> {dado dos numeros reales x y, f4 la division entre 2 de la suma de estos.}

---especificacion---> problema f4 (x:R), (y:R): R:{
                            requiere:{True}
                            asegura:{res= ((x+y)/2)}
}


e)
f5 :: ( Float , Float ) -> Float
f5 (x , y ) = ( x + y )/2
--------------------> {dado una tupla compuesta por dos numeros reales x y, f4 devuelve la division entre 2 de la suma de x y}

---especificacion---> problema f5 (tupla:(R,R)): R{
                            requiere:{True}
                            asegura:{res= ((tupla_0+tupla_1)/2)}                      
}

f)
f6 :: Float -> Int -> Bool
f6 a b = truncate a == b
-------------------->{ dado un a real y un b entero, f6 toma a y lo redondea al entero mas cercano a 0. Luego se fija si a redondeado es igual a b}

---especificacion---> problema f6 (a:R), (b:Z): Bool{
                            requiere:{True}
                            asegura:{devuelve si es cierto que b y el resultado de redondear a para abajo son iguales}
}

--}
f6 :: Float -> Int -> Bool
f6 a b = truncate a == b

