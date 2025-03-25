#include <bits/stdc++.h>
using namespace std;
 
// Convierte (x,y) (0-indexado) en índice lineal para una grilla de ancho 'dx'
inline int idx(int x, int y, int dx) {
    return y * dx + x;
}
 
// Estructura para cada viento (dirección)
struct Wind {
    int wx, wy;
    // Vector de tamaño dx*dy: obs[i] es true si la celda está observada.
    vector<bool> obs;
};
 
// Para almacenar la partición en cadenas para un viento dado.
// Cada cadena tiene un vector de celdas (índices lineales) en el orden de recorrido.
// Además, se guarda el índice (dentro del vector) de la celda observada según los datos (o -1 si ninguna).
struct Chain {
    vector<int> cells;
    int inputBoundary; // posición en 'cells' de la celda observada (según la entrada), o -1 si ninguna.
};
 
// Para cada viento, almacenaremos todas sus cadenas.
typedef vector<Chain> Chains;
 
// Función para particionar la grilla en cadenas para un viento dado
Chains partitionChains(const Wind &wind, int dx, int dy) {
    int dxy = dx * dy;
    vector<bool> used(dxy, false);
    Chains chains;
    // Una celda es inicio de cadena si su predecesor (p - d) está fuera de rango.
    for (int y = 0; y < dy; y++){
        for (int x = 0; x < dx; x++){
            int i = idx(x,y,dx);
            int px = x - wind.wx, py = y - wind.wy;
            if(px >= 0 && px < dx && py >= 0 && py < dy)
                continue;
            Chain C;
            int pos = 0;
            int inputB = -1;
            int cx = x, cy = y;
            while(cx >= 0 && cx < dx && cy >= 0 && cy < dy) {
                int ci = idx(cx,cy,dx);
                C.cells.push_back(ci);
                if(inputB == -1 && wind.obs[ci])
                    inputB = pos;
                pos++;
                cx += wind.wx;
                cy += wind.wy;
            }
            C.inputBoundary = inputB;
            for (int ci : C.cells)
                used[ci] = true;
            chains.push_back(C);
        }
    }
    return chains;
}
 
// Calcula, para una partición de cadenas y una estructura X (vector<char> de tamaño dxy, donde '1' indica molécula),
// la frontera de cada cadena: para cada cadena se retorna el índice (dentro de la cadena) de la primera celda llena,
// o -1 si ninguna.
vector<int> computeBoundaries(const Chains &chains, const vector<char> &X) {
    vector<int> boundaries;
    for (const auto &C : chains) {
        int b = -1;
        for (int pos = 0; pos < (int)C.cells.size(); pos++){
            if(X[C.cells[pos]] == '1') { b = pos; break; }
        }
        boundaries.push_back(b);
    }
    return boundaries;
}
 
// Verifica, para una partición de cadenas y unas fronteras calculadas, que cada cadena cumple con la entrada dada.
bool checkBoundaries(const Chains &chains, const vector<int> &boundaries) {
    for (size_t i = 0; i < chains.size(); i++){
        if(chains[i].inputBoundary != -1) {
            if(boundaries[i] != chains[i].inputBoundary)
                return false;
        } else {
            if(boundaries[i] != -1)
                return false;
        }
    }
    return true;
}
 
