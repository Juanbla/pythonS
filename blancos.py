#Comprueba si un directorio esta vacio o no

import os
dirName = 'C:/Users/juanv/Documents/'

if os.path.exists(dirName) and os.path.isdir(dirName):

    if not os.listdir(dirName):
        print(f" Directorio vacio {dirName}.")
    else:
        print(f"Directorio {dirName} no vacio.")
else:
    print(f"El directorio {dirName} no existe.")
