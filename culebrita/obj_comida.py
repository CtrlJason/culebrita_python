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
        posicion_anterior = mundo.mapa_culebrita.tablero[columnas][filas]
        fruta = mundo.mapa_culebrita.tablero[columnas][filas] = manzana.comida
        # guarda la posicion actual de la fruta para su posterior comparacion
        print(posicion_anterior)
        # comparamos la ubicacion de la posicion random de la fruta, si esta en la misma posicion que el jugador la fruta se imprime en un lugar diferente
        if posicion_anterior == "🟦":
            self.posicion = [[columnas],[filas]] # Se guarda la posicion actual para su posterior utilizacion
            print("si se cumple la opcion 1")
            fruta
        elif posicion_anterior == "⬜":
            jugador = mundo.mapa_culebrita.tablero[columnas][filas] = "⬜" # Marca la posicion de la manzana que se sobre ponga en el jugador
            jugador
            manzana.posicion_fruta()
            print("si se cumple la opcion 2")
        # manzana.comprobacion_espacios()

    def guardado(self):
        self.posicion
        return self.posicion
    
    def comprobacion_espacios(self):
        pass
manzana = Comida_personaje(comida="🍎")
print()