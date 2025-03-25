#include <iostream>
#include <vector>
#include <set>
#include <utility>

using namespace std;

int main() {
    int dx, dy, k;
    cin >> dx >> dy >> k;
    
    // Inicializamos las rejillas min (mínimo de moléculas) y max (máximo de moléculas)
    vector<vector<bool>> min_grid(dy + 1, vector<bool>(dx + 1, false));
    vector<vector<bool>> max_grid(dy + 1, vector<bool>(dx + 1, true));
    
    for (int i = 0; i < k; i++) {
        int wx, wy, b;
        cin >> wx >> wy >> b;
        
        // Recopilamos los límites (boundaries) para esta dirección del viento
        set<pair<int, int>> boundaries;
        for (int j = 0; j < b; j++) {
            int x, y;
            cin >> x >> y;
            boundaries.insert({x, y});
            
            // Los límites siempre deben tener moléculas
            min_grid[y][x] = true;
            max_grid[y][x] = true;
            
            // La celda previa a un límite no puede tener una molécula
            int prev_x = x - wx;
            int prev_y = y - wy;
            if (prev_x >= 1 && prev_x <= dx && prev_y >= 1 && prev_y <= dy) {
                max_grid[prev_y][prev_x] = false;
            }
        }
        
        // Procesar las restricciones para celdas que no son límites
        for (int y = 1; y <= dy; y++) {
            for (int x = 1; x <= dx; x++) {
                if (boundaries.count({x, y}) == 0) {
                    int prev_x = x - wx;
                    int prev_y = y - wy;
                    
                    if (prev_x >= 1 && prev_x <= dx && prev_y >= 1 && prev_y <= dy) {
                        // Si la celda previa tiene una molécula y esta no es un límite,
                        // esta celda también debe tener una molécula
                        if (min_grid[prev_y][prev_x]) {
                            min_grid[y][x] = true;
                            max_grid[y][x] = true;
                        }
                    }
                }
            }
        }
        
        // Restricción adicional: si una celda no es un límite y la siguiente tiene molécula,
        // esta celda también debe tener molécula
        for (int y = dy; y >= 1; y--) {
            for (int x = dx; x >= 1; x--) {
                int next_x = x + wx;
                int next_y = y + wy;
                
                if (next_x >= 1 && next_x <= dx && next_y >= 1 && next_y <= dy) {
                    if (min_grid[next_y][next_x] && boundaries.count({next_x, next_y}) == 0) {
                        min_grid[y][x] = true;
                        max_grid[y][x] = true;
                    }
                }
            }
        }
    }
    
    // Imprimir la configuración mínima
    for (int y = 1; y <= dy; y++) {
        for (int x = 1; x <= dx; x++) {
            cout << (min_grid[y][x] ? '#' : '.');
        }
        cout << endl;
    }
    
    cout << endl;
    
    // Imprimir la configuración máxima
    for (int y = 1; y <= dy; y++) {
        for (int x = 1; x <= dx; x++) {
            cout << (max_grid[y][x] ? '#' : '.');
        }
        cout << endl;
    }
    
    return 0;
}