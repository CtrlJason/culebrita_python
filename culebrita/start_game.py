#Librerias o modulos
import obj_comida, obj_jugador, os

def clean():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Unix/Linux/Mac
    else:
        os.system('clear')
#---------------------------------------------------------------------#
# Menu del juego donde se mostraran 2 opciones
while True:
    control_user = int(input("Bienvenido al juego de la culebrita, seleccione una de las siguientes opciones:\n1. Iniciar juego\n2. Creditos\n3. Salir\n : "))
    if control_user == 1:
        obj_comida.manzana.posicion_fruta()
        obj_jugador.culebrita.movimiento()
    elif control_user == 2:
        clean()
        print("\ncreditos:\n✨ Hecho por: Yeison David Mosquera Murillo\n✨ Github: CtrlJason\n")
    elif control_user == 3:
        clean()
        print("\nJuego terminado \n\n¡Gracias por jugar! 🤓\n")
        break
    else:
        clean()
        print("Elije una opcion valida\n")
        # Queda pendiente: 1. Jugador se toca asi mismo, pierde 2. Manzana no puede aparecer encima del jugador