from collections import deque

def bfs(pos_inicial, pos_objetivo, movimientos_posibles):
    # Creamos una cola para almacenar las posiciones por explorar
    cola = deque([pos_inicial])
    # Set para registrar las posiciones visitadas
    visitados = set()
    visitados.add(pos_inicial)
    
    # Mientras haya posiciones en la cola
    while cola:
        # Extraemos la primera posición de la cola
        actual = cola.popleft()
        
        # Si la posición actual es la posición objetivo, finalizamos
        if actual == pos_objetivo:
            print("Posición encontrada:", actual)
            return
        
        # Exploramos las posiciones vecinas posibles
        for movimiento in movimientos_posibles:
            nueva_posicion = (actual[0] + movimiento[0], actual[1] + movimiento[1])
            if nueva_posicion not in visitados:
                visitados.add(nueva_posicion)
                cola.append(nueva_posicion)
    
    print("No se encontró la posición.")
