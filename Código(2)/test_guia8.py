import unittest
from queue import Queue as Cola
from queue import LifoQueue as Pila
from pila_cola_diccionario import cantidadElementos, buscarElMaximo, agruparPorLongitud
from ejercicio_palabraMasFrecuente import laPalabraMasFrecuente

class Test_cantidadElementos(unittest.TestCase):

    # Tests para cantidadElementos de una cola
    def test_cantidadElementosColaVacia(self):
        c = Cola()
        resultado = cantidadElementos(c)
        self.assertEqual(resultado, 0)

    def test_cantidadElementosColaNoVacia(self):
        c = Cola()
        c.put(99)
        c.put(354)
        resultado = cantidadElementos(c)
        self.assertEqual(resultado, 2)

class Test_buscarElMaximo(unittest.TestCase):

    def test_buscarElMaximo_unElemento(self):
        p = Pila()
        p.put(3)
        resultado = buscarElMaximo(p)
        self.assertEqual(resultado, 3)

    def test_buscarElMaximo_todosIguales(self):
        p = Pila()
        p.put(3)
        p.put(3)
        p.put(3)
        resultado = buscarElMaximo(p)
        self.assertEqual(resultado, 3)

    def test_buscarElMaximo_creciente(self):
        p = Pila()
        p.put(3)
        p.put(4)
        p.put(5)
        resultado = buscarElMaximo(p)
        self.assertEqual(resultado, 5)

    def test_buscarElMaximo_decreciente(self):
        p = Pila()
        p.put(30)
        p.put(20)
        p.put(10)
        resultado = buscarElMaximo(p)
        self.assertEqual(resultado, 30)

class Test_agruparPorLongitud(unittest.TestCase):
    
    def test_agrupa_archivo_palabras(self):
        archivo = "archivo_palabras.txt"
        esperado = {4: 2, 2: 3, 3: 7, 6: 6, 7: 1, 8: 1, 1: 1}
        resultado = agruparPorLongitud(archivo)
        self.assertEqual(resultado, esperado)

class Test_palabraMasFrecuente(unittest.TestCase):
    
    def test_frecuente_archivo_palabras(self):
        archivo = "archivo_palabras.txt"
        esperado = ["que", "prueba", "una"]
        resultado = laPalabraMasFrecuente(archivo)
        self.assertIn(resultado, esperado)


if __name__ == '__main__':
    unittest.main()

