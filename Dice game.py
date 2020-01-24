#Projecto de los dados
import random

#a) Hacer una partida con M rondas y N jugadores.
    #Se guardarán en un diccionario.
def dado():
    """Función que devuelve un número entre 1 y 6"""
    return random.randint(1, 6)


def lanzamiento():
    """Devuelve una tupla ordenada de un par de dados"""
    pares = sorted((dado(), dado()))
    return tuple(pares)


def rondas(numRondas):
    """Devuelve un diccionario por compresión, con {clave => valor}
    igual a Ronda N => TuplaDados."""
    return dict(("Ronda " + str(i), lanzamiento())
                for i in range(numRondas))

def partida(numRondas, numJugadores):
    """Devuelve un diccionario por compresión, con {clave => valor}
    igual a Jugador M => Lanzamiento en Ronda N."""
    return dict(("Jugador " + str(i), rondas(numRondas))
                for i in range(numJugadores))

"""Variables con info de la partida"""
nRondas = 3
nJugadores = 3
logPartida = partida(nRondas, nJugadores)

#b) Saber que pares de dados no han salido;
    # Calcula también todos los posibles resultados.
""" 1) Coleccion con los posibles lanzamientos
     2) Lista con los posibles lanzamientos ordenados"""
posibles = set((x, y) for x in range(1, 7) for y in range (1, 7) if y >= x)
posiblesOrdenados = sorted(posibles)

def paresObtenidos(diccio):
    """Devuelve un lista por compresión que contiene dentro de tuplas
    todos los lanzamientos que han salido"""
    return [diccio.get(x).get(y) for x in diccio
            for y in diccio.get(x)]

""" 1) Coleccion con los lanzamientos que han salido
     2) Lista con los lanzamientos anteriores ordenados"""
logPartidaSet = set(paresObtenidos(logPartida))
logPartidaOrdenado = sorted(logPartidaSet)

def paresNoObtenidos(obtenidos, posibles):
    """Devuelve una collecion con los lanzamientos que no han salido"""
    return (posibles - obtenidos)

"""Lista ordenada de los lanzamientos que no han salido"""
noObtenidos = sorted(paresNoObtenidos(logPartidaSet, posibles))

#c) Sumar la puntuacion de cada jugador.
    # Sacar al ganador

def puntuacionJugador():
    """Devuelve en un diccionario con cada jugador y su puntuacion total"""
    jugadorPuntos = 0
    puntuaciones = {}
    for i in logPartida:
        for o in logPartida.get(i):
            tirada = logPartida.get(i).get(o)
            jugadorPuntos += (tirada[0] + tirada[1])
        puntuaciones[i] = jugadorPuntos
        jugadorPuntos = 0
    return puntuaciones

"""Variable donde se almacena cada jugador con su puntuación"""
puntuaciones = puntuacionJugador()

def ganador():
    """Devuelve el ganador con su puntuacion"""
    ganador = max(puntuaciones, key=puntuaciones.get)
    return(ganador, puntuaciones[ganador])

"""Variable donde se almacena el ganador"""
ganador = ganador()


def printer():
    """Imprime toda la info por pantalla"""
    print('-------------------')
    print('Han participado: ', nJugadores, ' jugadores.')
    print('Han jugado: ', nRondas, ' rondas.')
    print('-------------------')
    for i in logPartida:
        print('*** ', i, ' ***')
        for o in logPartida.get(i):
            print(o)
            print(logPartida.get(i).get(o))
        print('-> Puntuación final: ', puntuaciones.get(i), ' <-')
        print('-------------------')
    print('El jugador con más puntos ha sido:', ganador)
    print('-------------------')
    print('Han salido los lanzamientos: ', logPartidaOrdenado)
    print('No han salido los lanzamientos: ', noObtenidos)
    
        



    
