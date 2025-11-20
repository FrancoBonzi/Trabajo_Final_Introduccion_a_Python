#Nombre y Apellido: Franco Santiago Bonzi

import secrets
import string
import sys

diccionario = {
    'letras' : string.ascii_letters,
    'numeros' : string.digits,
    'caracteres' : string.punctuation
}

def generarSoloConLetras():

    print("Se va a generar una contraseña solamente con letras \n")

    longitudDeContrasenia = input("Ingrese la longitud que quiere que sea su contraseña: ")

    while not longitudDeContrasenia.isdigit() or int(longitudDeContrasenia)<4:
        print("\nERROR: Debe ingresar un número mayor a 4.\n")
        longitudDeContrasenia = input("Ingrese la longitud que quiere que sea su contraseña: ")

    longitudDeContrasenia = int(longitudDeContrasenia)

    contraseña = ""

    for i in range(longitudDeContrasenia):
        contraseña += secrets.choice(diccionario["letras"])

    print(f"CONTRASEÑA GENERADA: {contraseña}")

    with open("contrasenias.txt","a",encoding="utf-8") as archivo:
        archivo.write("CONTRASEÑA GENERADA: " + contraseña + "\n")

    input("Presione ENTER para continuar...")    


def generarSoloConNumeros():

    print("Se va a generar una contraseña solamente con números \n")

    longitudDeContrasenia = input("Ingrese la longitud que quiere que sea su contraseña: ")

    while not longitudDeContrasenia.isdigit() or int(longitudDeContrasenia)<4:
        print("\nERROR: Debe ingresar un número mayor a 4.\n")
        longitudDeContrasenia = input("Ingrese la longitud que quiere que sea su contraseña: ")

    longitudDeContrasenia = int(longitudDeContrasenia)    

    contraseña = ""

    for i in range(longitudDeContrasenia):
        contraseña += secrets.choice(diccionario["numeros"])

    print(f"CONTRASEÑA GENERADA: {contraseña}")    
    
    with open("contrasenias.txt","a",encoding="utf-8") as archivo:
        archivo.write("CONTRASEÑA GENERADA: "+ contraseña + "\n")

    input("Presione ENTER para continuar...")    

def generarSoloConLetrasYNumeros():

    print("Se va a generar una contraseña solamente con letras y números \n")

    longitudDeContrasenia = input("Ingrese la longitud que quiere que sea su contraseña: ")

    while not longitudDeContrasenia.isdigit() or int(longitudDeContrasenia)<4:
        print("\nERROR: Debe ingresar un número mayor a 4.\n")
        longitudDeContrasenia = input("Ingrese la longitud que quiere que sea su contraseña: ")

    longitudDeContrasenia = int(longitudDeContrasenia)

    letrasyNumeros = diccionario["letras"] + diccionario["numeros"]

    contraseña = ""

    for i in range(longitudDeContrasenia):
        contraseña += secrets.choice(letrasyNumeros)

    print(f"CONTRASEÑA GENERADA: {contraseña}")

    with open("contrasenias.txt","a",encoding="utf-8") as archivo:
        archivo.write("CONTRASEÑA GENERADA: "+ contraseña + "\n") 

    input("Presione ENTER para continuar...")       

def generarContraseñaCompleta():

    print("Se va a generar una contraseña solamente con letras, números y caracteres \n")

    longitudDeContrasenia = input("Ingrese la longitud que quiere que sea su contraseña: ")

    while not longitudDeContrasenia.isdigit() or int(longitudDeContrasenia)<4:
       print("\nERROR: Debe ingresar un número mayor a 4.\n")
       longitudDeContrasenia = input("Ingrese la longitud que quiere que sea su contraseña: ")
 
    longitudDeContrasenia = int(longitudDeContrasenia)

    letrasNumerosyCaracteres = diccionario["letras"] + diccionario["numeros"] + diccionario["caracteres"]
    contraseña = ""

    for i in range(longitudDeContrasenia):
        contraseña += secrets.choice(letrasNumerosyCaracteres)

    print(f"CONTRASEÑA GENERADA: {contraseña}")    

    with open("contrasenias.txt","a",encoding="utf-8") as archivo:
        archivo.write("CONTRASEÑA GENERADA: "+ contraseña + "\n")

    input("Presione ENTER para continuar...")        


def salir():
    print("Saliendo del programa....")
    sys.exit()



def MenuPrincipal():

    while True: 
        print("*--------------Bienvenidos-------------*")

        print("       Generador de contraseñas         ")

        print("------------------*.*-------------------")

        print("Seleccione una de las siguientes opciones: \n")

        print(">> 1. Generar contraseña solo de Letras")
    
        print(">> 2. Generar contraseña solo de Números")
    
        print(">> 3. Generar contraseña solo de Letras y Números")
    
        print(">> 4. Generar contraseña solo de Letras, Números y caracteres")
    
        print(">> 0. Salir \n")


        opcionSeleccionada = int(input("|> Escriba la opción seleccionada: "))

        if opcionSeleccionada == 1:
            generarSoloConLetras()  
        elif opcionSeleccionada == 2:
            generarSoloConNumeros()
        elif opcionSeleccionada == 3:
            generarSoloConLetrasYNumeros()    
        elif opcionSeleccionada == 4:
            generarContraseñaCompleta() 
        elif opcionSeleccionada == 0:
            salir()  
        else:
            print("LA OPCIÓN INGRESADA NO ES VÁLIDA. INTENTE DE NUEVO....")    



MenuPrincipal()