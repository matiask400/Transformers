#include <bits/stdc++.h>
using namespace std;
 
// Convert (x,y) (0-indexado) en índice lineal para una grilla de ancho 'dx'
inline int idx(int x, int y, int dx) {
    return y * dx + x;
}
 
// Estructura para cada viento (direction)
struct Wind {
    int wx, wy;
    // vector<bool> de tamaño dx*dy: obs[i] es true si la celda está observada
    vector<bool> obs;
};
 
// Para almacenar la partición en cadenas para un viento.
// Cada cadena tiene un vector de celdas (índices lineales) en el orden de recorrido.
// Además, se guarda el índice (dentro del vector) de la celda que es la entrada según los datos (o -1 si no hay).
struct Chain {
    vector<int> cells;
    int inputBoundary; // posición en 'cells' de la celda observada (según la entrada), o -1 si ninguna.
};
 
// Para cada viento, almacenaremos todas sus cadenas.
typedef vector<Chain> Chains;
 
// --- Función para particionar la grilla en cadenas para un viento dado ---
Chains partitionChains(const Wind &wind, int dx, int dy) {
    int dxy = dx * dy;
    vector<bool> used(dxy, false);
    Chains chains;
    // Recorrer todas las celdas; una celda es inicio de cadena si su "predecesor" p - d está fuera.
    for (int y = 0; y < dy; y++){
        for (int x = 0; x < dx; x++){
            int i = idx(x,y,dx);
            // Predecesor: (x - wx, y - wy)
            int px = x - wind.wx, py = y - wind.wy;
            if(px >= 0 && px < dx && py >= 0 && py < dy) continue; // no es inicio
            // Iniciar cadena desde (x,y)
            Chain C;
            int pos = 0;
            int cx = x, cy = y;
            int inputB = -1;
            while(cx >= 0 && cx < dx && cy >= 0 && cy < dy) {
                int ci = idx(cx, cy, dx);
                C.cells.push_back(ci);
                // Si aún no se ha asignado la entrada y esta celda está observada en los datos, se fija
                if(inputB == -1 && wind.obs[ci])
                    inputB = pos;
                pos++;
                cx += wind.wx;
                cy += wind.wy;
            }
            C.inputBoundary = inputB;
            // Marcar todas las celdas de esta cadena como usadas
            for (int ci : C.cells)
                used[ci] = true;
            chains.push_back(C);
        }
    }
    return chains;
}
 
// --- Función para calcular, en una estructura X (vector<char> de tamaño dxy, '1' = molecule, '0' = empty),
// la "frontera" para un viento: para cada cadena, se retorna el índice (en la cadena) de la primera celda llena, o -1 si ninguna.
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
 
