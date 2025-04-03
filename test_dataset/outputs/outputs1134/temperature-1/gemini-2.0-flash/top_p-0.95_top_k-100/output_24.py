def hit_bricks(grid, hits):
    m = len(grid)
    n = len(grid[0])
    
    def is_valid(r, c):
        return 0 <= r < m and 0 <= c < n
    
    def dfs(r, c, temp_grid):
        if not is_valid(r, c) or temp_grid[r][c] != 1:
            return 0
        
        temp_grid[r][c] = 2  # Mark as visited/stable
        
        count = 1
        count += dfs(r + 1, c, temp_grid)
        count += dfs(r - 1, c, temp_grid)
        count += dfs(r, c + 1, temp_grid)
        count += dfs(r, c - 1, temp_grid)
        
        return count
    
    # Step 1: Mark hits as -1 in the grid
    for r, c in hits:
        if grid[r][c] == 1:
            grid[r][c] = -1
    
    # Step 2: Make a copy of the grid and mark initial stable bricks as 2
    temp_grid = [row[:] for row in grid]
    for c in range(n):
        if temp_grid[0][c] == 1:
            dfs(0, c, temp_grid)
    
    # Step 3: Reverse iterate through hits and calculate fallen bricks
    result = []
    for i in range(len(hits) - 1, -1, -1):
        r, c = hits[i]
        
        if grid[r][c] == 0:
            result.append(0)
            continue
            
        grid[r][c] = 1
        
        # Check if it's connected to the top or adjacent to a stable brick
        is_stable = False
        if r == 0:
            is_stable = True
        else:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and temp_grid[nr][nc] == 2:
                    is_stable = True
                    break
                    
        if not is_stable:
            result.append(0)
            continue
            
        # Count the number of bricks that become stable after adding this brick
        initial_count = sum(sum(1 for val in row if val == 2) for row in temp_grid)
        
        temp_grid = [row[:] for row in grid]
        
        for c_top in range(n):
            if temp_grid[0][c_top] == 1:
                dfs(0, c_top, temp_grid)
                
        final_count = sum(sum(1 for val in row if val == 2) for row in temp_grid)
        
        result.append(final_count - initial_count -1 ) #Subtract 1 for the brick at hits[i]
    
    # Step 4: Reverse the result array
    result.reverse()
    return result


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
            "hits": [[0,2],[2,0],[0,1],[1,2]],
            "expected": [0,0,1,0]
        },
       {
            "grid": [[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1]],
            "hits": [[4,0],[0,1],[3,1],[2,3],[0,4],[3,0],[1,0],[4,2],[2,0],[0,3],[4,1],[1,2]],
            "expected": [0,0,0,0,0,0,0,0,1,0,1,0]
        }
    ]

    num_correct = 0
    for i, test_case in enumerate(test_cases):
        grid = [row[:] for row in test_case["grid"]]  # Deep copy
        hits = [hit[:] for hit in test_case["hits"]] #Deep copy

        actual_result = hit_bricks(grid, hits)
        expected_result = test_case["expected"]

        if actual_result == expected_result:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input Grid: {test_case['grid']}")
            print(f"  Input Hits: {test_case['hits']}")
            print(f"  Expected: {expected_result}")
            print(f"  Actual:   {actual_result}")

    print(f"\n{num_correct}/{len(test_cases)} correct")

if __name__ == "__main__":
    test_hit_bricks()