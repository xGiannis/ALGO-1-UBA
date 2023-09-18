{--
Ejercicio 5. Tıtulo: Frecuencia de bondis A Ciudad Universitaria (CU) llegan 8 lıneas de colectivos A=(28, 33, 34, 37, 45,
107, 160, 166).
 Con el fin de controlar la frecuencia diaria de cada una de ellas, un grupo de investigacion del Departamento de
Computacion instalo camaras y sistemas de reconocimiento de imagenes en el ingreso al predio. 
Durante cada dıa dicho sistema
identifica y registra cada colectivo que entra, almacenando la informacion de a que linea pertenece en una secuencia.

a)  Especificar el problema cantidadColectivosLinea() que a partir de la secuencia de colectivos que entran a CU, el numero de
una de las lıneas que entra a CU, y una secuencia que cumpla con la descripcion del sistema presentado, devuelva cuantos
colectivos de esa lınea ingresaron durante el dıa.

{problema cantidadColectivosLinea (s1:seq<Z>), (l:Z), (comb:seq<Z>) : Z{
            requiere:{comb debe tener como elementos s1 y l}     
            requiere:{l debe ser alguna de las 8 lineas de colectivo q entran}
            requiere:{s1 almacena cada colectivo que entra}
            asegura:{res va a devolver cantidad de ingresos de l segun s1 }


} 


b) Especificar el problema compararLineas() que a partir de los numeros de 2 lıneas y una secuencia que cumpla con la descripcion
del sistema presentado, devuelva cual de las dos lıneas tiene mejor frecuencia diaria (utilizar cantidadColectivosLinea())

problema compararLineas (bondi1:Z),(bondi2:Z),(s2:seq<Z>): seq<Z>:
            requiere: {bondi1 debe pertencer a A}
            requiere: {bondi2 debe pertencer a A}
            requiere: {s2 contiene a cantidadColectivosLinea(s1,bondi1,comb) y a cantidadColectivosLinea(s1,bondi2,comb)}
            asegura: {res devuelve el mayor entre los 2 elementos de s2/24 }



--}