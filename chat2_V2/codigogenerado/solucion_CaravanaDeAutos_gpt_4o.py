def reorganize_caravan(N, D, distances):
    if N <= 1 or N > 1000 or D < 1 or D > 10000:
        return 0  # Inputs out of bounds

    moves_needed = 0

    for i in range(1, N-1):
        if distances[i-1] > D:
            if distances[i-1] - distances[i] <= D:
                moves_needed += 1
            else:
                return 0  # It's not possible to rearrange without moving the first or last car

    return moves_needed

def main():
    while True:
        first_line = input().strip()
        N, D = map(int, first_line.split())
        if N == 0 and D == 0:
            break
        second_line = input().strip()
        distances = list(map(int, second_line.split()))
        result = reorganize_caravan(N, D, distances)
        print(result)

# Start the program
main()