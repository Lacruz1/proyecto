import random
import time
def PPT():
    salir = True
    print("/////Juego de piedra, papel o tijeras///// \n---Escribe ´salir´ para abandonar el juego---")
    Puntos=0
    while salir == True:
        print("")
        opciones = ["piedra", "papel", "tijera"]
        eleccion = input("Elija una opcion: ").strip().lower()
        maquina = random.choice(opciones)
        if maquina == eleccion:
            print("Empate :|")
            print(f"Esta es tu puntuacion: {Puntos}")

        elif (maquina == "piedra" and eleccion == "papel") or \
                (maquina == "papel" and eleccion == "tijera") or \
                (maquina == "tijera" and eleccion == "piedra"):
            print(f"*La maquina eligio*: {maquina}")
            print("***Ganaste***")
            Puntos+=1
            print(f"Esta es tu puntuacion: {Puntos}!!!")
        elif eleccion == "salir":
            salir=False
        elif eleccion not in opciones:
            print("Opcion invalida" )
        else:
            print(f"*La maquina eligio*: {maquina}")
            print("Perdiste...")
            Puntos-=1
            print(f"Esta es tu puntuacion: {Puntos}")
    print(f"Esta es tu puntuacion final: {Puntos}!")
    return "PPT", Puntos
def simon():
    Puntos = 0
    secuencia = []
    ronda = 1
    salida = True
    print("///// Juego de Simón Dice (Secuencia de Números) /////")
    print("--- Objetivo: Repetir la secuencia de números en el orden correcto. ---")
    print("--- Escribe 'salir' en cualquier momento para abandonar. ---")
    time.sleep(8)
    while salida == True:
        print("\n" + "="*50)
        print(f"Ronda: {ronda}")
        nuevo_numero = random.randint(1, 10) 
        secuencia.append(nuevo_numero)
        
        print("\n¡Observa y memoriza estos numeros!")
        time.sleep(5)
        for num in secuencia:
            print(f"  --> {num}")
            time.sleep(0.5) 
        
        time.sleep(0.5) 
        print("\n" * 50) 
        print("Ahora, ingresa la secuencia completa, número por número ")
        
        
        correcto = True
        
        for i in range(len(secuencia)):
            
            a = f"Número #{i + 1} de {len(secuencia)}: "
            entrada = input(a).strip() 

        
            if entrada.lower() == 'salir':
                print("Tu puntaje final es:", Puntos)
                salida = False
                correcto = False
                break
            
            
            try:
                intento_num = int(entrada)
            except ValueError:
                
                print("Entrada inválida. Debes ingresar un número.")
                correcto = False
                break 

           
            if intento_num != secuencia[i]:
                print(f" Incorrecto. El número correcto era: {secuencia[i]}.")
                correcto = False
                break
        
        if not salida:
            break
            
        if correcto:
            print("\n¡Correcto! Has recordado toda la secuencia.\n")
        
            Puntos += 3 * ronda 
            ronda += 1
            print(f"Tu puntaje actual es: {Puntos}")
        else:
            Puntos -= 2 * ronda
            print(f"\n¡Derrota! Perdiste en la Ronda {ronda}.")
            print(f"La secuencia completa era: {secuencia}")
            print(f"Tu puntaje final es: {Puntos}")
            salida = False 
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

    Puntos = 0
    intentos = 0
    salir = True

    while salir:
        if intentos >= 5:
            print("Se excedió el límite de intentos\n¡Perdiste!")
            Puntos -= 50
            print("La palabra correcta era:", palabraC, "!!!")
            print("Tu puntaje fue: ", Puntos, "!")
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
            Puntos +=200
            print("Tu puntaje fue: ",Puntos,"!!!")
            salir = False
    return "Wordle", Puntos
