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
import sys

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
        mensaje = input("Ingrese un Mensaje: ")

        numero_ticket = random.randrange(1000,9999)

        limpiarPantalla()

        print("==========================================================")
        print("             Se genero el siguiente Ticket")
        print("==========================================================\n")

        print(f"Su nombre: {nombre}         N° Ticket: {numero_ticket}")
        print(f"Su Sector: {sector}")
        print(f"Asunto: {asunto}\n")

        print(f"Mensaje: {mensaje}\n")

        print(">>> Recorda el número de ticket <<<\n")

        with open("tickets.txt","a",encoding="utf-8") as archivo:
            archivo.write(f"{numero_ticket}|{nombre}|{sector}|{asunto}|{mensaje}\n")

        respuesta = input("Desea generar un nuevo ticket? (s/n): ").lower()

        if respuesta != 's':
            return

def LeerTicket():

    while True:
        limpiarPantalla()

        numeroDeTicket = input("Ingrese el número de ticket: ")    

        if not os.path.exists("tickets.txt"):
            print("\n Aún no hay tickets cargados...")
            input("Presione ENTER para continuar") 
            return

        encontrado = False

        with open("tickets.txt","r",encoding="utf-8") as archivo:
            for linea in archivo:
              partes = linea.strip().split("|")

              if partes[0] == numeroDeTicket:
                limpiarPantalla()

                print("===== TICKET ENCONTRADO ====\n")
                print(f"Número: {partes[0]}")
                print(f"Nombre: {partes[1]}")
                print(f"Sector: {partes[2]}")
                print(f"Asunto: {partes[3]}")
                print(f"Mensaje: {partes[4]}")
                print("============================\n")

                encontrado=True
                break
        
        if not encontrado:
            print("\nEL NÚMERO DE TIKCET INGRESADO NO SE ENCUENTRA.\n")


        opcion = input("\n¿Desea leer otro número de ticket (s/n): ").lower()

        if opcion != 's':
            print("SALIENDO DEL programa")   
            break  


def Salir():
    print("\Cerrando el sistema...")
    sys.exit() 

def Menu():

    while True:
        
        limpiarPantalla()

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
            print("LA OPCIÓN INGRESADA NO ES LA CORRECTA. INTENTE DE NUEVO")   
            input("Presione ENTER para continuar...")
      

        
Menu()


        