// --- MAIN ---
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int dx, dy, k;
    cin >> dx >> dy >> k;
    int dxy = dx * dy;
 
    // Leer datos de la grilla y de cada viento.
    vector<Wind> winds(k);
    for (int i = 0; i < k; i++){
        int wx, wy, b;
        cin >> wx >> wy >> b;
        winds[i].wx = wx;
        winds[i].wy = wy;
        winds[i].obs.assign(dxy, false);
        for (int j = 0; j < b; j++){
            int ox, oy;
            cin >> ox >> oy;
            int index = idx(ox - 1, oy - 1, dx); // (1,1) es esquina superior izquierda.
            winds[i].obs[index] = true;
        }
    }
 
    // Calcular la estructura máxima X_max:
    // Una celda p se puede llenar (representada internamente como '1') si, para cada viento,
    // p pertenece a una cadena que tiene al menos una celda observada y su "orden" en la cadena es >=
    // el orden de la primera celda observada (inputBoundary).
    vector<char> X_max(dxy, '0');
    for (int i = 0; i < dxy; i++){
        bool allowed = true;
        int x = i % dx, y = i / dx;
        for (int d = 0; d < k; d++){
            int cx = x, cy = y;
            int order = 0;
            int inputOrder = -1;
            while(true){
                int px = cx - winds[d].wx, py = cy - winds[d].wy;
                if(px < 0 || px >= dx || py < 0 || py >= dy) break;
                cx = px; cy = py;
            }
            int tx = cx, ty = cy;
            while(true){
                if(tx < 0 || tx >= dx || ty < 0 || ty >= dy) break;
                if(winds[d].obs[idx(tx,ty,dx)] && inputOrder == -1)
                    inputOrder = order;
                if(tx == x && ty == y) break;
                order++;
                tx += winds[d].wx; ty += winds[d].wy;
            }
            if(inputOrder == -1 || order < inputOrder) { allowed = false; break; }
        }
        if(allowed) X_max[i] = '1';
    }
 
    // Particionar en cadenas para cada viento.
    vector<Chains> windChains(k);
    for (int d = 0; d < k; d++){
        windChains[d] = partitionChains(winds[d], dx, dy);
    }
 
    // Definir X_min como copia de X_max; sobre X_min intentaremos quitar moléculas innecesarias.
    vector<char> X_min = X_max;
 
    // Pre-calcular fronteras actuales para cada viento.
    vector<vector<int>> currentBoundaries(k);
    for (int d = 0; d < k; d++){
        currentBoundaries[d] = computeBoundaries(windChains[d], X_min);
    }
 
    // Función lambda para actualizar la frontera de una cadena en un viento.
    auto updateChainBoundary = [&](int d, int chainIdx) {
        const Chain &C = windChains[d][chainIdx];
        int newB = -1;
        for (int pos = 0; pos < (int)C.cells.size(); pos++){
            if(X_min[C.cells[pos]] == '1') { newB = pos; break; }
        }
        currentBoundaries[d][chainIdx] = newB;
    };
 
    // Proceso de poda: intentamos quitar moléculas de X_min que no sean "mandatorias".
    bool changed = true;
    while(changed) {
        changed = false;
        for (int i = 0; i < dxy; i++){
            if(X_min[i] == '0') continue;
            bool mandatory = false;
            int x = i % dx, y = i / dx;
            for (int d = 0; d < k; d++){
                int cx = x, cy = y;
                while(true){
                    int px = cx - winds[d].wx, py = cy - winds[d].wy;
                    if(px < 0 || px >= dx || py < 0 || py >= dy) break;
                    cx = px; cy = py;
                }
                int chainId = -1;
                for (int j = 0; j < (int)windChains[d].size(); j++){
                    int c = windChains[d][j].cells[0];
                    int ccx = c % dx, ccy = c / dx;
                    if(ccx == cx && ccy == cy) { chainId = j; break; }
                }
                if(chainId == -1) continue;
                int bpos = currentBoundaries[d][chainId];
                if(bpos != -1) {
                    int boundaryCell = windChains[d][chainId].cells[bpos];
                    if(boundaryCell == i && bpos == windChains[d][chainId].inputBoundary)
                        mandatory = true;
                }
            }
            if(mandatory) continue;
            X_min[i] = '0'; // intentamos quitar
            bool valid = true;
            for (int d = 0; d < k; d++){
                int x = i % dx, y = i / dx;
                int cx = x, cy = y;
                while(true){
                    int px = cx - winds[d].wx, py = cy - winds[d].wy;
                    if(px < 0 || px >= dx || py < 0 || py >= dy) break;
                    cx = px; cy = py;
                }
                int chainId = -1;
                for (int j = 0; j < (int)windChains[d].size(); j++){
                    int c = windChains[d][j].cells[0];
                    int ccx = c % dx, ccy = c / dx;
                    if(ccx == cx && ccy == cy) { chainId = j; break; }
                }
                if(chainId == -1) continue;
                updateChainBoundary(d, chainId);
                if(currentBoundaries[d][chainId] != windChains[d][chainId].inputBoundary) {
                    valid = false;
                    break;
                }
            }
            if(valid) {
                changed = true;
            } else {
                X_min[i] = '1'; // revertir
                for (int d = 0; d < k; d++){
                    int x = i % dx, y = i / dx;
                    int cx = x, cy = y;
                    while(true){
                        int px = cx - winds[d].wx, py = cy - winds[d].wy;
                        if(px < 0 || px >= dx || py < 0 || py >= dy) break;
                        cx = px; cy = py;
                    }
                    int chainId = -1;
                    for (int j = 0; j < (int)windChains[d].size(); j++){
                        int c = windChains[d][j].cells[0];
                        int ccx = c % dx, ccy = c / dx;
                        if(ccx == cx && ccy == cy) { chainId = j; break; }
                    }
                    if(chainId == -1) continue;
                    updateChainBoundary(d, chainId);
                }
            }
        }
    }
 
    // Preparar salidas: convertir X_min y X_max a grillas de dy filas y dx columnas,
    // usando '#' para molécula (cuando el valor es '1') y '.' para vacío (cuando es '0').
    vector<string> minGrid(dy, string(dx, '.'));
    vector<string> maxGrid(dy, string(dx, '.'));
    for (int y = 0; y < dy; y++){
        for (int x = 0; x < dx; x++){
            int i = idx(x,y,dx);
            minGrid[y][x] = (X_min[i]=='1' ? '#' : '.');
            maxGrid[y][x] = (X_max[i]=='1' ? '#' : '.');
        }
    }
 
    // Imprimir la salida: primero la estructura mínima, luego una línea en blanco, luego la estructura máxima.
    // Se asume que (1,1) es la esquina superior izquierda (fila 0).
    for (int y = 0; y < dy; y++){
        cout << minGrid[y] << "\n";
    }
    cout << "\n";
    for (int y = 0; y < dy; y++){
        cout << maxGrid[y] << "\n";
    }
 
    return 0;
}
