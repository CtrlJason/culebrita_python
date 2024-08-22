#Modulos
import mundo, obj_comida, vista_juego, time, keyboard, winsound # Para pausar el tiempo de ejecucion de una seccion del codigo
from pathlib import Path
# Variables
jugador = mundo.mapa_culebrita.tablero
#Sonidos
ruta_sonido_comer = Path(__file__).parent/"sonidos/comer.wav" # En este caso se utiliza Path(__file__).parent/ para obtener la ubicacion de un archivo y viajar entre carpetas atravez de un "/"
ruta_sonido_perder = Path(__file__).parent/"sonidos/perder.wav"
class Personaje():
    def __init__(self, sprite):
        self.sprite = sprite
    #---------------------------------------------------------------------#    
    def movimiento(self):
        pasos_x = 2
        pasos_y = 4
        ultima_tecla = "d"
        count = 0
        puntos = 0
        count_s = 1
        puntos_anteriores = 0
        list_pos_x = []
        list_pos_y = []
        #---------------------------------------------------------------------#
        while True:
            #---------------------------------------------------------------------#
            # Se sobre escriben los cuadros blancos de la serpiente con azules desde su ultima posicion
            if puntos == 0: # [CONDUNCIONAL 1]
                # se establece el largo de la serpiente inicial al comer la fruta
                list_pos_y.append(pasos_y)
                list_pos_x.append(pasos_x)
                if count > 0: # [CONDUNCIONAL 2]
                    list_pos_x.pop(0)
                    list_pos_y.pop(0)
                w_line = jugador[pasos_y][pasos_x] = "🟦"
            #---------------------------------------------------------------------#
            if puntos != puntos_anteriores: # Este condicional se ejecuta unicamente cuando el jugador alla obtenido un punto # [CONDUNCIONAL 3]
                list_pos_x.append(pasos_x)
                list_pos_y.append(pasos_y)
            #---------------------------------------------------------------------#
            if puntos > 0: # [CONDUNCIONAL 4]
                # se agregan nuevas posiciones y se eliminan las anteriores
                list_pos_x.append(pasos_x)
                list_pos_y.append(pasos_y)
                list_pos_x.pop(0)
                list_pos_y.pop(0)
                w_line = jugador[list_pos_y[0]][list_pos_x[0]] = "🟦"
                pint = jugador[list_pos_y[-1]][list_pos_x[-1]] = "🟨"
                pint
                w_line
            #---------------------------------------------------------------------#
            # guardamos el puntaje actual del jugador para que no se ejecute el condicional [CONDUNCIONAL 3]
            puntos_anteriores = puntos
            count += 1
            #---------------------------------------------------------------------#
            if keyboard.is_pressed("w") and not keyboard.is_pressed("s") and not ultima_tecla == "s": # Movimiento arriba
                pasos_y -= 1
                pasos_x += 0
                ultima_tecla = "w"
                jugador[pasos_y][pasos_x] = culebrita.sprite
            elif keyboard.is_pressed("d") and not keyboard.is_pressed("a") and not ultima_tecla == "a": # Movimiento derecha
                ultima_tecla = "d"
                pasos_y -= 0
                pasos_x += 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
            elif keyboard.is_pressed("s") and not keyboard.is_pressed("w") and not ultima_tecla == "w": # Movimiento abajo
                pasos_y += 1
                pasos_x += 0
                ultima_tecla = "s"
                jugador[pasos_y][pasos_x] = culebrita.sprite
            elif keyboard.is_pressed("a") and not keyboard.is_pressed("d") and not ultima_tecla == "d": # Movimiento izquierda
                pasos_y += 0
                pasos_x -= 1
                ultima_tecla = "a"
                jugador[pasos_y][pasos_x] = culebrita.sprite
            #---------------------------------------------------------------------#
            # Verificador de ultima tecla presionada    
            if ultima_tecla == "w" and not keyboard.is_pressed("w"): # Movimiento arriba
                pasos_x += 0
                pasos_y -= 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
            elif ultima_tecla == "d" and not keyboard.is_pressed("d"): # Movimiento derecha
                pasos_y -= 0
                pasos_x += 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
            elif ultima_tecla == "s" and not keyboard.is_pressed("s"): # Movimiento abajo
                pasos_y += 1
                pasos_x += 0
                jugador[pasos_y][pasos_x] = culebrita.sprite
            elif ultima_tecla == "a" and not keyboard.is_pressed("a"): # Movimiento izquierda
                pasos_y += 0
                pasos_x -= 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
            #---------------------------------------------------------------------#
            if pasos_y == 8 or pasos_y == 0 or pasos_x == 8 or pasos_x == 0:
                winsound.PlaySound(ruta_sonido_perder, winsound.SND_FILENAME) # Para ejecutar o iniciar el sonido
                print("\nHas perdido\n")
                jugador[pasos_y][pasos_x] = "🟥"
                break
            #---------------------------------------------------------------------#
            if (pasos_y, pasos_x) in zip(list_pos_y, list_pos_x):
                    print("\nHas perdido\n")
                    break
            #---------------------------------------------------------------------#
            posicion = [[pasos_y],[pasos_x]]
            posicion2 = obj_comida.manzana.guardado()
            #---------------------------------------------------------------------#
            # Verificador de posicion de jugador y fruta
            if posicion == posicion2:
                winsound.PlaySound(ruta_sonido_comer, winsound.SND_FILENAME) # Para ejecutar o iniciar el sonido
                obj_comida.manzana.posicion_fruta()
                puntos += 1
                count_s += 1
            #---------------------------------------------------------------------#
            vista_juego.vista()
            # Puntaje
            print(f"Puntos: {puntos}")
            time.sleep(0.34)
        
culebrita = Personaje(sprite="🟧")