import sys
import io

def is_boomerang(points: list[list[int]]) -> bool:
    """
    Checks if three points form a boomerang.

    A boomerang is a set of three points that are all distinct and not 
    in a straight line.

    Args:
        points: A list containing three points, where each point is a list [x, y].

    Returns:
        True if the points form a boomerang, False otherwise.
    """
    # Ensure there are exactly 3 points (guaranteed by constraints, but good practice)
    if len(points) != 3:
        # This case shouldn't happen based on constraints, but handles potential misuse
        return False 
        
    p1 = points[0]
    p2 = points[1]
    p3 = points[2]

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]

    # Check for distinct points implicitly using the collinearity check.
    # If any two points are the same, the expression below will evaluate to 0 == 0,
    # resulting in False (not a boomerang).

    # Check for collinearity using the slope comparison method, avoiding division:
    # Three points (x1, y1), (x2, y2), (x3, y3) are collinear if the slope between
    # p1 and p2 is equal to the slope between p2 and p3.
    # (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2)  (if denominators are non-zero)
    # Cross-multiply to avoid division by zero and potential floating point issues:
    # (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
    #
    # The points are *not* collinear (and thus form a boomerang, assuming they are distinct)
    # if the two sides of the equation are *not* equal.
    # This condition also handles the case where points are identical. If p1=p2 or p2=p3,
    # one side of the multiplication will involve (x2-x1) or (y2-y1) = 0 and the other
    # side will involve (x3-x2) or (y3-y2) = 0 for the respective identical pair,
    # making the equality (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1) true,
    # meaning the function correctly returns False.

    return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)

def run_tests():
    """
    Runs predefined test cases against the is_boomerang function and prints the results.
    """
    test_cases = [
        # Example 1: Not collinear, distinct
        ([[1,1],[2,3],[3,2]], True),
        # Example 2: Collinear, distinct
        ([[1,1],[2,2],[3,3]], False),
        # Custom Test Cases
        # Collinear horizontal
        ([[0,0],[1,0],[2,0]], False),
        # Collinear vertical
        ([[0,0],[0,1],[0,2]], False),
        # Two points identical (p1 == p2)
        ([[1,1],[1,1],[2,3]], False),
         # Two points identical (p2 == p3)
        ([[0,5],[1,1],[1,1]], False),
        # Two points identical (p1 == p3)
        ([[2,3],[1,1],[2,3]], False),
        # All points identical
        ([[0,0],[0,0],[0,0]], False),
        # Right angle triangle
        ([[0,0],[1,1],[0,1]], True),
        # Large coordinates, collinear
        ([[0,0],[50,50],[100,100]], False),
         # Large coordinates, not collinear
        ([[0,0],[100,0],[0,100]], True),
        # General non-collinear case
        ([[0,0],[1,2],[2,1]], True),
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    # Capture standard output
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, (points, expected) in enumerate(test_cases):
        result = is_boomerang(points)
        passed = result == expected
        print(f"{passed}")
        if passed:
            correct_tests += 1

    # Restore standard output
    sys.stdout = old_stdout
    output_str = captured_output.getvalue()

    # Print the captured output line by line
    for line in output_str.strip().split('\n'):
        print(line)
        
    # Print the final summary
    print(f"{correct_tests}/{total_tests}")

# Execute the tests when the script is run
if __name__ == '__main__':
    run_tests()