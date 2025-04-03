import sys
import io

def is_boomerang(points):
    """
    Checks if three points form a boomerang.
    A boomerang is a set of three points that are all distinct and not in a straight line.

    Args:
        points: A list of three points, where each point is a list [x, y].

    Returns:
        True if the points form a boomerang, False otherwise.
    """
    # Ensure there are exactly 3 points (guaranteed by constraints, but good practice)
    if len(points) != 3:
        # This case shouldn't happen based on constraints, but handles general cases
        return False 
        
    # Extract coordinates for clarity
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    # Check for collinearity using the cross-product method derived from slopes.
    # Three points (x1, y1), (x2, y2), (x3, y3) are collinear if the slope
    # between (x1, y1) and (x2, y2) is the same as the slope between 
    # (x2, y2) and (x3, y3).
    # (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2)
    # To avoid division by zero, we cross-multiply:
    # (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
    #
    # This equality holds true if the points are collinear OR if any two points are identical.
    # For example, if points[0] == points[1]:
    # (y1 - y1) * (x3 - x1) == (y3 - y1) * (x1 - x1)
    # 0 * (x3 - x1) == (y3 - y1) * 0
    # 0 == 0 (True)
    #
    # A boomerang requires the points to be distinct AND non-collinear.
    # Therefore, the condition for a boomerang is that the above equality must be FALSE.
    
    # Calculate the two parts of the cross-product equality
    part1 = (y2 - y1) * (x3 - x2)
    part2 = (y3 - y2) * (x2 - x1)

    # Return True if they are not equal (i.e., not collinear and distinct)
    return part1 != part2

# Test framework
def run_tests():
    """
    Runs predefined test cases against the is_boomerang function and prints the results.
    """
    test_cases = [
        # Input: points, Expected Output
        ([[1,1],[2,3],[3,2]], True),  # Example 1
        ([[1,1],[2,2],[3,3]], False), # Example 2: Collinear
        ([[0,0],[1,0],[2,0]], False), # Collinear horizontal
        ([[0,0],[0,1],[0,2]], False), # Collinear vertical
        ([[0,0],[1,1],[0,0]], False), # P1 == P3 (not distinct)
        ([[1,1],[1,1],[2,2]], False), # P1 == P2 (not distinct)
        ([[1,1],[2,2],[2,2]], False), # P2 == P3 (not distinct)
        ([[0,0],[1,2],[2,1]], True),  # Non-collinear
        ([[0,0],[0,0],[0,0]], False), # All identical
        ([[10,20],[30,40],[50,60]], False), # Collinear diagonal
        ([[0,0],[1,0],[0,1]], True),  # Right angle triangle
        ([[5,8],[5,9],[6,8]], True),  # Another triangle
        ([[0,0],[1,1],[100,100]], False), # Collinear
        ([[0,100],[0,0],[0,50]], False), # Collinear vertical
        ([[100,0],[0,0],[50,0]], False), # Collinear horizontal
        ([[1,1],[1,2],[1,3]], False), # Collinear vertical
        ([[1,1],[2,1],[3,1]], False), # Collinear horizontal
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    for i, (points_input, expected_output) in enumerate(test_cases):
        # Run the function with the test input
        actual_output = is_boomerang(points_input)
        # Compare the actual output with the expected output
        result = actual_output == expected_output
        # Print the result for this test case
        print(result) 
        # Increment the count of correct tests if the result is True
        if result:
            correct_count += 1

    # Restore stdout
    sys.stdout = old_stdout

    # Print the captured output
    print(redirected_output.getvalue(), end='')

    # Print the final summary
    print(f"{correct_count}/{total_tests}")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()