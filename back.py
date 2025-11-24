import random
def PPT():
    salir = True
    print("Juego de piedra papel tijeras\nEscriba ´salir´ para abandonar el juego")
    puntos=0
    while salir == True:
        print("")
        opciones = ["piedra", "papel", "tijera"]
        eleccion = input("Elija una opcion: ").strip().lower()
        maquina = random.choice(opciones)
        if maquina == eleccion:
            print("Empate")

        elif (maquina == "piedra" and eleccion == "papel") or \
                (maquina == "papel" and eleccion == "tijera") or \
                (maquina == "tijera" and eleccion == "piedra"):
            print(f"La maquina eligio : {maquina}")
            print("Ganaste")
            puntos+=1
            print(puntos)
        elif eleccion == "salir":
            salir=False
        elif eleccion not in opciones:
            print("Opcion invalida" )
        else:
            print(f"La maquina eligio : {maquina}")
            print("Perdiste")
            puntos-=1
            print(puntos)
    print(puntos)