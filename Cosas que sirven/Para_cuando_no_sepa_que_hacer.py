#Lista que elige aleatoriamente una actividad para cuando no sepa qué hacer
import random

def obtenerContenido(FICHERO):
    with open(FICHERO, "rt", encoding="utf-8") as file:
        lista = []
        linea = file.readline()
        lista.append(linea.strip())

        while linea!="":
            linea = file.readline()
            lista.append(linea.strip())

        lista.pop(-1)
        return lista

def nuevaActividad(lista, FICHERO):
    nueva = input("Introduce una nueva actividad: ")
    if nueva=="":
        return ""

    if nueva in lista:
        print("\nEsa actividad ya se encuentra en la lista\n")
    else:
        with open(FICHERO, 'at', encoding="utf-8") as file:
            file.write(nueva + "\n")
        print("\nActividad añadida a la lista\n")

def eliminarActividad(lista, FICHERO):
    eliminada = input("\nIntroduce la actividad que desees eliminar de la lista: ")
    if eliminada=="":
        return ""

    if eliminada not in lista:
        print("\nNo se encuentra la actividad en la lista\n")
    else:
        lista_nueva = [elem for elem in lista if elem!=eliminada]
        with open(FICHERO, "wt", encoding="utf-8") as file:
            for elem in lista_nueva:
                file.write(elem + "\n")
        print("\nLista actualizada correctamente\n")

def mostrarActividades(lista):
    if len(lista)==0:
        print("No tienes ninguna actividad en tu lista\n")
    else:
        print("\n" + ("\n".join([str(x) for x in lista])) + "\n")

def generarAleatoria(lista):
    if len(lista)==0:
        print("No tienes ninguna actividad en tu lista\n")
    else:
        numero = random.randint(1, len(lista))
        resultado = str(lista[numero-1])
        print(resultado)
        print()

def mostrarMenu(lista):
    opcion = 0

    while opcion!="5":
        print("Elige una opción:\n  *Para abortar una opción, presiona enter\n\n1 - Introducir una activida nueva\n2 - Muéstrame la lista de actividades\n3 - Elige una actividad por mí\n4 - Eliminar actividad de la lista\n5 - Termina el programa\n")
        opcion = input()
        match opcion:
            case "1":
                nuevaActividad(lista, FICHERO)
                lista = obtenerContenido(FICHERO)
            case "2": mostrarActividades(lista)
            case "3": generarAleatoria(lista)
            case "4":
                 eliminarActividad(lista, FICHERO)
                 lista = obtenerContenido(FICHERO)
            case "5":
                print("¡Hasta pronto!")
                input()
            case _: print("Opción no válida\n")

print("Este programa te ayudará a elegir una actividad si no sabes qué hacer o no te decides\n")
FICHERO = "actividades"
lista = obtenerContenido(FICHERO)
mostrarMenu(lista)

