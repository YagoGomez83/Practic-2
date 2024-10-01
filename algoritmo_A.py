import heapq

def a_star(pos_inicial, pos_objetivo, movimientos_posibles, heuristica):
    # Inicializamos una cola de prioridad
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, pos_inicial))
    
    # Diccionario para almacenar los costos
    costos = {pos_inicial: 0}
    
    # Diccionario para registrar las rutas
    rutas = {pos_inicial: None}
    
    while cola_prioridad:
        # Extraemos el nodo con el menor costo (f(n) = g(n) + h(n))
        _, actual = heapq.heappop(cola_prioridad)
        
        # Si llegamos al objetivo, reconstruimos la ruta
        if actual == pos_objetivo:
            print("Ruta encontrada:", reconstruir_ruta(rutas, pos_objetivo))
            return
        
        # Exploramos los movimientos posibles
        for movimiento in movimientos_posibles:
            nueva_posicion = (actual[0] + movimiento[0], actual[1] + movimiento[1])
            nuevo_costo = costos[actual] + 1  # Suponiendo costo uniforme para cada movimiento
            
            # Si la nueva posición no ha sido explorada o tiene un menor costo
            if nueva_posicion not in costos or nuevo_costo < costos[nueva_posicion]:
                costos[nueva_posicion] = nuevo_costo
                prioridad = nuevo_costo + heuristica(nueva_posicion, pos_objetivo)
                heapq.heappush(cola_prioridad, (prioridad, nueva_posicion))
                rutas[nueva_posicion] = actual
    
    print("No se encontró la ruta.")

def reconstruir_ruta(rutas, posicion_final):
    ruta = []
    actual = posicion_final
    while actual is not None:
        ruta.append(actual)
        actual = rutas[actual]
    return ruta[::-1]

# Ejemplo de función heurística (distancia Manhattan)
def heuristica(pos, objetivo):
    return abs(pos[0] - objetivo[0]) + abs(pos[1] - objetivo[1])