def gato():

    print("¡Bienvenido al juego del Gato!")
    print("Referencia de posiciones:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("------------")
    Puntos=0
    while True:
        tablero = [" "] * 10
        jugador = input("¿Quieres ser X o O? ").upper()
        computadora = "O" if jugador == "X" else "X"
        turno = random.choice(["jugador", "computadora"])
        print(turno, "irá primero.")

        def dibujar():
            print(" " + tablero[1] + " | " + tablero[2] + " | " + tablero[3])
            print("-----------")
            print(" " + tablero[4] + " | " + tablero[5] + " | " + tablero[6])
            print("-----------")
            print(" " + tablero[7] + " | " + tablero[8] + " | " + tablero[9])

        def ganador(letra):
            return ((tablero[1]==letra and tablero[2]==letra and tablero[3]==letra) or
                    (tablero[4]==letra and tablero[5]==letra and tablero[6]==letra) or
                    (tablero[7]==letra and tablero[8]==letra and tablero[9]==letra) or
                    (tablero[1]==letra and tablero[4]==letra and tablero[7]==letra) or
                    (tablero[2]==letra and tablero[5]==letra and tablero[8]==letra) or
                    (tablero[3]==letra and tablero[6]==letra and tablero[9]==letra) or
                    (tablero[1]==letra and tablero[5]==letra and tablero[9]==letra) or
                    (tablero[3]==letra and tablero[5]==letra and tablero[7]==letra))

        def tableroLleno():
            return all(tablero[i] != " " for i in range(1,10))

        juego = True
        while juego:
            if turno == "jugador":
                dibujar()
                mov = input("Tu movimiento (1-9): ")
                if mov.isdigit() and 1 <= int(mov) <= 9 and tablero[int(mov)] == " ":
                    tablero[int(mov)] = jugador
                    if ganador(jugador):
                        dibujar()
                        print("¡Ganaste!")
                        Puntos+=5
                        print("tu puntaje es:", Puntos)
                        juego = False
                    elif tableroLleno():
                        dibujar()
                        print("¡Empate!")
                        print("tu puntaje es:", Puntos)
                        Puntos-=2
                        juego = False
                        
                    else:
                        turno = "computadora"
                else:
                    print("Movimiento inválido.")
            else:
                mov = random.choice([i for i in range(1,10) if tablero[i] == " "])
                tablero[mov] = computadora
                if ganador(computadora):
                    dibujar()
                    print("La computadora ganó.")
                    Puntos-=80
                    juego = False
                elif tableroLleno():
                    dibujar()
                    print("¡Empate!")
                    juego = False
                else:
                    turno = "jugador"

        if input(f"Esta es tu puntuacion: {Puntos} \nQuieres jugar de nuevo? (s/n): ").lower() != "s":
            break
    return "Gato", Puntos
def numero():
    intento=10
    Puntos=0
    salida = True
    while salida == True:    
        print("")
        dificultad = input("selecciona ´salir´ para abandonar o una dificultad: \nFacil(0-20), \nMedio(0-70),\ndificil(0-200), \nImposible(0-500),\nMODO ´Diablo´(0-4000)\n").lower().strip()
        try:
            if dificultad == "facil": 
                nC=random.randint(0,20)
                while intento > 0:
                    print("")
                    print("")
                    print("---------------------------------------------")
                    print(f"Intentos restantes: {intento}")
                    print("")
                    ing=int(input("Ingresa un numero: "))
                    if ing < 0 or ing > 20:
                        print("El numero es invalido, selecciona un numero dentro del rango(0-20)")
                        print(f"Intentos restantes: {intento}")
                    if ing == nC:
                        print(f"Ganaste el numero era {nC}")
                        Puntos+=10
                        print(f"Tu puntaje es: {Puntos}")
                        if intento == 1:
                            intento += 9
                        elif intento == 2:
                            intento += 8
                        elif intento == 3:
                            intento += 7
                        elif intento == 4:
                            intento += 6
                        elif intento == 5:
                            intento += 5
                        elif intento == 6:
                            intento += 4
                        elif intento == 7:
                            intento += 3
                        elif intento == 8:
                            intento += 2
                        elif intento == 9:
                            intento += 1
                        break
                    elif ing < nC:
                        print("El numero correcto es mayor")
                        intento-=1

                    elif ing > nC:
                        print("El numero correcto es menor")
                        intento-=1
                        
                if intento == 0:
                    print("")
                    print("")
                    print(f"Intentos restantes: {intento}")
                    print(f"Te quedaste sin intentos perdiste")
                    print(f"El numero correcto era: {nC}")
                    Puntos-=100
                    print(f"{Puntos} puntos perdidos")
                    intento +=10
        except ValueError:
            print("entrada invalida")
        try:
            if dificultad == "medio": 
                nC=random.randint(0,70)
                while intento > 0:
                    print("")
                    print("")
                    print("---------------------------------------------")
                    print(f"Intentos restantes: {intento}")
                    print("")
                    ing=int(input("Ingresa un numero: "))
                    if ing < 0 or ing > 70:
                        print("El numero es invalido, selecciona un numero dentro del rango(0-70)")
                        
                    if ing == nC:
                        print(f"Ganaste el numero era {nC}")
                        Puntos+=40
                        print(f"Tu puntaje es: {Puntos}")
                        if intento == 1:
                            intento += 9
                        elif intento == 2:
                            intento += 8
                        elif intento == 3:
                            intento += 7
                        elif intento == 4:
                            intento += 6
                        elif intento == 5:
                            intento += 5
                        elif intento == 6:
                            intento += 4
                        elif intento == 7:
                            intento += 3
                        elif intento == 8:
                            intento += 2
                        elif intento == 9:
                            intento += 1
                        break
                    elif ing < nC:
                        print("El numero correcto es mayor")
                        intento-=1
                        
                    elif ing > nC:
                        print("El numero correcto es menor")
                        intento-=1
                        
                if intento == 0:
                    print("")
                    print("")
                    print(f"Intentos restantes: {intento}")
                    print(f"Te quedaste sin intentos perdiste")
                    print(f"El numero correcto era: {nC}")
                    Puntos-=150
                    print(f"{Puntos} puntos perdidos")
                    intento +=10
        except ValueError:
            print("entrada invalida")
        try:
            if dificultad == "dificil": 
                nC=random.randint(0,200)
                while intento > 0:
                    print("")
                    print("")
                    print("---------------------------------------------")
                    print(f"Intentos restantes: {intento}")
                    print("")
                    ing=int(input("Ingresa un numero: "))
                    if ing < 0 or ing > 200:
                        print("El numero es invalido, selecciona un numero dentro del rango(0-200)")

                    if ing == nC:
                        print(f"Ganaste el numero era {nC}")
                        Puntos+=200
                        print(f"Tu puntaje es: {Puntos}")
                        if intento == 1:
                            intento += 9
                        elif intento == 2:
                            intento += 8
                        elif intento == 3:
                            intento += 7
                        elif intento == 4:
                            intento += 6
                        elif intento == 5:
                            intento += 5
                        elif intento == 6:
                            intento += 4
                        elif intento == 7:
                            intento += 3
                        elif intento == 8:
                            intento += 2
                        elif intento == 9:
                            intento += 1
                        break
                    elif ing < nC:
                        print("El numero correcto es mayor")
                        intento-=1
                        
                    elif ing > nC:
                        print("El numero correcto es menor")
                        intento-=1
                        
                if intento == 0:
                    print("")
                    print("")
                    print(f"Intentos restantes: {intento}")
                    print(f"Te quedaste sin intentos perdiste")
                    print(f"El numero correcto era: {nC}")
                    Puntos-=100
                    print(f"{Puntos} puntos perdidos")
                    intento +=10
        except ValueError:
            print("entrada invalida")
        try:
            if dificultad == "imposible": 
                nC=random.randint(0,400)
                while intento > 0:
                    print("")
                    print("")
                    print("---------------------------------------------")
                    print(f"Intentos restantes: {intento}")
                    print("")
                    ing=int(input("Ingresa un numero: "))
                    if ing < 0 or ing > 500:
                        print("El numero es invalido, selecciona un numero dentro del rango(0-500)")
                        
                    if ing == nC:
                        print(f"Ganaste el numero era {nC}")
                        Puntos+=300
                        print(f"Tu puntaje es: {Puntos}")
                        if intento == 1:
                            intento += 9
                        elif intento == 2:
                            intento += 8
                        elif intento == 3:
                            intento += 7
                        elif intento == 4:
                            intento += 6
                        elif intento == 5:
                            intento += 5
                        elif intento == 6:
                            intento += 4
                        elif intento == 7:
                            intento += 3
                        elif intento == 8:
                            intento += 2
                        elif intento == 9:
                            intento += 1
                        break
                    elif ing < nC:
                        print("El numero correcto es mayor")
                        intento-=1
                        
                    elif ing > nC:
                        print("El numero correcto es menor")
                        intento-=1
                        
                if intento == 0:
                    print("")
                    print("")
                    print(f"Intentos restantes: {intento}")
                    print(f"Te quedaste sin intentos perdiste")
                    print(f"El numero correcto era: {nC}")
                    Puntos-=40
                    print(f"{Puntos} puntos perdidos")
                    intento +=10
        except ValueError:
            print("entrada invalida")
        try:
            if dificultad == "diablo": 
                nC=random.randint(0,4000)
                while intento > 0:
                    print("")
                    print("")
                    print("---------------------------------------------")
                    print(f"Intentos restantes: {intento}")
                    print("")
                    ing=int(input("Ingresa un numero: "))
                    if ing < 0 or ing > 4000:
                        print("El numero es invalido, selecciona un numero dentro del rango(0-4000)")
                        
                    if ing == nC:
                        print(f"Ganaste el numero era {nC}")
                        Puntos+=500
                        print(f"Tu puntaje es: {Puntos}")
                        if intento == 1:
                            intento += 9
                        elif intento == 2:
                            intento += 8
                        elif intento == 3:
                            intento += 7
                        elif intento == 4:
                            intento += 6
                        elif intento == 5:
                            intento += 5
                        elif intento == 6:
                            intento += 4
                        elif intento == 7:
                            intento += 3
                        elif intento == 8:
                            intento += 2
                        elif intento == 9:
                            intento += 1
                        break
                    elif ing < nC:
                        print("El numero correcto es mayor")
                        intento-=1
                        
                    elif ing > nC:
                        print("El numero correcto es menor")
                        intento-=1
                        

                if intento == 0:
                    print("")
                    print("")
                    print(f"Intentos restantes: {intento}")
                    print(f"Te quedaste sin intentos perdiste")
                    print(f"El numero correcto era: {nC}")
                    Puntos-=20
                    print(f"{Puntos} puntos perdidos")
                    intento +=10
        except ValueError:
            print("entrada invalida")

        if dificultad == "salir":
            salida = False
    return "numero", Puntos