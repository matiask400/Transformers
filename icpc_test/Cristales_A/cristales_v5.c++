#include <bits/stdc++.h>
using namespace std;
 
// Función auxiliar para convertir (x,y) (0-indexado) en índice lineal (fila×ancho + columna)
inline int idx(int x, int y, int dx) {
    return y * dx + x;
}
 
// Estructura que almacena los datos de un viento.
struct Wind {
    int wx, wy;
    // Vector de observados (de tamaño dx*dy); true si la celda fue observada según la entrada.
    vector<bool> obs;
};
 
// Para cada cadena (rayo) en un viento, almacenamos:
struct Chain {
    vector<int> cells;         // Índices lineales de las celdas en orden (0,1,2,…)
    vector<int> obsPositions;  // Posiciones (en la cadena) donde se observó una molécula (según datos)
};
 
// Para cada viento d, queremos obtener un vector de tamaño (dx*dy) (inicializado con valor “permitido” y “forzado” para cada celda)
// que indiquen las condiciones impuestas por ese viento. Es decir, para cada celda p (índice i):
//   allowed_d[p] = true si, en la cadena a la que pertenece p, se cumple que:
//       – La cadena tiene al menos una observación (R no vacía)
//       – p está en una posición pos que NO es forzada a estar vacía (no coincide con r-1 para algún r en R con r > R[0])
//       – Además, p debe estar en o después de la primera observación (pos >= R[0]).
//   forced_d[p] = true si p es exactamente una de las observaciones (es decir, su posición pos está en R).
 
// Dadas las dimensiones y la información de un viento, esta función rellena los arrays allowed y forced (de tamaño dxy)
void processWind(const Wind &wind, int dx, int dy, vector<bool> &allowed, vector<bool> &forced) {
    int dxy = dx * dy;
    allowed.assign(dxy, false);
    forced.assign(dxy, false);
    
    // Para "particionar" la grilla en cadenas: recorremos todas las celdas; una celda es inicio de cadena
    // si su predecesor (x - wx, y - wy) está fuera de la grilla.
    for (int y = 0; y < dy; y++){
        for (int x = 0; x < dx; x++){
            int px = x - wind.wx, py = y - wind.wy;
            if(px >= 0 && px < dx && py >= 0 && py < dy) continue; // no es inicio de cadena.
            
            // Simular la cadena iniciando en (x,y)
            Chain chain;
            int pos = 0;
            int cx = x, cy = y;
            while(cx >= 0 && cx < dx && cy >= 0 && cy < dy) {
                int id = idx(cx, cy, dx);
                chain.cells.push_back(id);
                if(wind.obs[id])
                    chain.obsPositions.push_back(pos);
                pos++;
                cx += wind.wx;
                cy += wind.wy;
            }
            // Si la cadena no tuvo ninguna observación, todas sus celdas deben quedar vacías.
            if(chain.obsPositions.empty()){
                for (int id : chain.cells)
                    allowed[id] = false;
                continue;
            }
            // Si hay observaciones, sea r0 la primera.
            int r0 = chain.obsPositions[0];
            // Para cada celda en la cadena, con índice pos:
            for (int i = 0; i < (int)chain.cells.size(); i++){
                int cellId = chain.cells[i];
                // Si la celda está antes de la primera observación, no está permitida.
                if(i < r0) {
                    allowed[cellId] = false;
                    forced[cellId] = false;
                    continue;
                }
                // Inicialmente se permite.
                bool cellAllowed = true;
                // Para cada observación (a partir de la segunda) se requiere que la celda que está justo antes (r-1) se quede vacía.
                // Es decir, si i == r - 1 para algún r (con r > r0), la celda debe quedar vacía.
                for (size_t j = 1; j < chain.obsPositions.size(); j++){
                    int r = chain.obsPositions[j];
                    if(i == r - 1) { cellAllowed = false; break; }
                }
                allowed[cellId] = cellAllowed;
                // Se marca forzada si i es exactamente alguna de las observaciones.
                forced[cellId] = false;
                for (int r : chain.obsPositions) {
                    if(i == r) { forced[cellId] = true; break; }
                }
            }
        }
    }
}
 
// MAIN
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int dx, dy, k;
    cin >> dx >> dy >> k;
    int dxy = dx * dy;
    
    vector<Wind> winds(k);
    for (int d = 0; d < k; d++){
        int wx, wy, b;
        cin >> wx >> wy >> b;
        winds[d].wx = wx;
        winds[d].wy = wy;
        winds[d].obs.assign(dxy, false);
        for (int j = 0; j < b; j++){
            int ox, oy;
            cin >> ox >> oy;
            // (1,1) es la esquina superior izquierda.
            int id = idx(ox - 1, oy - 1, dx);
            winds[d].obs[id] = true;
        }
    }
    
    // Para cada viento d, calculamos arrays allowed_d y forced_d (de tamaño dxy).
    // Luego, para cada celda p, se combinarán las condiciones:
    // overallAllowed[p] = ∧_{d=0}^{k-1} allowed_d[p]
    // overallForced[p] = ∨_{d=0}^{k-1} forced_d[p]
    vector<vector<bool>> allowedByWind(k, vector<bool>(dxy, false));
    vector<vector<bool>> forcedByWind(k, vector<bool>(dxy, false));
    
    for (int d = 0; d < k; d++){
        processWind(winds[d], dx, dy, allowedByWind[d], forcedByWind[d]);
    }
    
    // Combinar condiciones sobre todos los vientos.
    vector<char> X_max(dxy, '.'); // estructura maximal
    vector<char> X_min(dxy, '.'); // estructura minimal
    for (int i = 0; i < dxy; i++){
        bool overallAllowed = true;
        bool overallForced = false;
        for (int d = 0; d < k; d++){
            overallAllowed = overallAllowed && allowedByWind[d][i];
            overallForced = overallForced || forcedByWind[d][i];
        }
        if(overallAllowed) X_max[i] = '#';
        if(overallAllowed && overallForced) X_min[i] = '#';
    }
    
    // Preparar la salida: convertimos el vector lineal a grilla con dy filas y dx columnas.
    // Recordando que (1,1) es la esquina superior izquierda, la fila 0 es la primera.
    vector<string> maxGrid(dy, string(dx, '.'));
    vector<string> minGrid(dy, string(dx, '.'));
    for (int y = 0; y < dy; y++){
        for (int x = 0; x < dx; x++){
            int id = idx(x, y, dx);
            maxGrid[y][x] = X_max[id];
            minGrid[y][x] = X_min[id];
        }
    }
    
    // Imprimir: primero la estructura mínima, luego una línea en blanco y finalmente la estructura máxima.
    for (int y = 0; y < dy; y++){
        cout << minGrid[y] << "\n";
    }
    cout << "\n";
    for (int y = 0; y < dy; y++){
        cout << maxGrid[y] << "\n";
    }
    
    return 0;
}
