#Creamos el fichero y lo abrimos en modo escritura
file = open("mifichero.txt", "w")
#Escribimos una línea de texto y cerramos el archivo
file.write("Hola, esto es el ejercicio 1 del tema 8")
file.close()
#Abrimos nuevamente el fichero en modo append y agregamos una
#nueva línea de texto
file = open("mifichero.txt", "a")
file.write("\nAgregamos más texto como lo solicita el ejercicio")
#Cerramos el archivo
file.close()