// c:\Users\mkoro\Desktop\Transformers\crystal_patterns.cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Function to apply pattern type 1 (diagonal patterns)
void applyDiagonalPattern(vector<string>& grid, int startRow, int startCol, int direction) {
    int rows = grid.size();
    int cols = grid[0].size();
    
    // Set the starting position
    if (startRow >= 0 && startRow < rows && startCol >= 0 && startCol < cols) {
        grid[startRow][startCol] = '#';
    }
    
    // Create diagonal patterns
    for (int d = 1; d < max(rows, cols); d++) {
        int newRow = startRow + d * direction;
        
        // Right diagonal
        int rightCol = startCol + d;
        if (newRow >= 0 && newRow < rows && rightCol >= 0 && rightCol < cols) {
            grid[newRow][rightCol] = '#';
        }
        
        // Left diagonal
        int leftCol = startCol - d;
        if (newRow >= 0 && newRow < rows && leftCol >= 0 && leftCol < cols) {
            grid[newRow][leftCol] = '#';
        }
    }
}

// Function to create a pattern based on transformation parameters
vector<string> createPattern(const vector<int>& params, int rows, int cols) {
    vector<string> grid(rows, string(cols, '.'));
    
    int type = params[0];
    int direction = params[1];
    int count = params[2];
    
    if (type == 1) {
        // Type 1: V-shaped diagonal patterns
        for (int i = 0; i < count; i++) {
            int startRow = params[3 + i*2];
            int startCol = params[4 + i*2];
            applyDiagonalPattern(grid, startRow, startCol, direction);
        }
    } else if (type == 0) {
        // Type 0: Direct coordinate placement
        for (int i = 0; i < count; i++) {
            int r = params[3 + i*2];
            int c = params[4 + i*2];
            
            if (r >= 0 && r < rows && c >= 0 && c < cols) {
                grid[r][c] = '#';
            }
        }
    }
    
    return grid;
}

int main() {
    int rows, cols, patterns;
    cin >> rows >> cols >> patterns;
    
    vector<vector<int>> transformations;
    for (int i = 0; i < patterns; i++) {
        int type, direction, count;
        cin >> type >> direction >> count;
        
        vector<int> params = {type, direction, count};
        for (int j = 0; j < count * 2; j++) {
            int value;
            cin >> value;
            params.push_back(value);
        }
        
        transformations.push_back(params);
    }
    
    // Create and print patterns
    for (const auto& params : transformations) {
        vector<string> grid = createPattern(params, rows, cols);
        for (const string& row : grid) {
            cout << row << endl;
        }
        cout << endl;
    }
    
    return 0;
}