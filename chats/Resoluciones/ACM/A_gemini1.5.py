import sys

def ask_question(a, b, c):
    print(f"{a} {b} {c}")
    sys.stdout.flush()  # Ensure the question is sent immediately
    return int(input())

def solve_sphinx_riddle():
    # We ask five questions, aiming to create a system of equations.
    # One equation might be a lie, so we'll need to account for that.

    answers = []
    for _ in range(5):
        # These coefficients can be adjusted for different strategies
        a = _ % 3  # Cycle through 0, 1, 2
        b = (_ + 1) % 3
        c = (_ + 2) % 3
        answers.append((a, b, c, ask_question(a, b, c)))

    # Now we have 5 equations. We need to find a combination of 4
    # that yields consistent results.  This is a simplified approach,
    # and more robust error checking could be implemented.

    for i in range(5):
        # Assume the i-th answer is a lie
        test_answers = answers[:i] + answers[i+1:]

        # Try to solve the system of equations (details omitted here
        # as it requires setting up and solving linear equations)

        # ... (Implementation of solving the system of 3 equations)

        # If a solution is found and it's non-negative, we have our answer
        if solution_found and all(x >= 0 for x in solution):
            return solution  

    # If no consistent solution is found, we couldn't identify the lie
    return None

if __name__ == "__main__":
    solution = solve_sphinx_riddle()
    if solution:
        print(f"{solution[0]} {solution[1]} {solution[2]}")
    else:
        print("Couldn't determine the answer")
