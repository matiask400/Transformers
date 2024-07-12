def find_optimal_cut(n, dna_sequence):
    from collections import defaultdict, deque

    # Helper function to check proper nesting for a sequence
    def check_proper_nesting(sequence):
        stack = defaultdict(deque)
        nested_types = set()
        for marker in sequence:
            c, i = marker[0], marker[1:]
            if c == 's':
                stack[i].append('s')
            elif c == 'e':
                if stack[i] and stack[i][-1] == 's':
                    stack[i].pop()
                    if not stack[i]:
                        nested_types.add(i)
                else:
                    return 0  # Found improper nesting
        return len(nested_types)

    # Iterate through all possible cuts
    max_nested_types = 0
    best_cut_position = 1

    for cut_position in range(1, n + 1):
        # Create the linear sequence starting at the cut position
        linear_sequence = dna_sequence[cut_position - 1:] + dna_sequence[:cut_position - 1]
        
        # Check how many gene types form proper nesting
        nested_count = check_proper_nesting(linear_sequence)
        
        if nested_count > max_nested_types:
            max_nested_types = nested_count
            best_cut_position = cut_position
        elif nested_count == max_nested_types and cut_position < best_cut_position:
            best_cut_position = cut_position

    return best_cut_position, max_nested_types

# Read input
n = int(input().strip())
dna_sequence = input().strip().split()

# Find optimal cut
p, m = find_optimal_cut(n, dna_sequence)

# Output result
print(p, m)
