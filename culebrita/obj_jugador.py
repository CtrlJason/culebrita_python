#Modulos
import mundo, obj_comida, vista_juego, time, keyboard # Para pausar el tiempo de ejecucion de una seccion del codigo
# Variables

jugador = mundo.mapa_culebrita.tablero
class Personaje():
    def __init__(self, sprite):
        self.sprite = sprite
        
    def movimiento(self):
        pasos_x = 2
        pasos_y = 4
        ultima_tecla = "d"
        puntos = 0
        count = 1
        count_s = 1
        count_s = 2
        while True:
            # Verificador de presion de tecla
            if keyboard.is_pressed("w") and not keyboard.is_pressed("s") and not ultima_tecla == "s": # Movimiento arriba
                pasos_y -= 1
                pasos_x += 0
                ultima_tecla = "w"
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y+count_s][pasos_x] = "🟦"
                if count_s > 1 and ultima_tecla == "a":
                    jugador[pasos_y+1][pasos_x-1] = "🟦"
                if count_s > 1 and ultima_tecla == "d":
                    jugador[pasos_y+1][pasos_x+1] = "🟦"
            elif keyboard.is_pressed("d") and not keyboard.is_pressed("a") and not ultima_tecla == "a": # Movimiento derecha
                ultima_tecla = "d"
                pasos_y -= 0
                pasos_x += 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y][pasos_x-count_s] = "🟦"
                if count_s > 1 and ultima_tecla == "w":
                    jugador[pasos_y-1][pasos_x-1] = "🟦"
                if count_s > 1 and ultima_tecla == "s":
                    jugador[pasos_y+1][pasos_x-1] = "🟦"
            elif keyboard.is_pressed("s") and not keyboard.is_pressed("w") and not ultima_tecla == "w": # Movimiento abajo
                pasos_y += 1
                pasos_x += 0
                ultima_tecla = "s"
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y-count_s][pasos_x] = "🟦"
                if count_s > 1 and ultima_tecla == "a":
                    jugador[pasos_y-1][pasos_x-1] = "🟦"
                if count_s > 1 and ultima_tecla == "d":
                    jugador[pasos_y-1][pasos_x+1] = "🟦"
            elif keyboard.is_pressed("a") and not keyboard.is_pressed("d") and not ultima_tecla == "d": # Movimiento izquierda
                pasos_y += 0
                pasos_x -= 1
                ultima_tecla = "a"
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y][pasos_x+count_s] = "🟦"
                if count_s > 1 and ultima_tecla == "w":
                    jugador[pasos_y-1][pasos_x+1] = "🟦"
                if count_s > 1 and ultima_tecla == "s":
                    jugador[pasos_y+1][pasos_x+1] = "🟦"
            # Verificador de ultima tecla presionada    
            if ultima_tecla == "w" and not keyboard.is_pressed("w"): # Movimiento arriba
                pasos_x += 0
                pasos_y -= 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y+count_s][pasos_x] = "🟦"
            elif ultima_tecla == "d" and not keyboard.is_pressed("d"): # Movimiento derecha
                pasos_y -= 0
                pasos_x += 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y][pasos_x-count_s] = "🟦"
            elif ultima_tecla == "s" and not keyboard.is_pressed("s"): # Movimiento abajo
                pasos_y += 1
                pasos_x += 0
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y-count_s][pasos_x] = "🟦"
            elif ultima_tecla == "a" and not keyboard.is_pressed("a"): # Movimiento izquierda
                pasos_y += 0
                pasos_x -= 1
                jugador[pasos_y][pasos_x] = culebrita.sprite
                jugador[pasos_y][pasos_x+count_s] = "🟦"
            if pasos_y == 8 or pasos_y == 0 or pasos_x == 8 or pasos_x == 0:
                print("Has perdido")
                jugador[pasos_y][pasos_x] = "🟥" 
                break
            posicion = [[pasos_y],[pasos_x]]
            posicion2 = obj_comida.manzana.guardado()
            # Verificador de posicion de jugador y fruta
            if posicion == posicion2:
                obj_comida.manzana.posicion_fruta()
                puntos += 1
                count_s += 1
            vista_juego.vista()
            # Puntaje
            print(f"Puntos: {puntos}")
            time.sleep(0.5)
        
culebrita = Personaje(sprite="⬜")