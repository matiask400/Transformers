#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Wind {
    int wx, wy;
    // Grilla de observados: obs[y][x] es true si la celda (x,y) (0-indexado) fue observada.
    vector<vector<bool>> obs;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int dx, dy, k;
    cin >> dx >> dy >> k;
    
    // Leemos los datos de cada viento.
    vector<Wind> winds(k);
    for (int i = 0; i < k; i++){
        int wx, wy, b;
        cin >> wx >> wy >> b;
        winds[i].wx = wx;
        winds[i].wy = wy;
        // Inicializamos la grilla de observados (dimensiones: dy filas, dx columnas)
        winds[i].obs.assign(dy, vector<bool>(dx, false));
        for (int j = 0; j < b; j++){
            int ox, oy;
            cin >> ox >> oy;
            // Convertir a 0-indexado. Dado que (1,1) es la esquina superior izquierda,
            // la fila es oy-1 y la columna es ox-1.
            winds[i].obs[oy - 1][ox - 1] = true;
        }
    }
    
    // Para cada viento guardaremos dos grillas:
    // posList[d][y][x] almacena la posición (en la cadena) de la celda (x,y) para el viento d.
    // chainList[d][y][x] almacena el índice de la primera celda observada en la cadena de (x,y) (o -1 si no hay ninguno).
    vector<vector<vector<int>>> posList(k, vector<vector<int>>(dy, vector<int>(dx, -1)));
    vector<vector<vector<int>>> chainList(k, vector<vector<int>>(dy, vector<int>(dx, -1)));
    
    // Procesamos cada viento por separado.
    for (int d = 0; d < k; d++){
        int wx = winds[d].wx, wy = winds[d].wy;
        // Para cada celda de la grilla, si es "inicio de cadena" para este viento (es decir, su predecesor (x-wx, y-wy) está fuera)
        // simulamos la cadena.
        for (int y = 0; y < dy; y++){
            for (int x = 0; x < dx; x++){
                int prev_x = x - wx;
                int prev_y = y - wy;
                if (prev_x >= 0 && prev_x < dx && prev_y >= 0 && prev_y < dy)
                    continue; // No es inicio de cadena.
                int pos = 0;
                int chainObs = -1; // Índice de la primera celda observada en la cadena (aún no encontrado).
                int cur_x = x, cur_y = y;
                while (cur_x >= 0 && cur_x < dx && cur_y >= 0 && cur_y < dy) {
                    posList[d][cur_y][cur_x] = pos;
                    if (chainObs == -1 && winds[d].obs[cur_y][cur_x])
                        chainObs = pos;
                    chainList[d][cur_y][cur_x] = chainObs;
                    pos++;
                    cur_x += wx;
                    cur_y += wy;
                }
            }
        }
    }
    
    // Construimos las dos soluciones: mínima y máxima.
    // Una celda (x,y) es permitida globalmente si para cada viento:
    //    • La cadena tiene algún observado (chainList != -1)
    //    • La celda está en o después del primer observado (lo que siempre se verifica, salvo que esté antes)
    // Además, se dice que la celda es "forzada" si para al menos un viento su posición es igual a chainList.
    vector<string> minGrid(dy, string(dx, '.'));
    vector<string> maxGrid(dy, string(dx, '.'));
    for (int y = 0; y < dy; y++){
        for (int x = 0; x < dx; x++){
            bool allowed = true;
            bool forced = false;
            for (int d = 0; d < k; d++){
                int chainVal = chainList[d][y][x];
                if (chainVal == -1) { // No hay observado en la cadena ⇒ celda debe quedar vacía.
                    allowed = false;
                    break;
                }
                int posVal = posList[d][y][x];
                if (posVal < chainVal) { // La celda está antes del primer observado ⇒ no se puede llenar.
                    allowed = false;
                    break;
                }
                if (posVal == chainVal) {
                    forced = true;
                }
            }
            if (allowed) {
                maxGrid[y][x] = '#';
                if (forced)
                    minGrid[y][x] = '#';
            }
        }
    }
    
    // Imprimimos la salida:
    // Se debe producir primero la estructura con el número mínimo de moléculas,
    // luego una línea en blanco y, finalmente, la estructura con el número máximo.
    // La celda (1,1) corresponde a la esquina superior izquierda, por lo que recorremos las filas en orden natural.
    for (int y = 0; y < dy; y++){
        cout << minGrid[y] << "\n";
    }
    cout << "\n";
    for (int y = 0; y < dy; y++){
        cout << maxGrid[y] << "\n";
    }
    
    return 0;
}
