import psutil
from os import system

#Funcion para verificar si el proceso esta vivo.
def isAlive () -> bool:
    #Iteramos sobre todos los procesos actuales y obtenemos su nombre
    for proc in psutil.process_iter():
        if proc.name () == "reloj.exe":
            return True
        
    return False

if __name__ == "__main__":
    while True:
        if not isAlive ():
            system ("start reloj.exe")