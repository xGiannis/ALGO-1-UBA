--oioi
module Solucion where
--VAMOS A HACER Q RELACION SEA UN COMPORTAMIENTO A LO RED SOCIAL
--DONDE UN FOLLOW A OTRO (UNO,OTRO) PERO NO HAYA NINGUN CASO 
--SIMETRICO (OTRO,UNO) NI IGUALES!!!(UNO,UNO).

{-problema relacionesValidas (relaciones: seq⟨String × String⟩) : Bool {
    requiere: {True}
    asegura: {(res = true) ↔ no hay tuplas en relaciones con ambas componentes iguales ni tuplas repetidas (sin considerar
                el orden)}
}-}


relacionesValidas :: [(String,String)] -> Bool --[(Char,Char)]  es relaciones
relacionesValidas [] = True
relacionesValidas (r1:xs) = elemDiferentes (r1:xs) && todasTuplasDif (r1:xs) --TENGOQ  VER Q NO HAYA LSITAS SIMETRICVAS PARA TODASTUPASDIFF

elemDiferentes :: [(String,String)] -> Bool
elemDiferentes [] = True
elemDiferentes ((persona1,persona2):xs) = persona1 /= persona2 && elemDiferentes xs




todasTuplasDif :: [(String,String)] -> Bool 
todasTuplasDif [] = True
todasTuplasDif [(str1,str2)] = True
todasTuplasDif (r1:r2:xs) = (r1 /= r2 && todasTuplasDif (r2:xs)) && notSimetricas (r1:r2:xs)


notSimetricas :: [(String,String)] -> Bool 
notSimetricas [] = True
notSimetricas [x] =True
notSimetricas (r1:r2:xs) =  (r1 /= darVuelta r2 && notSimetricas (r1:xs)) == notSimetricas(r2:xs) 



darVuelta :: (t, t) -> (t, t)
darVuelta (e1,e2)=(e2,e1)


-- $$$$$$$$$$$$$$$$$$$$$$$$SIGUIENTE$$$$$$$$$$$$$$$$$$$$$
{-problema personas (relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
    requiere: {relacionesValidas(relaciones)}
    asegura: {resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en cualquiera de las dos
            posiciones, sin repetir}
}-}

personas :: [(String,String)] -> [String] --DEVUELVE GENTE DE LA RED SOCIAL
personas [] = []
personas (r1:xs) = sinRepetir (creacionDeLista(r1:xs))

creacionDeLista :: [(String,String)] -> [String]
creacionDeLista [] = []
creacionDeLista ((p1,p2):xs) = p1:p2:creacionDeLista xs

sinRepetir :: [String] -> [String]
sinRepetir [] = []
sinRepetir [x] = [x]
sinRepetir (p1:p2:xs) | diferenteATodosELem(p1:p2:xs)= p1: sinRepetir(p2:xs)
                      | otherwise = sinRepetir(p2:xs)  

diferenteATodosELem :: [String] -> Bool
diferenteATodosELem []=True
diferenteATodosELem [x]= True
diferenteATodosELem (p1:p2:xs) = p1/= p2 && diferenteATodosELem(p1:xs)


-- $$$$$$$$$$$$$$$$$$$$$$$$SIGUIENTE$$$$$$$$$$$$$$$$$$$$$
{-problema personas (relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
    requiere: {relacionesValidas(relaciones)}
    asegura: {resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en cualquiera de las dos
            posiciones, sin repetir}
}-}


{-problema amigosDe (persona: String, relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
    requiere: {relacionesValidas(relaciones)}
    asegura: {resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en las que alguna de las
            componentes es persona}
}-}

amigosDe :: String -> [(String,String)]  -> [String] --STRING ES PERSONA | [(String,String)] ES RELACIONES | [String] ES RES
amigosDe "" _ = []
amigosDe _ [] = [] --le puedo pasar cualquier lista de relaciones. dont matter
amigosDe persona (r1:xs) | persona `pertenece` r1 = (devolverNoPersona persona r1):amigosDe persona xs
                         | otherwise = amigosDe persona xs
 
pertenece :: String -> (String,String) -> Bool
pertenece persona (man1,man2) = persona == man1 || persona == man2

devolverNoPersona::String -> (String,String) -> String
devolverNoPersona persona (man1,man2) | persona == man1 = man2
                                      | otherwise = man1  

