#!/usr/bin/env pypy3
import sys
import sys
input_data = sys.stdin.buffer.read().split()
it = iter(input_data)
def ni():
    return int(next(it))
    
dx = ni()
dy = ni()
k = ni()

# Convertir dimensiones: usaremos índices 0..dx-1 y 0..dy-1.
# Para cada viento, guardaremos dos matrices (listas de listas de enteros) de tamaño dy x dx:
#   pos[d][y][x]: posición de la celda (x,y) en la cadena del viento d.
#   chainR[d][y][x]: valor de R para la cadena; si la cadena aún no ha tenido celda observada, se guarda -1.
# Una celda estará "permitida" (para cualquier estructura) respecto a un viento si chainR != -1,
# lo que significa que en la cadena existe al menos un límite observado y la celda está en o después de él.
# En la estructura mínima se llenan solo las celdas que sean forzadas en al menos un viento (pos == chainR).

# Guardamos para cada viento su vector y su conjunto de observados (convertidos a índices 0-indexados)
vientos = []
for _ in range(k):
    wx = ni()
    wy = ni()
    b = ni()
    obs = set()
    for _ in range(b):
        ox = ni() - 1
        oy = ni() - 1
        obs.add((ox, oy))
    vientos.append((wx, wy, obs))

# Para cada viento, inicializamos matrices de pos y chainR
# Usamos listas de listas de tamaño dy x dx (índice [y][x])
pos_list = []
chainR_list = []
for (wx, wy, obs) in vientos:
    pos_mat = [[-1] * dx for _ in range(dy)]
    chainR_mat = [[-1] * dx for _ in range(dy)]
    # Recorremos toda la grilla para encontrar "celdas inicio" de cadena para este viento.
    for y in range(dy):
        for x in range(dx):
            # Una celda (x,y) es inicio de cadena si (x-wx, y-wy) está fuera de rango.
            prev_x = x - wx
            prev_y = y - wy
            if 0 <= prev_x < dx and 0 <= prev_y < dy:
                continue  # no es inicio
            # Iniciamos una cadena desde (x,y)
            cur_x = x
            cur_y = y
            pos = 0
            chain_obs = -1  # se actualizará cuando se encuentre la primera celda observada
            while 0 <= cur_x < dx and 0 <= cur_y < dy:
                # Si aún no se ha marcado la celda observada en esta cadena y la celda es observada, la marcamos.
                if chain_obs == -1 and (cur_x, cur_y) in obs:
                    chain_obs = pos
                pos_mat[cur_y][cur_x] = pos
                # IMPORTANTE: se asigna chain_obs sólo si ya se encontró; sino, permanece -1.
                chainR_mat[cur_y][cur_x] = chain_obs
                pos += 1
                cur_x += wx
                cur_y += wy
    pos_list.append(pos_mat)
    chainR_list.append(chainR_mat)

# Ahora, para cada celda, combinamos las restricciones de todos los vientos.
# Una celda (x,y) podrá contener molécula en la estructura máxima si y solo si
# para cada viento d, la celda pertenece a una cadena que tiene algún observado (chainR != -1).
# En la mínima se llenan solo aquellas celdas que, además, sean forzadas en al menos un viento
# (es decir, pos == chainR en al menos un viento).

# Creamos las grillas de caracteres para la solución mínima y máxima.
# Nota: la salida debe tener la fila 1 en la parte superior; internamente usamos 0-indexado
# donde y=0 es la primera fila (parte inferior) por facilidad, así que invertiremos las filas a la salida.
min_grid = [['.'] * dx for _ in range(dy)]
max_grid = [['.'] * dx for _ in range(dy)]

for y in range(dy):
    for x in range(dx):
        allowed = True
        forced = False
        for d in range(k):
            # Para cada viento, si la cadena no tiene ningún observado (chainR == -1), la celda no puede llenarse.
            if chainR_list[d][y][x] == -1:
                allowed = False
                break
            # Si en algún viento la celda es la primera observada en la cadena (pos == chainR), se fuerza su llenado en la mínima.
            if pos_list[d][y][x] == chainR_list[d][y][x]:
                forced = True
        if allowed:
            max_grid[y][x] = '#'
            if forced:
                min_grid[y][x] = '#'
            # Sino, en la estructura mínima se deja vacío para minimizar moléculas.
        # Si no está permitido en algún viento, debe quedar vacío en ambas.
        
# Imprimir la salida: primero la estructura mínima, luego una línea en blanco, luego la máxima.
# Se requiere que la celda (1,1) corresponda a la esquina superior izquierda.
# Por ello, imprimimos las filas en orden descendente de y.
out_lines = []
for row in range(dy-1, -1, -1):
    out_lines.append("".join(min_grid[row]))
out_lines.append("")
for row in range(dy-1, -1, -1):
    out_lines.append("".join(max_grid[row]))
sys.stdout.write("\n".join(out_lines))
