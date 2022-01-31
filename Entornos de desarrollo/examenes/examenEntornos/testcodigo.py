import unittest
import codigo

class testcodigo(unittest.TestCase):
    def test_no_hay_argumentos_devuelve_cero(self):
        respuesta = codigo.sumar('')
        self.assertEqual(respuesta, 0)

    def test_lista_enteros_floats_devuelve_suma(self):
        respuesta = codigo.sumar(['-5','8.6','-2'])
        self.assertEqual(respuesta,0.6)

    def test_cadena_de_texto_devuelve_cero(self):
        respuesta = codigo.sumar('holi')
        self.assertEqual(respuesta, 0)

    def test_objetos_no_numericos_devuelve_cero(self):
        respuesta = codigo.sumar('a','f')
        self.assertEqual(respuesta, 0)
        
    def test_numeros_complejos_devuelve_cero(self):
        respuesta = codigo.sumar(4j)
        self.assertEqual(respuesta, 0)

