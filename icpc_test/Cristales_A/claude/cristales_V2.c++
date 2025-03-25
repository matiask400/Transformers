#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    int dx, dy, k;
    cin >> dx >> dy >> k;
    
    // These grids represent the minimum and maximum possible configurations
    // min_grid[y][x] = true means there must be a molecule at (x, y)
    // max_grid[y][x] = true means there can be a molecule at (x, y)
    vector<vector<bool>> min_grid(dy + 1, vector<bool>(dx + 1, false));
    vector<vector<bool>> max_grid(dy + 1, vector<bool>(dx + 1, true));
    
    for (int i = 0; i < k; i++) {
        int wx, wy, b;
        cin >> wx >> wy >> b;
        
        // Process boundaries for this wind direction
        set<pair<int, int>> boundaries;
        for (int j = 0; j < b; j++) {
            int x, y;
            cin >> x >> y;
            boundaries.insert({x, y});
        }
        
        // For each cell in the grid
        for (int y = 1; y <= dy; y++) {
            for (int x = 1; x <= dx; x++) {
                int prev_x = x - wx;
                int prev_y = y - wy;
                
                // Check if this is a boundary
                bool is_boundary = boundaries.count({x, y}) > 0;
                
                // If this is a boundary:
                // 1. There must be a molecule here (min_grid)
                // 2. There cannot be a molecule at the previous cell (max_grid)
                if (is_boundary) {
                    min_grid[y][x] = true;
                    if (prev_x >= 1 && prev_x <= dx && prev_y >= 1 && prev_y <= dy) {
                        max_grid[prev_y][prev_x] = false;
                    }
                } 
                // If this is not a boundary:
                // 1. If there's a molecule at the previous cell, there must be one here too (min_grid)
                // 2. If there cannot be a molecule at the previous cell, there cannot be one here (max_grid)
                else {
                    if (prev_x >= 1 && prev_x <= dx && prev_y >= 1 && prev_y <= dy) {
                        if (min_grid[prev_y][prev_x]) {
                            min_grid[y][x] = true;
                        }
                        if (!max_grid[prev_y][prev_x]) {
                            max_grid[y][x] = false;
                        }
                    }
                }
            }
        }
    }
    
    // Print the minimum configuration
    for (int y = 1; y <= dy; y++) {
        for (int x = 1; x <= dx; x++) {
            cout << (min_grid[y][x] ? '#' : '.');
        }
        cout << endl;
    }
    
    cout << endl;
    
    // Print the maximum configuration
    for (int y = 1; y <= dy; y++) {
        for (int x = 1; x <= dx; x++) {
            cout << (max_grid[y][x] ? '#' : '.');
        }
        cout << endl;
    }
    
    return 0;
}