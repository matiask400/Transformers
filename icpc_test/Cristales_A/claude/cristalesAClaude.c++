#include <iostream>
#include <vector>
#include <set>
using namespace std;

struct Point {
    int x, y;
    Point(int x = 0, int y = 0) : x(x), y(y) {}
    bool operator<(const Point& other) const {
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
};

int main() {
    int dx, dy, k;
    cin >> dx >> dy >> k;

    // Definite molecules (must exist)
    set<Point> definite;
    // Potential molecules (may or may not exist)
    set<Point> potential;

    for (int i = 0; i < k; i++) {
        int wx, wy, b;
        cin >> wx >> wy >> b;

        for (int j = 0; j < b; j++) {
            int x, y;
            cin >> x >> y;
            Point boundary(x, y);
            definite.insert(boundary);

            // Add the point that must not have a molecule (upwind)
            Point upwind(x - wx, y - wy);
            if (upwind.x >= 1 && upwind.x <= dx && upwind.y >= 1 && upwind.y <= dy) {
                potential.erase(upwind);
            }

            // For each boundary, we need to check if there are molecules downwind
            // that would create additional boundaries not observed
            for (int x_pos = 1; x_pos <= dx; x_pos++) {
                for (int y_pos = 1; y_pos <= dy; y_pos++) {
                    Point p(x_pos, y_pos);
                    if (definite.count(p)) continue;

                    Point downwind(x_pos + wx, y_pos + wy);
                    if (downwind.x >= 1 && downwind.x <= dx && 
                        downwind.y >= 1 && downwind.y <= dy && 
                        !definite.count(downwind)) {
                        potential.insert(p);
                    }
                }
            }
        }
    }

    // Remove points from potential that would create contradictions
    for (int i = 0; i < k; i++) {
        int wx, wy, b;
        cin >> wx >> wy >> b;
        vector<Point> boundaries;
        
        for (int j = 0; j < b; j++) {
            int x, y;
            cin >> x >> y;
            boundaries.push_back(Point(x, y));
        }

        set<Point> to_remove;
        for (const Point& p : potential) {
            Point downwind(p.x + wx, p.y + wy);
            if (downwind.x >= 1 && downwind.x <= dx && 
                downwind.y >= 1 && downwind.y <= dy &&
                !definite.count(downwind) && !potential.count(downwind)) {
                to_remove.insert(p);
            }
        }
        
        for (const Point& p : to_remove) {
            potential.erase(p);
        }
    }

    // Print minimal structure
    for (int y = 1; y <= dy; y++) {
        for (int x = 1; x <= dx; x++) {
            Point p(x, y);
            cout << (definite.count(p) ? '#' : '.');
        }
        cout << endl;
    }

    cout << endl;

    // Print maximal structure
    for (int y = 1; y <= dy; y++) {
        for (int x = 1; x <= dx; x++) {
            Point p(x, y);
            cout << (definite.count(p) || potential.count(p) ? '#' : '.');
        }
        cout << endl;
    }

    return 0;
}