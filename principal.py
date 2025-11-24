#codigo para la interfaz grafica
import os
import time
import random

ARCHIVO_PUNTUACIONES = "puntuaciones.txt"


def cargar_puntuaciones():
    """Lee el archivo y retorna una lista de diccionarios."""
    datos = []
    if os.path.exists(ARCHIVO_PUNTUACIONES):
        with open(ARCHIVO_PUNTUACIONES, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 3:
                    datos.append({"jugador": partes[0], "juego": partes[1], "puntos": int(partes[2])})
    return datos

def guardar_puntuacion(nombre, juego, puntos):
    """Escribe una nueva puntuación en el archivo (Persistencia)."""
    with open(ARCHIVO_PUNTUACIONES, "a", encoding="utf-8") as f:
        f.write(f"{nombre}|{juego}|{puntos}\n")


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_encabezado(texto):
    print("=" * 50)
    print(f"{texto.center(50)}")
    print("=" * 50)


def pantalla_inicio():
    limpiar_pantalla()
    print("\n")
    print("╔" + "═" * 48 + "╗")
    print("║" + " " * 48 + "║")
    print("║" + "   S I S T E M A   D E   M I N I J U E G O S    ║")
    print("║" + " " * 48 + "║")
    print("╚" + "═" * 48 + "╝")
    print("\n")
    

    while True:
        nombre = input("  >>> Por favor, ingresa tu nombre de jugador: ").strip()
        if len(nombre) > 0:
            return nombre
        print("  (!) El nombre no puede estar vacío.")


def jugar_minijuego(numero_juego, nombre_jugador):
    limpiar_pantalla()
    imprimir_encabezado(f"MINIJUEGO #{numero_juego}")
    print(f"\n  ¡Jugando al juego {numero_juego}...")
    
    
    time.sleep(1.5) 
    puntos_obtenidos = random.randint(10, 100) 
    
    print(f"  Terminaste el juego. ¡Obtuviste {puntos_obtenidos} puntos!")
    
   
    guardar_puntuacion(nombre_jugador, f"Juego {numero_juego}", puntos_obtenidos)
    print("\n  [Puntuación guardada exitosamente]")
    input("\n  Presiona ENTER para volver al menú...")

def mostrar_tabla_puntuaciones():
    limpiar_pantalla()
    imprimir_encabezado("TABLA DE PUNTUACIONES")
    
    datos = cargar_puntuaciones() 
    
    if not datos:
        print("\n  No hay registros todavía.")
    else:
        print(f"\n  {'JUGADOR':<15} | {'JUEGO':<10} | {'PUNTOS':<10}")
        print("  " + "-"*40)
        for registro in datos:
            print(f"  {registro['jugador']:<15} | {registro['juego']:<10} | {registro['puntos']:<10}")
            
    input("\n  Presiona ENTER para volver al menú...")


def menu_principal():
    nombre_jugador = pantalla_inicio() 
    
    while True:
        limpiar_pantalla()
        print(f"  Jugador actual: {nombre_jugador}\n")
        imprimir_encabezado("MENÚ PRINCIPAL")
        
   
        print("  1. Jugar Minijuego 1 (piedra, papel o tijeras)")
        print("  2. Jugar Minijuego 2 (tres en rayas)")
        print("  3. Jugar Minijuego 3 (ahorcado)")
        print("  4. Jugar Minijuego 4 (nmb)")
        print("  5. Jugar Minijuego 5 (bsucamina)")
        print("  6. Ver Puntuaciones") 
        print("  7. Salir")             
        
        opcion = input("\n  >>> Selecciona una opción (1-7): ")
        

        if opcion in ['1', '2', '3', '4', '5']:
            jugar_minijuego(int(opcion), nombre_jugador)
        
        elif opcion == '6':
            mostrar_tabla_puntuaciones()
            
        elif opcion == '7':
            print(f"\n  ¡Hasta luego, {nombre_jugador}!")
            break
        
        else:
            print("\n  (!) Opción no válida.")
            time.sleep(1)


if __name__ == "__main__":
   
    menu_principal()