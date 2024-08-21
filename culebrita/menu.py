#Librerias o modulos
import obj_comida, obj_jugador
# Menu del juego donde se mostraran 2 opciones
while True:
    control_user = int(input("Bienvenido al juego de la culebrita, seleccione una de las siguientes opciones:\n1. Iniciar juego\n2. Salir\n : "))
    if control_user == 1:
        obj_comida.manzana.posicion_fruta()
        obj_jugador.culebrita.movimiento()
    elif control_user == 2:
        print("\nJuego finalizado")
        break
    else:
        print("Elije una opcion valida\n")
        # Queda pendiente: 1. Jugador se toca asi mismo, pierde 2. Manzana no puede aparecer encima del jugador