import random
def PPT():
    salir = True
    print("/////Juego de piedra, papel o tijeras///// \n---Escribe ´salir´ para abandonar el juego---")
    puntos=0
    while salir == True:
        print("")
        opciones = ["piedra", "papel", "tijera"]
        eleccion = input("Elija una opcion: ").strip().lower()
        maquina = random.choice(opciones)
        if maquina == eleccion:
            print("Empate :|")
            print(f"Esta es tu puntuacion: {puntos}")

        elif (maquina == "piedra" and eleccion == "papel") or \
                (maquina == "papel" and eleccion == "tijera") or \
                (maquina == "tijera" and eleccion == "piedra"):
            print(f"*La maquina eligio*: {maquina}")
            print("***Ganaste***")
            puntos+=1
            print(f"Esta es tu puntuacion: {puntos}!!!")
        elif eleccion == "salir":
            salir=False
        elif eleccion not in opciones:
            print("Opcion invalida" )
        else:
            print(f"*La maquina eligio*: {maquina}")
            print("Perdiste...")
            puntos-=1
            print(f"Esta es tu puntuacion: {puntos}")
    print(f"Esta es tu puntuacion final: {puntos}!")

def wordle():
    palabras = [
        "Amigo", "Barco", "Canto", "Denso", "Fuego", "Grito", "Huevo", "Llave", "Nieve", "Ronda",
        "Silla", "Tarde", "Verde", "Zorro", "Arena", "Baila", "Cielo", "Doble", "Faro", "Gallo",
        "Hilos", "Joven", "Lente", "Mente", "Nubes", "Oído", "Pared", "Quita", "Ratas", "Sabor",
        "Tocar", "Usado", "Viento", "Yerno", "Zarpa", "Avena", "Broma", "Carga", "Dulce", "Firme",
        "Gente", "Hacha", "Jugar", "Llama", "Miedo", "Nacer", "Ocaso", "Pista", "Quiso", "Riego",
        "Sello", "Tinta", "Uvas", "Vasto", "Yegua", "Zumba", "Aquel", "Bazar", "Cinta", "Datos",
        "Ficha", "Gotas", "Hilos", "Jefes", "Lomos", "Marea", "Noche", "Ojalá", "Pacto", "Queso",
        "Resto", "Sapos", "Tumba", "Unida", "Votos", "Yates", "Zonas", "Añoso", "Borde", "Cajas",
        "Dices", "Fases", "Gafas", "Hilos", "Jirón", "Lucha", "Mueve", "Naves", "Obras", "Pocos",
        "Quema", "Rizos", "Sueño", "Tocar", "Unión", "Vales", "Yacer", "Zetas", "Aguas", "Botes"
    ]
    palabraC = random.choice(palabras)
    print("/////Mini Wordle ///// \n---Escribe ´salir´ para abandonar el juego---")
    print("**Tienes 5 intentos**")

    puntos = 0
    intentos = 0
    salir = True

    while salir:
        if intentos >= 5:
            print("Se excedió el límite de intentos\n¡Perdiste!")
            puntos -= 50
            print("La palabra correcta era:", palabraC, "!!!")
            print("Tu puntaje fue: ", puntos, "!")
            salir = False
        else:
            intento = input("\n--Ingrese la palabra a probar--\n(la palabra tiene que ser de 5 letras): ").capitalize()

            if intento == "Salir":
                print("La palabra correcta era:", palabraC, "!!!")
                salir = False

            elif len(intento) > 5:
                print("La palabra excede el límite de 5 letras!!!")

            elif len(intento) < 5:
                print("La palabra es inválida, debe tener exactamente 5 letras.")

            else:
                pista = ""
                for i in range(len(palabraC)):
                    l = intento[i]
                    if l == palabraC[i]:
                        pista += "✔"
                    elif l in palabraC:
                        pista += "-"
                    else:
                        pista += "X"

                intentos += 1
                print(f"{pista}")
                print("Intentos:", intentos)
        if intento == palabraC:
            print("La palabra correcta es:", palabraC)
            print("¡¡¡Ganaste!!!")
            print("Lo hiciste con estos intentos: ", intentos, "!")
            print("La palabra correcta era:", palabraC,"!")
            puntos +=200
            print("Tu puntaje fue: ",puntos,"!!!")
            salir = False
wordle()

