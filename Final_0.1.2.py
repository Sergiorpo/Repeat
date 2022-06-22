import os
import platform
def limpiar():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

print("Esta aplicacion te permite escribir un texto y "
      "sustituir los {0} por la palabra o palabras que te pedire a continuacion.")

texto = input("Introduce un texto: ")
lista = []
lista_usuario = None
limpiar()


print("Ahora escribe el nombre de usuario o usuarios. Puedes introducir tantos como quieras.")
while lista_usuario != "SALIR":
    lista_usuario = input("Introduzca un usuario y escribe 'SALIR' para finalizar:  ")
    if lista_usuario == "SALIR":
        print("FIN")
    if lista_usuario != "SALIR":
        lista.append(lista_usuario)


limpiar()
nombre_fichero = input("Dime el nombre del fichero: ")
extension_archivo = input("Dime en que extension quieres que se guarde (No es necesario poner punto.).\n"
                          "Extension: ")

f = open (nombre_fichero+'.'+extension_archivo,'w')
list_user = []


for i in lista:
    list_user.append(texto.format(i))



print('\n'.join(list_user),file=f)
f.close()
input("Presiona cualquier tecla para finalizar...")