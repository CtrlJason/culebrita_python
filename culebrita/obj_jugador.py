#Modulos
import mundo, obj_comida, vista_juego, time, keyboard # Para pausar el tiempo de ejecucion de una seccion del codigo
# Variables

jugador = mundo.mapa_culebrita.tablero
posicion_comida = obj_comida.manzana.posicion_fruta()
class Personaje():
    def __init__(self, sprite):
        self.sprite = sprite
        
    def movimiento(self):
        pasos_x = 2
        pasos_y = 4
        ultima_tecla = "d"
        while True:
            # Verificador de presion de tecla
            if keyboard.is_pressed("w") and not keyboard.is_pressed("s") and not ultima_tecla == "s": # Movimiento arriba
                pasos_y -= 1
                pasos_x += 0
                ultima_tecla = "w"
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y+1][pasos_x] = "🟦"
            elif keyboard.is_pressed("d") and not keyboard.is_pressed("a") and not ultima_tecla == "a": # Movimiento derecha
                pasos_y -= 0
                pasos_x += 1
                ultima_tecla = "d"
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y][pasos_x-1] = "🟦"
            elif keyboard.is_pressed("s") and not keyboard.is_pressed("w") and not ultima_tecla == "w": # Movimiento abajo
                pasos_y += 1
                pasos_x += 0
                ultima_tecla = "s"
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y-1][pasos_x] = "🟦"
            elif keyboard.is_pressed("a") and not keyboard.is_pressed("d") and not ultima_tecla == "d": # Movimiento izquierda
                pasos_y += 0
                pasos_x -= 1
                ultima_tecla = "a"
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y][pasos_x+1] = "🟦"
            # Verificador de ultima tecla presionada    
            if ultima_tecla == "w" and not keyboard.is_pressed("w"): # Movimiento arriba
                pasos_x += 0
                pasos_y -= 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y+1][pasos_x] = "🟦"
            elif ultima_tecla == "d" and not keyboard.is_pressed("d"): # Movimiento derecha
                pasos_y -= 0
                pasos_x += 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y][pasos_x-1] = "🟦"
            elif ultima_tecla == "s" and not keyboard.is_pressed("s"): # Movimiento abajo
                pasos_y += 1
                pasos_x += 0
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y-1][pasos_x] = "🟦"
            elif ultima_tecla == "a" and not keyboard.is_pressed("a"): # Movimiento izquierda
                pasos_y += 0
                pasos_x -= 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y][pasos_x+1] = "🟦"
            if pasos_y == 8 or pasos_y == 0 or pasos_x == 8 or pasos_x == 0:
                print("Has perdido")
                jugador[pasos_y][pasos_x] = "🟥" 
                break
            vista_juego.vista()
            time.sleep(0.6)
culebrita = Personaje(sprite="⬜")