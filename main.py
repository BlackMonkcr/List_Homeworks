while True:
    interaccion = input("¿Quieres realizar alguna accion? (Y/N): ")

    if interaccion.lower() != "n":

        #Menu de opciones
        if interaccion.lower() == "y":
            print("\n¿Que accion desea realizar?\n")
            print("1. Registrar Tarea")
            print("2. Editar Tarea")
            print("3. Eliminar Tarea")
            print()

            #Verificacion de opcion
            accion = input("Indica una opcion (numero): ")

            if accion == "1":
                #REGISTRO
                print("\nREGISTRAR TAREA\n")


            elif accion == "2":
                #EDICION
                print("\nEDITAR TAREA\n")


            elif accion == "3":
                #ELIMINACION
                print("\nELIMINAR TAREA\n")


            else:
                #NO OPTION
                print("\nNinguna opcion ingresada\n")
    else:
        break;

