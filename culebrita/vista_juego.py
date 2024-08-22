#Librerias o modulos
import mundo, os

def clean():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Unix/Linux/Mac
    else:
        os.system('clear')

def vista():
    clean()
    for ver_mapa in mundo.mapa_culebrita.tablero:
        print(ver_mapa)
    print("\n")