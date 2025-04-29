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
    # CÁLCULO DE LA ESTRUCTURA MÍNIMA
    # Se parte de la unión de todas las fronteras observadas y se propaga hacia atrás
    # (si la celda forzada no es frontera en un viento, se obliga la celda "trasera").
    # -----------------------
    M_min = [[False]*(dx+1) for _ in range(dy+1)]
    new_cells = set()
    for wind in winds:
        for (x, y) in wind['B']:
            if not M_min[y][x]:
                M_min[y][x] = True
                new_cells.add((x, y))
    while new_cells:
        next_new = set()
        for (x, y) in new_cells:
            for wind in winds:
                # Si (x,y) es frontera observada para este viento, la condición ya se cumple.
                if (x, y) in wind['B']:
                    continue
                wx = wind['wx']
                wy = wind['wy']
                xp = x - wx
                yp = y - wy
                if xp < 1 or xp > dx or yp < 1 or yp > dy:
                    continue
                if not M_min[yp][xp]:
                    M_min[yp][xp] = True
                    next_new.add((xp, yp))
        new_cells = next_new

    # -----------------------
    # CÁLCULO DE LA ESTRUCTURA MÁXIMA
    # Se parte de la rejilla llena y se eliminan (propagando en forma de cola) aquellas celdas que,
    # para algún viento, violan la condición:
    #   Si una celda (x,y) está llena y NO es una frontera observada, entonces debe tener
    #   la celda (x-wx, y-wy) llena; de lo contrario se retira.
    # -----------------------
    M_max = [[True]*(dx+1) for _ in range(dy+1)]
    
    # Función que indica si para un viento dado la celda (x,y) viola la condición.
    def violates(wind, x, y):
        if (x, y) in wind['B']:
            return False
        wx = wind['wx']
        wy = wind['wy']
        xp = x - wx
        yp = y - wy
        if xp < 1 or xp > dx or yp < 1 or yp > dy:
            return True
        return not M_max[yp][xp]
    
    q = deque()
    # Inicialización: se recorren todas las celdas y se retiran aquellas que, para al menos un viento, violan la condición.
    for y in range(1, dy+1):
        for x in range(1, dx+1):
            for wind in winds:
                if violates(wind, x, y):
                    if M_max[y][x]:
                        M_max[y][x] = False
                        q.append((x, y))
                    break
    # Propagación: si se retira una celda, sus "vecinas directas" (según cada viento) podrían quedar inválidas.
    while q:
        x, y = q.popleft()
        for wind in winds:
            wx = wind['wx']
            wy = wind['wy']
            xp = x + wx
            yp = y + wy
            if xp < 1 or xp > dx or yp < 1 or yp > dy:
                continue
            if M_max[yp][xp] and (xp, yp) not in wind['B']:
                if violates(wind, xp, yp):
                    M_max[yp][xp] = False
                    q.append((xp, yp))
    
    # -----------------------
    # SALIDA: Se imprimen ambas estructuras (mínima y máxima) separadas por una línea en blanco.
    # Cada estructura se muestra en dy líneas de dx caracteres (la esquina superior izquierda es (1,1)).
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
