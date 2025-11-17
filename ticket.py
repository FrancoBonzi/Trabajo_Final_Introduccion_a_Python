#Nombre y Apellido: Franco Santiago Bonzi

"""
Se ha pedido crear un modulo para generar ticktes que contenga lo siguiente:
Un menu con 3 opciones - Alta ticket , Leer ticket , Salir.
    *Alta ticket : nombre, sector,asunto, problema
        -Al terminar de ingresar el ticket se debera mostrar por pantalla el mismo,
        sumandose el numero de ticket (que sera un numero random entre 1000,
        9999) y una leyenda que pida acordarse del numero
        -un menu que nos pregunte si deseamos crear otro ticket, en caso de ser no
        que nos regrese al menu principal, de lo contrario que nos regrese a la
        pantalla de alta.
    *leer ticet: numero ticket
        al ingresar el numero nos mostrara por pantalla el ticket almacenado
        debajo del mismo aparece una leyanda que nos preguntara si deseamos leer
        otro ticket, teniendo la funcionalidad similar a la anteriormente mensionada.
    *Salir : el programa finaliza y se cierra pidiendonos una confirmacion
"""
import random
import os

#FUNCIÓN PARA PODER LIMPIAR PANTALLA
def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")


#FUNCIÓN DE ALTA TICKET
def AltaTicket():

    while True:
        
        limpiarPantalla()

        print("Ingrese los datos para Generar el nuevo ticket\n")

        nombre = input("Ingrese su Nombre: ")
        sector = input("Ingrese su Sector: ")
        asunto = input("Ingrese su asunto: ")
        problema = input("Describa el problema que tiene: ")

        numeroTicket = random.randint(1000,9999)

        with open("tickets.txt","a",encoding="utf-8") as archivo:
            archivo.write(f"{numeroTicket}|{nombre}|{sector}|{asunto}|{problema}\n")

        limpiarPantalla()

        print("==========================================================")
        print("             Se genero el siguiente Ticket")
        print("==========================================================\n")

        print(f"Su nombre: {nombre}         N° Ticket: {numeroTicket}")
        print(f"Su Sector: {sector}")
        print(f"Asunto: {asunto}\n")

        print(f"Problema: {problema}\n")

        print(">>> Recorda el número de ticket <<<\n")

        respuesta = input("Desea generar un nuevo ticket? (s/n): ").lower()

        if respuesta != 's':
            break

def LeerTicket():

    while True:
        limpiarPantalla()

        numeroDeTicket = int(input("Ingrese el número de ticket: "))

def Salir():

    confirmarRespuesta = input("¿Estás seguro de salir (s/n): ?").lower()

    if confirmarRespuesta == 's':
        print("Está saliendo del programa...")  
        exit()     
    else:
        return

def Menu():

    while True:
        

        print("Hola bienvenido al Sistema de Tickets")

        print("1 - Generar un Nuevo Ticket")
        print("2 - Leer un Ticket")
        print("3 - Salir")

        opcionElegida = int(input(f"Seleccione: "))

        if opcionElegida == 1:
            AltaTicket()
        elif opcionElegida == 2:
            LeerTicket()
        elif opcionElegida == 3:
            Salir()
            break
        else:
            print("LA OPCIÓN INGRESADA NO ES LA CORRETA. INTENTE DE NUEVO")   
      

        
Menu()


        

