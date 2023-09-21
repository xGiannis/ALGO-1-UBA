import Test.HUnit
 -- USADO COMO BLOC DE NOTAS, EL CODIGO DE ACA NO SIRVE SI NO MAS PARA ESCRIBIR CUALQUIER COSA
  -- USADO COMO BLOC DE NOTAS, EL CODIGO DE ACA NO SIRVE SI NO MAS PARA ESCRIBIR CUALQUIER COSA
   -- USADO COMO BLOC DE NOTAS, EL CODIGO DE ACA NO SIRVE SI NO MAS PARA ESCRIBIR CUALQUIER COSA
    -- USADO COMO BLOC DE NOTAS, EL CODIGO DE ACA NO SIRVE SI NO MAS PARA ESCRIBIR CUALQUIER COSA
     -- USADO COMO BLOC DE NOTAS, EL CODIGO DE ACA NO SIRVE SI NO MAS PARA ESCRIBIR CUALQUIER COSA
      -- USADO COMO BLOC DE NOTAS, EL CODIGO DE ACA NO SIRVE SI NO MAS PARA ESCRIBIR CUALQUIER COSA
       -- USADO COMO BLOC DE NOTAS, EL CODIGO DE ACA NO SIRVE SI NO MAS PARA ESCRIBIR CUALQUIER COSA
run = runTestTT tests

{-problema relacionesValidas (relaciones: seq⟨String × String⟩) : Bool {
    requiere: {True}
    asegura: {(res = true) ↔ no hay tuplas en relaciones con ambas componentes iguales ni tuplas repetidas (sin considerar
el orden)}
}-} --VEO Q LA LISTA VACIA ES TRUE.


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




tests = test ["relaciones vacias"~: (relacionesValidas[])~?= True 
              "l elem mal"~: (relacionesValidas[("A","A")])
              "l elem bien"~: (relacionesValidas[("A","B")])


run2 = runTestTT testpersonas
testpersonas= test [
                    " personas: una sola relacion, 2 personas" ~: (sonIguales (personas [relacion1_2])  [usuario1, usuario2]) ~?= True,
                    " personas: dos relaciones, 3 personas" ~: (sonIguales (personas [relacion1_2, relacion1_3]) [usuario1, usuario2, usuario3]) ~?= True
                    
                     ]

run3 = runTestTT testamigosDe
testamigosDe= test [
                    " amigosDe: una sola relacion, 1 solo amigo" ~: (amigosDe usuario1 [relacion1_2] ) ~?= [usuario2]
                    
                     ]

run4 = runTestTT testpersonaConMasAmigos
personaConMasAmigos= test[
                    " personaConMasAmigos: 2 relaciones, 1 solo max" ~: (personaConMasAmigos [relacion1_2, relacion1_3]) ~?= usuario1
                    
                     ]
