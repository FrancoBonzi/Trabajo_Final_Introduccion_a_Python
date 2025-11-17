#Nombre y Apellido: Franco Santiago Bonzi

import random

def generarSoloConLetras():

    print("Se va a generar una contraseña solamente con letras \n")

    longitudDeContrasenia = int(input("Ingrese la longitud que quiere que sea su contraseña: "))


    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    contraseña = ""

    for i in range(longitudDeContrasenia):
        contraseña += random.choice(letras)

    print(f"CONTRASEÑA GENERADA: {contraseña}")

    with open("contrasenias.txt","a",encoding="utf-8") as archivo:
        archivo.write("CONTRASEÑA GENERADA: " + contraseña + "\n")

    input("Presione ENTER para continuar...")    


def generarSoloConNumeros():

    print("Se va a generar una contraseña solamente con números \n")

    longitudDeContrasenia = int(input("Ingrese la longitud que quiere que sea su contraseña: "))

    numeros = "0123456789"
    contraseña = ""

    for i in range(longitudDeContrasenia):
        contraseña += random.choice(numeros)

    print(f"CONTRASEÑA GENERADA: {contraseña}")    
    
    with open("contrasenias.txt","a",encoding="utf-8") as archivo:
        archivo.write("CONTRASEÑA GENERADA: "+ contraseña + "\n")

    input("Presione ENTER para continuar...")    

def generarSoloConLetrasYNumeros():

    print("Se va a generar una contraseña solamente con letras y números \n")

    longitudDeContrasenia = int(input("Ingrese la longitud que quiere que sea su contraseña: "))

    letrasyNumeros= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    contraseña = ""

    for i in range(longitudDeContrasenia):
        contraseña += random.choice(letrasyNumeros)

    print(f"CONTRASEÑA GENERADA: {contraseña}")

    with open("contrasenias.txt","a",encoding="utf-8") as archivo:
        archivo.write("CONTRASEÑA GENERADA: "+ contraseña + "\n") 

    input("Presione ENTER para continuar...")       

def generarContraseñaCompleta():

    print("Se va a generar una contraseña solamente con letras, números y caracteres \n")

    longitudDeContrasenia = int(input("Ingrese la longitud que quiere que sea su contraseña: "))

    letrasNumerosyCaracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    contraseña = ""

    for i in range(longitudDeContrasenia):
        contraseña += random.choice(letrasNumerosyCaracteres)

    print(f"CONTRASEÑA GENERADA: {contraseña}")    

    with open("contrasenias.txt","a",encoding="utf-8") as archivo:
        archivo.write("CONTRASEÑA GENERADA: "+ contraseña + "\n")

    input("Presione ENTER para continuar...")        


def salir():
    print("Saliendo del programa....")



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