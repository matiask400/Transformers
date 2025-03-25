#!/usr/bin/env python3
import sys
from collections import deque

def main():
    limit = 10
    data = []
    line_count = 0
    
    for line in sys.stdin:
        if line_count >= limit:
            break
        data.extend(line.split())
        line_count += 1
        
    if not data:
        return
    it = iter(data)
    dx = int(next(it))
    dy = int(next(it))
    k = int(next(it))
    # Cada viento se representa como un diccionario con su dirección y conjunto de fronteras (observadas)
    winds = []
    for _ in range(k):
        wx = int(next(it))
        wy = int(next(it))
        b = int(next(it))
        B = set()
        for i in range(b):
            x = int(next(it))
            y = int(next(it))
            B.add((x, y))
        winds.append({'wx': wx, 'wy': wy, 'B': B})
    
    # -----------------------
    # Cálculo de la solución MINIMAL
    # Se parte de la unión de todas las fronteras observadas; luego,
    # para cada viento, si una celda “forzada” (con molécula) no es una frontera en ese viento,
    # se obliga a tener molécula la celda “trasera” (x-wx,y-wy)
    # -----------------------
    # Inicializamos M_min (1-indexado: M_min[y][x])
    M_min = [[False]*(dx+1) for _ in range(dy+1)]
    new_cells = set()
    # Se asigna True a todas las celdas que aparecen en alguna frontera
    for wind in winds:
        for (x, y) in wind['B']:
            if not M_min[y][x]:
                M_min[y][x] = True
                new_cells.add((x, y))
    # Propagación: para cada celda recién activada, en cada viento que no la reconozca como frontera,
    # se fuerza la celda “trasera” (si está en el dominio)
    while new_cells:
        next_new = set()
        for (x, y) in new_cells:
            for wind in winds:
                # Si la celda es frontera observada en este viento, la condición se satisface
                if (x, y) in wind['B']:
                    continue
                wx = wind['wx']
                wy = wind['wy']
                xp = x - wx
                yp = y - wy
                if xp < 1 or xp > dx or yp < 1 or yp > dy:
                    # Si la vecina trasera está fuera, la condición implica que (x,y) debiera ser frontera;
                    # la consistencia del problema garantiza que esto no ocurra.
                    continue
                if not M_min[yp][xp]:
                    M_min[yp][xp] = True
                    next_new.add((xp, yp))
        new_cells = next_new

    # -----------------------
    # Cálculo de la solución MAXIMAL
    # Para cada viento se computa, mediante barrido en orden (dependiendo de la dirección),
    # el conjunto A tal que:
    #   – Si la “vecina trasera” está fuera, sólo se permite molécula si la celda es frontera.
    #   – Si está dentro, se puede llenar la celda si es frontera o si su vecina trasera ya se llenó.
    # La solución máxima es la intersección (celda a celda) de los conjuntos permitidos para cada viento.
    # -----------------------
    A_list = []
    for wind in winds:
        wx = wind['wx']
        wy = wind['wy']
        B = wind['B']
        A = [[False]*(dx+1) for _ in range(dy+1)]
        # Se determina el orden de barrido según la dirección del viento
        x_range = range(1, dx+1) if wx >= 0 else range(dx, 0, -1)
        y_range = range(1, dy+1) if wy >= 0 else range(dy, 0, -1)
        # Barrido (anidado) en el orden que garantiza que la celda trasera se procese antes
        for y in y_range:
            for x in x_range:
                xp = x - wx
                yp = y - wy
                if xp < 1 or xp > dx or yp < 1 or yp > dy:
                    # Fuera del dominio: se permite la celda únicamente si es una frontera observada
                    A[y][x] = ((x, y) in B)
                else:
                    # Si la celda es frontera se permite; de lo contrario se permite si lo fue su vecina trasera
                    A[y][x] = ((x, y) in B) or A[yp][xp]
        A_list.append(A)
    # La estructura máxima es la intersección de todas las A obtenidas
    M_max = [[True]*(dx+1) for _ in range(dy+1)]
    for y in range(1, dy+1):
        for x in range(1, dx+1):
            for A in A_list:
                if not A[y][x]:
                    M_max[y][x] = False
                    break

    # -----------------------
    # Salida: se imprime primero la estructura mínima, luego una línea vacía y la máxima.
    # Cada estructura se imprime como dy líneas de dx caracteres (el carácter '#' indica molécula y '.' indica vacío).
    # Se asume que (1,1) corresponde a la esquina superior izquierda.
    # -----------------------
    out_lines = []
    for y in range(1, dy+1):
        line = []
        for x in range(1, dx+1):
            line.append('#' if M_min[y][x] else '.')
        out_lines.append(''.join(line))
    min_output = "\n".join(out_lines)
    
    out_lines = []
    for y in range(1, dy+1):
        line = []
        for x in range(1, dx+1):
            line.append('#' if M_max[y][x] else '.')
        out_lines.append(''.join(line))
    max_output = "\n".join(out_lines)
    
    sys.stdout.write(min_output + "\n\n" + max_output)

if __name__ == '__main__':
    main()
