def ask_sphinx():
    # Ask the five questions
    questions = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, 1, 0),
        (1, 0, 1)
    ]
    
    responses = []
    for a, b, c in questions:
        print(f"{a} {b} {c}")
        response = int(input())
        responses.append((a, b, c, response))
    
    return responses

def solve_leg_counts(responses):
    from itertools import combinations
    
    # We will try to find the correct combination of 4 out of 5 responses
    for subset in combinations(responses, 4):
        A = []
        B = []
        for a, b, c, r in subset:
            A.append([a, b, c])
            B.append(r)
        
        try:
            legs = np.linalg.solve(A, B)
            if all(leg >= 0 for leg in legs):
                return legs
        except np.linalg.LinAlgError:
            continue
    
    return None

# Interact with the sphinx and solve the riddle
responses = ask_sphinx()
legs = solve_leg_counts(responses)

if legs:
    print(f"{int(legs[0])} {int(legs[1])} {int(legs[2])}")
else:
    print("No solution found.")
