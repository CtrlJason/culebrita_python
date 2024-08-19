#Librerias o modulos
import mundo, random # libreria de numeros aleatorios

# Numero aleatorio en el tablero para que aparezca la fruta

# Alimento del jugador que lo hara crecer
class Comida_personaje():
    def __init__(self, comida):
        self.comida = comida
        
# Funcion para verificar si la manzana existe o no en el tablero para crearla nuevamente
    def posicion_fruta(self):
        columnas = random.randint(1,7)
        filas = random.randint(1,7)
        fruta = mundo.mapa_culebrita.tablero[columnas][filas] = manzana.comida
        fruta
manzana = Comida_personaje(comida="🍎")