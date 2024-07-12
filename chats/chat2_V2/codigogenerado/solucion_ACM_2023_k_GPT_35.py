import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read().splitlines()
    d, w = map(int, input[0].split())
    
    dice_faces = []
    for i in range(1, d + 1):
        dice_faces.append(input[i].split())
    
    valid_words = []
    for i in range(d + 1, d + 1 + w):
        valid_words.append(input[i])
    
    # DP to calculate expected number of rolls needed
    max_rolls = 1000  # Just a large number as a limit
    E = [float('inf')] * (max_rolls + 1)
    E[0] = 0.0
    
    for k in range(max_rolls):
        new_E = [float('inf')] * (max_rolls + 1)
        for j in range(w):
            word = valid_words[j]
            freq_needed = defaultdict(int)
            for ch in word:
                freq_needed[ch] += 1
            
            for roll in range(1, 7):
                roll_prob = 1 / 6.0
                current_dice = dice_faces[roll - 1]
                current_freq = defaultdict(int)
                for face in current_dice:
                    current_freq[face] += 1
                
                possible = True
                additional_rolls = 0.0
                for ch, needed_count in freq_needed.items():
                    current_count = current_freq[ch]
                    if current_count < needed_count:
                        possible = False
                        break
                    additional_rolls += (current_count - needed_count)
                
                if possible:
                    new_E[k + 1] = min(new_E[k + 1], E[k] + roll_prob * additional_rolls)
        
        E = new_E
        
        if E[k + 1] < float('inf'):
            print(f"{E[k + 1]:.7f}")
            return
    
    print("impossible")

