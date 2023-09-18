import Test.HUnit
import Solucion
import Solucion (relacionesValidas, amigosDe)



{-problema relacionesValidas (relaciones: seq⟨String × String⟩) : Bool {
    requiere: {True}
    asegura: {(res = true) ↔ no hay tuplas en relaciones con ambas componentes iguales ni tuplas repetidas (sin considerar
                    el orden)}
}-}

{-problema personas (relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
    requiere: {relacionesV alidas(relaciones)}
    asegura: {resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en cualquiera de las dos
            posiciones, sin repetir}
}-}

{-problema amigosDe (persona: String, relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
    requiere: {relacionesV alidas(relaciones)}
    asegura: {resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en las que alguna de las
            componentes es persona}
}-}


{-problema personaConMasAmigos (relaciones: seq⟨String × String⟩) : String {
    requiere: {relaciones no vac´ıa}
    requiere: {relacionesV alidas(relaciones)}
    asegura: {resu es el Strings que aparece mas veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
}-}



run1 = runTestTT testrelacionesValidas

testrelacionesValidas = test [
                " relacionesValidas: una sola correcta" ~: (relacionesValidas [("PERON","ABIGAIL")]) ~?= True,
                " relacionesValidas: una sola incorrecta" ~: (relacionesValidas [relacion1_1]) ~?= False,
                "Relvalida: todo correcto" ~:(relacionesValidas [("Gian","Souto"),("Augusto","Kun Aguero"),("Pato Bullrich","Peron")]) ~?=True,
                "RELinvalida: HAY UNA SIMETRICA" ~:(relacionesValidas [("Gian","Souto"),("Souto","Gian"),("Pato Bullrich","Peron")]) ~?=False,
                "REL invalidad: HAY 2 ELEMENTOS IGUALES EN UNA TUPLA" ~:(relacionesValidas [("PUPA","Souto"),("Gian","Gian"),("Pato Bullrich","Peron")]) ~?=False,
                "REL INVALIDAAAA: HAY 2 TUPLAS REPETIDASSSS"~:(relacionesValidas [("PUPA","Souto"),("Gian","Gian"),("Pato Bullrich","Peron")]) ~?=False,
                "REL VALDIA: RESPUESTA VACIA" ~:(relacionesValidas []) ~?=True
                ]


run2 = runTestTT testpersonas
testpersonas= test [
                    " personas: una sola relacion, 2 personas" ~: (sonIguales (personas [relacion1_2])  [usuario1, usuario2]) ~?= True,
                    " personas: dos relaciones, 3 personas" ~: (sonIguales (personas [relacion1_2, relacion1_3]) [usuario1, usuario2, usuario3]) ~?= True,
                    "personas: 3 relaciones, 6 personas" ~: sonIguales (personas [("Gian","Souto"),("Augusto","Kun Aguero"),("Pato Bullrich","Peron")])
                                                             ["Gian","Souto","Augusto","Kun Aguero","Pato Bullrich","Peron"] ~?= True,
                    "personas: 3 relaciones,4 personas" ~: sonIguales (personas [("Gian","Souto"),("Gian","Kun Aguero"),("Gian","Peron")])
                                                             ["Gian","Souto","Kun Aguero","Peron", "Peron"] ~?= False
                    


                     ]

run3 = runTestTT testamigosDe
testamigosDe= test [
                    " amigosDe: una sola relacion, 1 solo amigo" ~: amigosDe usuario1 [relacion1_2]  ~?= [usuario2],
                    " amigosDe: 3 relaciones, 0 amigos" ~: amigosDe "Cristina" [("Gian","Souto"),("Augusto","Kun Aguero"),
                        ("Pato Bullrich","Peron")] ~?= [],
                    "amigosDe: 3 relaciones, 1 amigo " ~: amigosDe "Gian" [("Gian","Souto"),("Augusto","Kun Aguero"),
                        ("Pato Bullrich","Peron")] ~?= ["Souto"],
                    "amigosDe: 0 relaciones, 0 amigos" ~: amigosDe "Gian" [] ~?= []       
                     ]





-- Ejemplos

usuario1 = "Juan"
usuario2 = "Natalia"
usuario3 = "Pedro"

relacion1_2 = (usuario1, usuario2)
relacion1_1 = (usuario1, usuario1)
relacion1_3 = (usuario1, usuario3)


-- FUNCIONES PARA TESTING, NO BORRAR
-- expectAny permite saber si el elemenot que devuelve la función es alguno de los esperados
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- sonIguales permite ver que dos listas sean iguales si no importa el orden
quitar :: (Eq t) => t -> [t] -> [t]
-- requiere x pertenece a y
quitar x (y:ys)
 | x == y = ys
 | otherwise = y : quitar x ys

incluido :: (Eq t) => [t] -> [t] -> Bool
incluido [] l = True
incluido (x:c) l = elem x l && incluido c (quitar x l)

sonIguales :: (Eq t) => [t] -> [t] -> Bool
sonIguales xs ys = incluido xs ys && incluido ys xs