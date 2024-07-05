import matplotlib.pyplot as plt
import numpy as np

def draw_example():
    # Crear una cuadrícula 5x5 con valores de tiempo y obstáculos
    grid = np.array([
        [0.1, 0.2, 0.3, 0.4, 0.5],
        [0.2, -1, 0.2, -1, 0.4],
        [0.3, 0.2, 0.1, 0.2, 0.3],
        [-1, 0.3, -1, 0.4, 0.2],
        [0.5, 0.4, 0.3, 0.2, 0.1]
    ])

    # Definir puntos de inicio (A) y destino (B)
    start = (0, 0)
    goal = (4, 4)

    # Ruta óptima encontrada (por ejemplo, esta ruta puede variar)
    path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap='gray', vmin=-1, vmax=1)

    # Marcar los obstáculos
    for (j, i), value in np.ndenumerate(grid):
        if value == -1:
            ax.text(i, j, 'X', ha='center', va='center', color='red')

    # Marcar el punto de inicio y destino
    ax.text(start[1], start[0], 'A', ha='center', va='center', color='blue')
    ax.text(goal[1], goal[0], 'B', ha='center', va='center', color='green')

    # Dibujar la ruta óptima
    for (i, j) in path:
        ax.text(j, i, '*', ha='center', va='center', color='yellow')

    # Mostrar los valores de g(n), h(n), y f(n) para cada nodo en la ruta
    g_costs = [0, 0.1, 0.3, 0.5, 0.6, 0.8, 1.0, 1.2, 1.3]
    h_costs = [0.8, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
    f_costs = [sum(x) for x in zip(g_costs, h_costs)]
    
    for k, (i, j) in enumerate(path):
        ax.text(j, i + 0.2, f'g={g_costs[k]:.1f}', ha='center', va='center', color='black', fontsize=8)
        ax.text(j, i - 0.2, f'h={h_costs[k]:.1f}', ha='center', va='center', color='black', fontsize=8)
        ax.text(j, i + 0.4, f'f={f_costs[k]:.1f}', ha='center', va='center', color='black', fontsize=8)

    # Configurar la cuadrícula
    ax.set_xticks(np.arange(grid.shape[1] + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(grid.shape[0] + 1) - 0.5, minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.tick_params(which="minor", size=0)
    ax.tick_params(which="major", bottom=False, left=False, labelbottom=False, labelleft=False)

    plt.title('Ejemplo de Planificación de Ruta con A*')
    plt.show()

draw_example()