---

# Trabajo Práctico de Inteligencia Artificial

Este repositorio contiene dos implementaciones en Python de algoritmos de búsqueda utilizados comúnmente en el campo de la inteligencia artificial para resolver problemas de búsqueda de caminos en espacios de estados.

## Contenido

1. **Búsqueda en Anchura (BFS - Breadth-First Search)**  
   Archivo: `bfs.py`  
   Descripción: Implementación del algoritmo de búsqueda en anchura para encontrar una posición objetivo en un espacio de estados. El BFS es un método de búsqueda exhaustivo que explora todos los nodos en un nivel antes de pasar al siguiente.  
   
2. **Algoritmo A* (A-Star Search)**  
   Archivo: `a_star.py`  
   Descripción: Implementación del algoritmo A*, que combina la búsqueda en anchura con una heurística para encontrar el camino más corto de manera más eficiente. En este caso, se usa la distancia Manhattan como heurística.

## Requisitos

- Python 3.x
- No se requieren librerías externas adicionales, pero se recomienda tener instaladas las siguientes para la gestión eficiente de colas y listas de prioridad:
  - `collections` (incluida en la librería estándar de Python)
  - `heapq` (incluida en la librería estándar de Python)

## Algoritmos Implementados

### 1. Búsqueda en Anchura (BFS)

**Archivo:** `bfs.py`

#### Descripción:

El algoritmo de búsqueda en anchura (BFS) explora el espacio de estados de manera exhaustiva, empezando desde la posición inicial y explorando todas las posiciones vecinas posibles, nivel por nivel, hasta encontrar la posición objetivo.

#### Ejecución:

La función principal es `bfs(pos_inicial, pos_objetivo, movimientos_posibles)`. Los parámetros son:
- `pos_inicial`: Tupla con las coordenadas de la posición inicial.
- `pos_objetivo`: Tupla con las coordenadas de la posición objetivo.
- `movimientos_posibles`: Lista de tuplas que representan los movimientos permitidos (por ejemplo, arriba, abajo, izquierda, derecha).

El algoritmo explora todas las posibles posiciones a partir de la inicial, utilizando una cola (`deque`) para procesar las posiciones pendientes de explorar. La función devuelve un mensaje indicando si se ha encontrado la posición objetivo o no.

#### Ejemplo de Uso:

```python
pos_inicial = (0, 0)
pos_objetivo = (3, 3)
movimientos_posibles = [(0, 1), (1, 0), (0, -1), (-1, 0)]

bfs(pos_inicial, pos_objetivo, movimientos_posibles)
```

---

### 2. Algoritmo A\* (A-Star Search)

**Archivo:** `a_star.py`

#### Descripción:

El algoritmo A\* es un algoritmo de búsqueda informada que utiliza una heurística para mejorar la eficiencia en la búsqueda del camino más corto. En este caso, la heurística empleada es la **distancia Manhattan**, que calcula la suma de las distancias absolutas en el eje X y Y entre la posición actual y la posición objetivo.

#### Ejecución:

La función principal es `a_star(pos_inicial, pos_objetivo, movimientos_posibles, heuristica)`. Los parámetros son:

- `pos_inicial`: Tupla con las coordenadas de la posición inicial.
- `pos_objetivo`: Tupla con las coordenadas de la posición objetivo.
- `movimientos_posibles`: Lista de tuplas que representan los movimientos permitidos.
- `heuristica`: Función heurística que estima la distancia desde una posición actual a la posición objetivo.

El algoritmo usa una cola de prioridad (`heapq`) para seleccionar el siguiente nodo a explorar basándose en el costo acumulado desde la posición inicial y la estimación de la distancia restante al objetivo.

#### Ejemplo de Uso:

```python
pos_inicial = (0, 0)
pos_objetivo = (3, 3)
movimientos_posibles = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def heuristica(pos, objetivo):
    return abs(pos[0] - objetivo[0]) + abs(pos[1] - objetivo[1])

a_star(pos_inicial, pos_objetivo, movimientos_posibles, heuristica)
```

---

## Comparación entre BFS y A\*

- **BFS**: Explora todos los caminos posibles hasta encontrar el objetivo. Es ideal cuando los costos de los movimientos son uniformes y no se tiene información previa sobre el espacio de búsqueda. Sin embargo, puede ser menos eficiente en términos de tiempo y espacio, especialmente en espacios de estados grandes.
- **A\***: Combina búsqueda en anchura con una heurística para priorizar los caminos que parecen más prometedores. Es más eficiente que BFS en muchos casos, ya que evita explorar rutas que claramente no son óptimas. La calidad de la heurística es clave para el rendimiento.

---

## Ejecución

Para ejecutar ambos scripts, asegúrate de tener instalados los requisitos y simplemente corre los archivos en Python:

```bash
python bfs.py
python a_star.py
```

---

## Autor

- Nombre del alumno: [Gomez Yago]
- Trabajo práctico: Trabajo Practico N° 2
- Materia: Inteligencia Artificial
- Profesor: Pablo Alejandro Virgolini

---

## Conclusiones

El trabajo práctico permite comparar dos enfoques fundamentales en la búsqueda de caminos: el exhaustivo (BFS) y el heurístico (A*). En problemas donde se conoce una buena heurística, A* es significativamente más eficiente en tiempo, mientras que BFS garantiza una exploración completa, aunque puede ser menos óptimo en problemas grandes.
