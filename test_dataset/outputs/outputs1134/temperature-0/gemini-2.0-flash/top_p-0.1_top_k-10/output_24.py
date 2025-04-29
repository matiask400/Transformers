def hit_bricks(grid, hits):
    m = len(grid)
    n = len(grid[0])
    
    def is_valid(row, col):
        return 0 <= row < m and 0 <= col < n
    
    def dfs(row, col, visited):
        if not is_valid(row, col) or grid[row][col] != 1 or (row, col) in visited:
            return 0
        
        visited.add((row, col))
        
        count = 1
        count += dfs(row + 1, col, visited)
        count += dfs(row - 1, col, visited)
        count += dfs(row, col + 1, visited)
        count += dfs(row, col - 1, visited)
        
        return count
    
    # Mark hits as -1 temporarily
    for row, col in hits:
        if grid[row][col] == 1:
            grid[row][col] = -1
    
    # Make stable bricks as 1
    for col in range(n):
        if grid[0][col] == 1:
            dfs(0, col, set())
    
    result = []
    for row, col in reversed(hits):
        if grid[row][col] == -1:
            grid[row][col] = 1
            
            # Check if the brick is connected to the top
            is_connected = row == 0
            
            # Check if the brick is adjacent to a stable brick
            if not is_connected:
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + dr, col + dc
                    if is_valid(new_row, new_col) and grid[new_row][new_col] == 1:
                        is_connected = True
                        break
            
            if is_connected:
                before = dfs(0, 0, set()) if grid[0][0] == 1 else 0
                visited = set()
                dfs(row, col, visited)
                after = dfs(0, 0, set()) if grid[0][0] == 1 else 0
                
                fallen = after - before - 1
                result.append(max(0, fallen))
            else:
                result.append(0)
        else:
            result.append(0)
    
    return result[::-1]

def test_hit_bricks():
    test_cases = [
        {
            "grid": [[1,0,0,0],[1,1,1,0]],
            "hits": [[1,0]],
            "expected": [2]
        },
        {
            "grid": [[1,0,0,0],[1,1,0,0]],
            "hits": [[1,1],[1,0]],
            "expected": [0,0]
        },
        {
            "grid": [[1,1,1],[0,1,0],[0,0,0]],
            "hits": [[0,2],[2,0],[0,0]],
            "expected": [0,1,0]
        },
        {
            "grid": [[1,1,1],[1,0,1],[1,1,1]],
            "hits": [[1,1],[0,1]],
            "expected": [1,0]
        }
    ]
    
    num_correct = 0
    total_tests = len(test_cases)
    
    for i, test_case in enumerate(test_cases):
        grid = [row[:] for row in test_case["grid"]]  # Create a deep copy
        hits = test_case["hits"]
        expected = test_case["expected"]
        
        result = hit_bricks(grid, hits)
        
        if result == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: grid={test_case['grid']}, hits={hits}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
    
    print(f"\n{num_correct}/{total_tests} correct")

if __name__ == "__main__":
    test_hit_bricks()