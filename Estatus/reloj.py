import threading
import time
from os import system

#Imprime el tiempo de la maquina cada n segundos en 20 ocasiones.
def imprimirTiempo (name, n) -> None:
    contador = 0

    while contador < 20:
        time.sleep (n)
        contador += 1

        print (f"{name}: {time.ctime (time.time ())}")
        print ("")

if __name__ == "__main__":
    try:
        t1 = threading.Thread (target=imprimirTiempo, args=("Hilo-1", 2)) #Obtiene el tiempo cada 2 segundos
        t2 = threading.Thread (target=imprimirTiempo, args=("Hilo-2", 4)) #Obtiene el tiempo cada 4 segundos

    except:
        print ("No se pudo ejecutar el hilo.")

    t1.start ()
    t2.start ()
