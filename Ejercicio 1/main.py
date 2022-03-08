import numpy as np

word = input("Instroduce una o varias palabras: ")
lst = list(word)#Se convierte en una lista
columnas = int(input("coloque las columnas deseadas: "))
lon = len(lst)#obtenemos la longitud para obtener cuantos espacios faltan
filas = int((lon / columnas) + .9)#Se obtiene el numero de filas
mul = int(filas * columnas)#Es el total el numero de espacios de la matriz
while lon < mul:#rellenado de espacios la lista
    lst = lst + [" "]
    lon = len(lst)
ar = np.array(lst).reshape((filas, columnas))#cambiamos la lista a una matriz
ra = np.transpose(ar)#la transponemos para el encriptado
tsl = np.reshape(ra, mul)#a lista de nuevo
print("".join(map(str, tsl)))#resultado de encriptado
