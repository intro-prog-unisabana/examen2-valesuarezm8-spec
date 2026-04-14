# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    # TODO: Pedir el nombre del archivo al usuario usando input()
    archivo=input("Enter file name:\n")
    # TODO: Abrir el archivo y leer el numero de vueltas n
    with open(archivo, "r") as File:
        vueltas= lap_timer.count()
        File.readline(vueltas)
    # TODO: Crear el cronometro usando lap_timer.init(n)
    cronometro = lap_timer.init()
    tiempo_de_vueltas=lap_timer.add_lap()
    print()
    
    # TODO: Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
    
    # TODO: Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()
    
    pass


if __name__ == "__main__":
    main()