// --- Función que verifica si, para un viento, la frontera actual (obtenida de X)
// coincide con la frontera requerida según la entrada (para cada cadena).
bool checkBoundaries(const Chains &chains, const vector<int> &boundaries) {
    // Para cada cadena, si la cadena tenía entrada (inputBoundary != -1), la frontera debe ser igual;
    // si no había entrada, no debe haber molécula.
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
            // (1,1) es esquina superior izquierda
            int index = idx(ox-1, oy-1, dx);
            winds[i].obs[index] = true;
        }
    }
 
    // Calcular la estructura máxima X_max:
    // Una celda p se puede llenar si, para cada viento, p pertenece a una cadena que tiene una entrada
    // (es decir, se observó al menos una molécula en esa cadena) y su "orden" en la cadena es >= el de la entrada.
    vector<char> X_max(dxy, '0');
    for (int i = 0; i < dxy; i++){
        bool allowed = true;
        // Para cada viento, simulamos la cadena "virtual" que contiene la celda i.
        int x = i % dx, y = i / dx;
        for (int d = 0; d < k; d++){
            // Determinar el "inicio" de la cadena para viento d a la que pertenece (x,y):
            int cx = x, cy = y;
            while(true){
                int px = cx - winds[d].wx, py = cy - winds[d].wy;
                if(px < 0 || px >= dx || py < 0 || py >= dy) break;
                cx = px; cy = py;
            }
            // Ahora, recorre la cadena desde (cx,cy) hasta (x,y) para determinar el orden y la entrada.
            int order = 0;
            int inputOrder = -1;
            int tx = cx, ty = cy;
            bool reached = false;
            while(tx != x || ty != y){
                if(winds[d].obs[idx(tx,ty,dx)] && inputOrder == -1)
                    inputOrder = order;
                order++;
                tx += winds[d].wx; ty += winds[d].wy;
                if(tx < 0 || tx >= dx || ty < 0 || ty >= dy) break; // no debería pasar
            }
            // Revisar la celda (x,y) también:
            if(winds[d].obs[idx(x,y,dx)] && inputOrder == -1)
                inputOrder = order;
            // Si la cadena no tiene entrada, p no puede estar lleno.
            if(inputOrder == -1) { allowed = false; break; }
            // p está en orden 'order'; debe ser >= inputOrder.
            if(order < inputOrder) { allowed = false; break; }
        }
        if(allowed) X_max[i] = '1';
    }
 
    // Ahora, construir las particiones en cadenas para cada viento (usando la función definida)
    vector<Chains> windChains(k);
    for (int d = 0; d < k; d++){
        windChains[d] = partitionChains(winds[d], dx, dy);
    }
 
    // Definir X_min como copia de X_max; sobre X_min intentaremos quitar moléculas sin alterar las fronteras.
    vector<char> X_min = X_max;
 
    // Para cada viento, precomputamos las fronteras actuales (según X_min) por cadena.
    vector<vector<int>> currentBoundaries(k);
    for (int d = 0; d < k; d++){
        currentBoundaries[d] = computeBoundaries(windChains[d], X_min);
    }
 
    // Función lambda que, para cada viento d, actualiza la frontera de la cadena a la que pertenece la celda p.
    auto updateChainBoundary = [&](int d, int chainIdx) {
        const Chain &C = windChains[d][chainIdx];
        int newB = -1;
        for (int pos = 0; pos < (int)C.cells.size(); pos++){
            if(X_min[C.cells[pos]] == '1') { newB = pos; break; }
        }
        currentBoundaries[d][chainIdx] = newB;
    };
 
    // Ahora, intentamos quitar (poner en '0') de X_min las moléculas que no son "mandatorias".
    // Una célula p es mandatoria para viento d si p es la frontera (primer 1 en la cadena) y además
    // la entrada (según los datos) es en esa posición; en ese caso no se puede quitar.
    // Se recorre la grilla; si p está lleno y para cada viento d en cuyo chain p aparece:
    //    si p es la frontera en ese cadena, debe coincidir con la entrada; de lo contrario, se puede quitar.
    // Se realizan pasadas hasta que no se pueda quitar nada.
    bool changed = true;
    while(changed) {
        changed = false;
        // Recorrer todas las celdas; para cada p con X_min[p]=='1' que no sea mandatoria en ningún viento,
        // probar a quitarla y verificar que, para cada viento, la frontera en la cadena correspondiente sigue siendo la misma.
        for (int i = 0; i < dxy; i++){
            if(X_min[i] == '0') continue;
            bool mandatory = false;
            // Para cada viento, averiguar en qué cadena está i.
            int x = i % dx, y = i / dx;
            for (int d = 0; d < k; d++){
                // Hallar el inicio de la cadena para viento d a la que pertenece i.
                int cx = x, cy = y;
                while(true){
                    int px = cx - winds[d].wx, py = cy - winds[d].wy;
                    if(px < 0 || px >= dx || py < 0 || py >= dy) break;
                    cx = px; cy = py;
                }
                // Encontrar el identificador de la cadena entre las ya particionadas.
                // Se busca la cadena cuyo primer celda sea (cx,cy).
                int chainId = -1;
                for (int j = 0; j < (int)windChains[d].size(); j++){
                    int c = windChains[d][j].cells[0];
                    int ccx = c % dx, ccy = c / dx;
                    if(ccx == cx && ccy == cy) { chainId = j; break; }
                }
                if(chainId == -1) continue; // no debería suceder
                // Si i es the boundary cell for viento d en esa cadena y la entrada es exactamente i, es mandatoria.
                int bpos = currentBoundaries[d][chainId];
                if(bpos != -1) {
                    int boundaryCell = windChains[d][chainId].cells[bpos];
                    if(boundaryCell == i && bpos == windChains[d][chainId].inputBoundary)
                        mandatory = true;
                }
            }
            if(mandatory) continue; // no se puede quitar p
            // Probar a quitar p: poner X_min[i] = '0' temporalmente
            X_min[i] = '0';
            bool valid = true;
            // Actualizar fronteras de las cadenas en las que i aparece y verificar que coinciden con la entrada.
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
                // Revert la remoción
                X_min[i] = '1';
                // Y restablecer fronteras (para las cadenas afectadas) volviendo a computarlas en X_min
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
 
    // Preparar salidas: convertir X_min y X_max (vectores lineales) en grillas de dy filas y dx columnas.
    vector<string> minGrid(dy, string(dx, '.'));
    vector<string> maxGrid(dy, string(dx, '.'));
    for (int y = 0; y < dy; y++){
        for (int x = 0; x < dx; x++){
            int i = idx(x, y, dx);
            minGrid[y][x] = X_min[i];
            maxGrid[y][x] = X_max[i];
        }
    }
 
    // Imprimir: la primera grilla (mínima), luego una línea en blanco, luego la máxima.
    // Recordar: la celda (1,1) es la esquina superior izquierda, es decir, la fila 0.
    for (int y = 0; y < dy; y++){
        cout << minGrid[y] << "\n";
    }
    cout << "\n";
    for (int y = 0; y < dy; y++){
        cout << maxGrid[y] << "\n";
    }
 
    return 0;
}
