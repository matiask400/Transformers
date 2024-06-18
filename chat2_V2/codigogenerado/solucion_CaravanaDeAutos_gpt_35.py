def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    i = 0
    results = []
    
    while i < len(data):
        first_line = data[i].strip()
        if first_line == "0 0":
            break
        
        N, D = map(int, first_line.split())
        
        if N == 0 and D == 0:
            break
        
        distances = list(map(int, data[i + 1].strip().split()))
        
        # Calculate required moves
        moves_required = 0
        
        for j in range(N - 1):
            current_distance = distances[j]
            if current_distance < D:
                moves_required += (D - current_distance)
        
        results.append(moves_required)
        
        # Move to next set of input
        i += 2
    
    for result in results:
        print(result)

