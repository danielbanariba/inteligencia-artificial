import heapq
from typing import List, Tuple, Dict

# Clase Nodo para representar cada celda en el mapa
class Node:
    def __init__(self, position: Tuple[int, int], g_cost: float, h_cost: float, parent=None):
        self.position = position  # Posición del nodo en la cuadrícula
        self.g_cost = g_cost  # Costo desde el inicio hasta este nodo
        self.h_cost = h_cost  # Heurística: costo estimado desde este nodo hasta el objetivo
        self.f_cost = g_cost + h_cost  # Costo total (g_cost + h_cost)
        self.parent = parent  # Nodo padre para poder reconstruir el camino

    # Definir operador menor que para comparar nodos en la cola de prioridad
    def __lt__(self, other):
        return self.f_cost < other.f_cost

# Función heurística para estimar la distancia (Manhattan) entre dos puntos
def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

# Obtener vecinos de una celda en la cuadrícula
def get_neighbors(current: Tuple[int, int], grid: List[List[float]]) -> List[Tuple[int, int]]:
    neighbors = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = current[0] + dx, current[1] + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != -1:
            neighbors.append((new_x, new_y))
    return neighbors

# Implementación del algoritmo A* para encontrar el camino óptimo
def a_star(start: Tuple[int, int], goal: Tuple[int, int], grid: List[List[float]]) -> List[Tuple[int, int]]:
    open_list = []  # Lista de nodos a explorar
    closed_set = set()  # Conjunto de nodos ya explorados
    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Devolver el camino desde el inicio al objetivo
        
        closed_set.add(current_node.position)
        
        for neighbor_pos in get_neighbors(current_node.position, grid):
            if neighbor_pos in closed_set:
                continue
            
            neighbor_g_cost = current_node.g_cost + grid[neighbor_pos[0]][neighbor_pos[1]]
            neighbor_h_cost = heuristic(neighbor_pos, goal)
            neighbor_node = Node(neighbor_pos, neighbor_g_cost, neighbor_h_cost, current_node)
            
            if neighbor_node not in open_list:
                heapq.heappush(open_list, neighbor_node)
            else:
                # Actualizar el nodo si este camino es mejor
                for i, node in enumerate(open_list):
                    if node.position == neighbor_pos and node.g_cost > neighbor_g_cost:
                        open_list[i] = neighbor_node
                        heapq.heapify(open_list)
                        break
    
    return []  # No se encontró un camino válido

# Función para imprimir la cuadrícula y la ruta encontrada
def print_grid(grid: List[List[float]], path: List[Tuple[int, int]] = None):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if path and (i, j) in path:
                print("* ", end="")
            elif cell == -1:
                print("# ", end="")
            else:
                print(f"{cell:.1f} ", end="")
        print()

# Función principal para interactuar con el usuario y ejecutar el algoritmo A*
def main():
    print("Bienvenido al planificador de ruta para vehículo robot")
    
    # Ingresar dimensiones de la cuadrícula
    rows = int(input("Ingrese el número de filas del mapa: "))
    cols = int(input("Ingrese el número de columnas del mapa: "))
    
    # Ingresar valores de la cuadrícula
    print("Ingrese los valores del mapa (use -1 para obstáculos, y valores entre 0 y 1 para el tiempo de desplazamiento):")
    grid = []
    for i in range(rows):
        row = input(f"Fila {i+1} (separe los valores con espacios): ").split()
        grid.append([float(x) for x in row])
    
    # Ingresar posiciones de inicio y objetivo
    start_x, start_y = map(int, input("Ingrese las coordenadas de inicio (x y): ").split())
    goal_x, goal_y = map(int, input("Ingrese las coordenadas de destino (x y): ").split())
    
    start = (start_x, start_y)
    goal = (goal_x, goal_y)
    
    print("\nMapa ingresado:")
    print_grid(grid)
    
    path = a_star(start, goal, grid)
    
    if path:
        print("\n¡Ruta encontrada!")
        print("Ruta:", path)
        print("Costo total de la ruta:", sum(grid[x][y] for x, y in path))
        
        print("\nMapa con la ruta marcada (*):")
        print_grid(grid, path)
    else:
        print("\nNo se encontró una ruta válida.")

if __name__ == "__main__":
    main()