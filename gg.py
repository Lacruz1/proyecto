import random

def dibujarTablero(tablero):

    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')

def ingresaLetraJugador():
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿Quieres ser X o O?')
        letra = input().upper()

    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienVaPrimero():
    if random.randint(0, 1) == 0:
        return 'computadora'
    else:
        return 'jugador'

def jugarDeNuevo():
    print('¿Quieres jugar de nuevo? (sí/no)')
    return input().lower().startswith('s')

def hacerMovimiento(tablero, letra, movimiento):
    tablero[movimiento] = letra

def esGanador(te, le):
   
    return ((te[1] == le and te[2] == le and te[3] == le) or
            (te[4] == le and te[5] == le and te[6] == le) or 
            (te[7] == le and te[8] == le and te[9] == le) or 
            (te[1] == le and te[4] == le and te[7] == le) or 
            (te[2] == le and te[5] == le and te[8] == le) or 
            (te[3] == le and te[6] == le and te[9] == le) or 
            (te[1] == le and te[5] == le and te[9] == le) or
            (te[3] == le and te[5] == le and te[7] == le))   

def obtenerCopiaTablero(tablero):
    dupeTablero = []
    for i in tablero:
        dupeTablero.append(i)
    return dupeTablero

def esEspacioLibre(tablero, movimiento):
    return tablero[movimiento] == ' '

def obtenerMovimientoJugador(tablero):
    movimiento = ' '
    while movimiento not in '1 2 3 4 5 6 7 8 9'.split() or not esEspacioLibre(tablero, int(movimiento)):
        print('¿Cuál es tu siguiente movimiento? (1-9)')
        movimiento = input()
    return int(movimiento)

def elegirMovimientoAleatorio(tablero, listaMovimientos):
    movimientosPosibles = []
    for i in listaMovimientos:
        if esEspacioLibre(tablero, i):
            movimientosPosibles.append(i)

    if len(movimientosPosibles) != 0:
        return random.choice(movimientosPosibles)
    else:
        return None

def obtenerMovimientoComputadora(tablero, letraComputadora):
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'

    for i in range(1, 10):
        copia = obtenerCopiaTablero(tablero)
        if esEspacioLibre(copia, i):
            hacerMovimiento(copia, letraComputadora, i)
            if esGanador(copia, letraComputadora):
                return i

    for i in range(1, 10):
        copia = obtenerCopiaTablero(tablero)
        if esEspacioLibre(copia, i):
            hacerMovimiento(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i

   
    movimiento = elegirMovimientoAleatorio(tablero, [1, 3, 7, 9])
    if movimiento != None:
        return movimiento

 
    if esEspacioLibre(tablero, 5):
        return 5

    
    return elegirMovimientoAleatorio(tablero, [2, 4, 6, 8])

def estaTableroLleno(tablero):
    for i in range(1, 10):
        if esEspacioLibre(tablero, i):
            return False
    return True

print('¡Bienvenido al juego del Gato!')

print('Referencia de posiciones:')
print(' 1 | 2 | 3 ')
print('-----------')
print(' 4 | 5 | 6 ')
print('-----------')
print(' 7 | 8 | 9 ')
print('--------------------------')

while True:
    elTablero = [' '] * 10
    letraJugador, letraComputadora = ingresaLetraJugador()
    turno = quienVaPrimero()
    print(turno + ' irá primero.')
    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'jugador':
            dibujarTablero(elTablero)
            movimiento = obtenerMovimientoJugador(elTablero)
            hacerMovimiento(elTablero, letraJugador, movimiento)

            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('¡Enhorabuena! ¡Has ganado!')
                juegoEnCurso = False
            else:
                if estaTableroLleno(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Empate!')
                    break
                else:
                    turno = 'computadora'
        else:
            movimiento = obtenerMovimientoComputadora(elTablero, letraComputadora)
            hacerMovimiento(elTablero, letraComputadora, movimiento)

            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('La computadora ha ganado.')
                juegoEnCurso = False
            else:
                if estaTableroLleno(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Empate!')
                    break
                else:
                    turno = 'jugador'

    if not jugarDeNuevo():
        break