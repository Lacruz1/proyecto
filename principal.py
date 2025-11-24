import os
import time
from back import PPT, gato, wordle, numero, simon

ARCHIVO_PUNTUACIONES = "puntuaciones.txt"

def borrar_puntuaciones():
    # Abrir en modo escritura vacía el archivo
    with open(ARCHIVO_PUNTUACIONES, "w", encoding="utf-8") as f:
        pass
    print("\nHistorial de puntuaciones borrado (archivo vacío).")
    time.sleep(1.5)

def guardar_puntuacion(nombre, juego, Puntos):
    with open(ARCHIVO_PUNTUACIONES, "a", encoding="utf-8") as f:
        f.write(f"{nombre}|{juego}|{Puntos}\n")

def mostrar_puntuaciones():
    if not os.path.exists(ARCHIVO_PUNTUACIONES):
        print("No hay registros todavía.")
        return
    with open(ARCHIVO_PUNTUACIONES, "r", encoding="utf-8") as f:
        print("\n=== TABLA DE PUNTUACIONES ===")
        for linea in f:
            print(linea.strip())

def menu_principal():
    nombre = input("Ingresa tu nombre: ")
    salir = True
    while salir:
        print("\n=== MENÚ ===")
        print("1. Gato")
        print("2. Número")
        print("3. Wordle")
        print("4. Piedra, Papel o Tijera")
        print("5. Simon dice")
        print("6. Ver puntuaciones")
        print("7. Borrar puntuaciones")
        print("8. Salir")

        opcion = input("Elige (1-8): ")
        if opcion == "1":
            juego, pts = gato()
        elif opcion == "2":
            juego, pts = numero()
        elif opcion == "3":
            juego, pts = wordle()
        elif opcion == "4":
            juego, pts = PPT()
        elif opcion == "5":
            juego, pts = simon()
        elif opcion == "6":
            mostrar_puntuaciones()
        elif opcion == "7":
            borrar_puntuaciones()
            continue
        elif opcion == "8":
            print("¡Hasta luego!")
            salir = False
            continue
        else:
            print("Opción inválida.")
            time.sleep(1)
            continue

        guardar_puntuacion(nombre, juego, pts)
        print(f"\nResultado: {juego} -> {pts} puntos")

if __name__ == "__main__":
    menu_principal()
    