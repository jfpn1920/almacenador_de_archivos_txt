import random
ids = []
nombres = []
contenidos = []
categorias = []
fechas = []
estados = []
observaciones = []
#------------------------------------------------#
#--|menu_principal_almacenador_de_archivos_txt|--#
#------------------------------------------------#
while True:
    print("menu principal almacenador de archivos txt")
    print("1) crear archivo txt")
    print("2) editar archivo txt")
    print("3) eliminar archivo txt")
    print("4) buscar archivo txt")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------------#
    #--|crear_archivo_txt|--#
    #-----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_archivo = 1
        else:
            id_archivo = ids[-1] + 1
        nombre = input("nombre del archivo txt: ")
        contenido = input("contenido del archivo: ")
        categoria = input("categoría: ")
        fecha = input("fecha de creación: ")
        estado = input("estado (disponible o archivado): ")
        observacion = input("observación: ")
        ids.append(id_archivo)
        nombres.append(nombre)
        contenidos.append(contenido)
        categorias.append(categoria)
        fechas.append(fecha)
        estados.append(estado)
        observaciones.append(observacion)
        print("archivo txt registrado correctamente.")
        print("id:", id_archivo)
    #------------------------#
    #--|editar_archivo_txt|--#
    #------------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar archivo txt")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {contenidos[i]} | {categorias[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {contenidos[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                nombres[posicion] = input("nuevo nombre del archivo txt: ")
                contenidos[posicion] = input("nuevo contenido: ")
                categorias[posicion] = input("nueva categoría: ")
                fechas[posicion] = input("nueva fecha de creación: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------------#
    #--|eliminar_archivo_txt|--#
    #--------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar archivo txt")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {contenidos[i]} | {categorias[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {contenidos[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    contenidos.pop(posicion)
                    categorias.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------------#
    #--|buscar_archivo_txt|--#
    #------------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar archivo txt")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {contenidos[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            disponibles = 0
            archivados = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {contenidos[i]} | {categorias[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
                if estados[i].lower() == "disponible":
                    disponibles += 1
                elif estados[i].lower() == "archivado":
                    archivados += 1
            print("estadísticas almacenador de archivos txt")
            print("cantidad de archivos:", len(ids))
            print("archivos disponibles:", disponibles)
            print("archivos archivados:", archivados)
            print("primer archivo:", nombres[0])
            print("último archivo:", nombres[-1])
            posicion = random.randint(0, len(ids) - 1)
            print("simulación de almacenamiento")
            print("archivo almacenado correctamente:")
            print(f"{ids[posicion]} | {nombres[posicion]} | {contenidos[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el almacenador de archivos txt.")
        break
    else:
        print("opción no válida.")