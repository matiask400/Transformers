#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Wind {
    int wx, wy;
    // Usamos un vector<bool> de tamaño dx*dy; el índice se calcula como idx = y*dx + x.
    vector<bool> obs;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int dx, dy, k;
    cin >> dx >> dy >> k;
    int dxy = dx * dy;
    
    // Leemos cada viento y marcamos las celdas observadas (convertidas a 0-indexado).
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
            // (1,1) es la esquina superior izquierda.
            int idx = (oy - 1) * dx + (ox - 1);
            winds[i].obs[idx] = true;
        }
    }
    
    // Para cada viento se calcularán dos arreglos de tamaño dxy:
    // - posList[d][idx] guarda la posición de la celda (x,y) en su cadena para el viento d.
    // - chainList[d][idx] guarda el índice (posición) de la primera celda observada en la cadena,
    //   o -1 si en esa cadena no hay celda observada.
    vector<vector<int>> posList(k, vector<int>(dxy, -1));
    vector<vector<int>> chainList(k, vector<int>(dxy, -1));
    
    // Función lambda para convertir (x,y) a índice lineal.
    auto indexOf = [dx](int x, int y) -> int {
        return y * dx + x;
    };
    
    // Para cada viento, simulamos las “cadenas”.
    // Una celda es inicio de cadena si su "predecesor" (x - wx, y - wy) está fuera de rango.
    for (int d = 0; d < k; d++){
        int wx = winds[d].wx, wy = winds[d].wy;
        for (int y = 0; y < dy; y++){
            for (int x = 0; x < dx; x++){
                int prev_x = x - wx, prev_y = y - wy;
                if (prev_x >= 0 && prev_x < dx && prev_y >= 0 && prev_y < dy)
                    continue; // No es inicio de cadena.
                int pos = 0;
                int chainObs = -1; // Aún no se encontró ninguna celda observada en la cadena.
                int cur_x = x, cur_y = y;
                while (cur_x >= 0 && cur_x < dx && cur_y >= 0 && cur_y < dy) {
                    int idx = indexOf(cur_x, cur_y);
                    posList[d][idx] = pos;
                    // La primera vez que se encuentre una celda observada se fija chainObs.
                    if (chainObs == -1 && winds[d].obs[idx])
                        chainObs = pos;
                    chainList[d][idx] = chainObs;
                    pos++;
                    cur_x += wx;
                    cur_y += wy;
                }
            }
        }
    }
    
    // Construimos las dos estructuras:
    // - En la estructura máxima se colocan moléculas en todas las celdas "permitidas":
    //   una celda es permitida si, para cada viento, su cadena tiene al menos un observado (chainList != -1)
    //   y la posición de la celda es mayor o igual a la posición del primer observado.
    // - En la estructura mínima se colocan moléculas solo en las celdas forzadas:
    //   es decir, aquellas que son permitidas y en al menos un viento su posición es exactamente igual a chainList.
    vector<string> minGrid(dy, string(dx, '.'));
    vector<string> maxGrid(dy, string(dx, '.'));
    
    for (int y = 0; y < dy; y++){
        for (int x = 0; x < dx; x++){
            int idx = indexOf(x, y);
            bool allowed = true;
            bool forced = false;
            for (int d = 0; d < k; d++){
                int chainVal = chainList[d][idx];
                // Si en algún viento la cadena no tiene celda observada, la celda no puede tener molécula.
                if (chainVal == -1) { allowed = false; break; }
                int posVal = posList[d][idx];
                // Si la celda está antes del primer observado en la cadena, no se permite.
                if (posVal < chainVal) { allowed = false; break; }
                // Si para algún viento la celda es la primera observada, se fuerza su llenado en la mínima.
                if (posVal == chainVal)
                    forced = true;
            }
            if (allowed) {
                maxGrid[y][x] = '#';
                if (forced)
                    minGrid[y][x] = '#';
            }
        }
    }
    
    // Imprimir la salida.
    // Se debe producir primero la estructura mínima, luego una línea en blanco y finalmente la estructura máxima.
    // La celda (1,1) corresponde a la esquina superior izquierda, así que recorremos las filas de 0 a dy-1.
    for (int y = 0; y < dy; y++){
        cout << minGrid[y] << "\n";
    }
    cout << "\n";
    for (int y = 0; y < dy; y++){
        cout << maxGrid[y] << "\n";
    }
    
    return 0;
}
