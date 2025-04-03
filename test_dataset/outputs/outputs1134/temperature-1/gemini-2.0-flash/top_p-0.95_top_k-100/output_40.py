from collections import deque

def openLock(deadends, target):
    deadends = set(deadends)
    if "0000" in deadends:
        return -1
    
    q = deque([("0000", 0)])
    visited = {"0000"}
    
    while q:
        lock, moves = q.popleft()
        
        if lock == target:
            return moves
        
        for i in range(4):
            digit = int(lock[i])
            
            # Move forward
            new_digit = (digit + 1) % 10
            new_lock = lock[:i] + str(new_digit) + lock[i+1:]
            if new_lock not in deadends and new_lock not in visited:
                q.append((new_lock, moves + 1))
                visited.add(new_lock)
            
            # Move backward
            new_digit = (digit - 1) % 10
            new_lock = lock[:i] + str(new_digit) + lock[i+1:]
            if new_lock not in deadends and new_lock not in visited:
                q.append((new_lock, moves + 1))
                visited.add(new_lock)
    
    return -1

def test_openLock():
    tests = [
        (["0201","0101","0102","1212","2002"], "0202", 6),
        (["8888"], "0009", 1),
        (["8887","8889","8878","8898","8788","8988","7888","9888"], "8888", -1),
        (["0000"], "8888", -1),
        (["1111"], "1110", 1),
        (["0001","0002","0003","0004","0005","0006","0007","0008"], "0009", 1),
        (["0000"], "0202", -1),
        (["9999"], "0000", 4),
        (["1000"], "0000", 1),
        ([], "1111", 4),
        ([], "0000", 0)
    ]
    
    correct_count = 0
    total_tests = len(tests)
    
    for i, (deadends, target, expected) in enumerate(tests):
        result = openLock(deadends, target)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: deadends={deadends}, target={target}")
            print(f"  Expected: {expected}, Got: {result}")
    
    print(f"\nCorrect: {correct_count}/{total_tests}")

if __name__ == "__main__":
    test_openLock()