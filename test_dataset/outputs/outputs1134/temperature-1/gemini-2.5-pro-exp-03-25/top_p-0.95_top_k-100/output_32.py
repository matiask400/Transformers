import sys
from collections import defaultdict

def solve():
    """
    Solves the Subarray Sums Divisible by K problem.
    Given an array A of integers, return the number of (contiguous, non-empty) 
    subarrays that have a sum divisible by K.
    """
    A = [int(x) for x in sys.argv[1].split(',')]
    K = int(sys.argv[2])
    
    count = 0
    prefix_sum = 0
    # Dictionary to store the frequency of prefix sum remainders modulo K.
    # Initialize with remainder 0 having frequency 1 to account for subarrays 
    # starting from index 0 whose sum is divisible by K.
    remainder_counts = defaultdict(int)
    remainder_counts[0] = 1 

    for num in A:
        prefix_sum += num
        remainder = prefix_sum % K
        
        # If a remainder `r` has occurred `f` times before, it means there are 
        # `f` indices `i` such that prefix_sum[i] % K == r.
        # For the current prefix_sum[j], if prefix_sum[j] % K == r, then
        # (prefix_sum[j] - prefix_sum[i]) % K == 0.
        # This corresponds to `f` subarrays ending at the current index `j-1` 
        # whose sum is divisible by K.
        count += remainder_counts[remainder]
        
        # Increment the frequency count for the current remainder.
        remainder_counts[remainder] += 1
        
    print(count)


def run_tests():
    """
    Runs test cases against the solve function.
    """
    tests = [
        # Format: (A_list_str, K_str, expected_output_str)
        ("4,5,0,-2,-3,1", "5", "7"),
        ("5", "9", "0"),
        ("5,0,5,0", "5", "10"), # [5], [5,0], [5,0,5], [5,0,5,0], [0], [0,5], [0,5,0], [5], [5,0], [0]
        ("-1,2,9", "3", "2"), # [-1,2,9] sum 10 % 3 = 1; [-1] -1 % 3 = 2; [2] 2 % 3 = 2; [9] 9 % 3 = 0 (1); [-1,2] 1 % 3 = 1; [2,9] 11 % 3 = 2; Total: [9], [-1,2,9] - [-1] = [2,9]? No wait.
                           # Let's trace [-1, 2, 9], K=3
                           # P = [0, -1, 1, 10]
                           # R = [0%3, -1%3, 1%3, 10%3] = [0, 2, 1, 1]
                           # counts = {0: 1} -> prefix 0, rem 0
                           # num -1: prefix -1, rem 2. count=0. counts={0:1, 2:1}
                           # num  2: prefix  1, rem 1. count=0. counts={0:1, 2:1, 1:1}
                           # num  9: prefix 10, rem 1. count+=counts[1](1)=1. counts={0:1, 2:1, 1:2}
                           # Final count = 1. Subarrays: [9]. Hmm, let's re-read.
                           # The problem asks for subarrays with sum divisible by K.
                           # Subarrays of [-1, 2, 9]:
                           # [-1] sum -1. No.
                           # [2] sum 2. No.
                           # [9] sum 9. Yes.
                           # [-1, 2] sum 1. No.
                           # [2, 9] sum 11. No.
                           # [-1, 2, 9] sum 10. No.
                           # Output should be 1. Where did I get 2 from? Ah, maybe an online source. Let's stick to 1 based on manual check and algorithm run.
                           # Let's try one more: [2,-2,2,-4], K=6
                           # P = [0, 2, 0, 2, -2]
                           # R = [0%6, 2%6, 0%6, 2%6, -2%6] = [0, 2, 0, 2, 4]
                           # counts = {0: 1} -> P[0]=0, r=0
                           # num 2: P[1]=2, r=2. count=0. counts={0:1, 2:1}
                           # num -2: P[2]=0, r=0. count+=counts[0](1)=1. counts={0:2, 2:1}. Subarray A[0..1]=[2,-2] sum 0.
                           # num 2: P[3]=2, r=2. count+=counts[2](1)=1+1=2. counts={0:2, 2:2}. Subarray A[1..2]=[-2,2] sum 0. NO -> P[3]%6 == P[1]%6 -> A[1..2] sum P[3]-P[1]=2-2=0. Yes.
                           # num -4: P[4]=-2, r=4. count+=counts[4](0)=2+0=2. counts={0:2, 2:2, 4:1}
                           # Final count = 2. Subarrays: [2,-2], [-2,2]. Correct. My previous trace for [-1,2,9] giving 1 seems correct. Let's update the test.
        ("-1,2,9", "3", "1"), 
        ("2,-2,2,-4", "6", "2"),
        ("0,0,0", "1", "6"), # N=3, N*(N+1)/2 = 3*4/2 = 6. [0],[0],[0],[0,0],[0,0],[0,0,0]
        ("7,4,-3,1,9", "5", "4") # P=[0,7,11,8,9,18] R=[0,2,1,3,4,3] counts={0:1}->P0,r0. num 7: P1=7,r2. c=0. cts={0:1,2:1}. num 4: P2=11,r1. c=0. cts={0:1,2:1,1:1}. num -3: P3=8,r3. c=0. cts={0:1,2:1,1:1,3:1}. num 1: P4=9,r4. c=0. cts={0:1,2:1,1:1,3:1,4:1}. num 9: P5=18,r3. c+=cts[3](1)=1. cts={0:1,2:1,1:1,3:2,4:1}. Final count=1. Subarray A[3..4]=[1,9] sum=10. NO WAIT P[5]-P[3] = 18-8=10. Correct.
                                        # Let's recheck the example 1 trace carefully.
                                        # A = [4,5,0,-2,-3,1], K = 5
                                        # P = [0, 4, 9, 9, 7, 4, 5]
                                        # R = [0%5, 4%5, 9%5, 9%5, 7%5, 4%5, 5%5] = [0, 4, 4, 4, 2, 4, 0]
                                        # cts={0:1} c=0 -> P0=0,r=0
                                        # n=4: P1=4, r=4. c=0. cts={0:1, 4:1}
                                        # n=5: P2=9, r=4. c+=cts[4](1)=1. cts={0:1, 4:2}.  (P2-P1 = 9-4 = 5 div by 5 -> A[1]=[5])
                                        # n=0: P3=9, r=4. c+=cts[4](2)=1+2=3. cts={0:1, 4:3}.  (P3-P1=9-4=5 div by 5 -> A[1..2]=[5,0]), (P3-P2=9-9=0 div by 5 -> A[2]=[0])
                                        # n=-2: P4=7, r=2. c+=cts[2](0)=3+0=3. cts={0:1, 4:3, 2:1}
                                        # n=-3: P5=4, r=4. c+=cts[4](3)=3+3=6. cts={0:1, 4:4, 2:1}. (P5-P1=4-4=0 -> A[1..4]=[5,0,-2,-3]), (P5-P2=4-9=-5 -> A[2..4]=[0,-2,-3]), (P5-P3=4-9=-5 -> A[3..4]=[-2,-3])
                                        # n=1: P6=5, r=0. c+=cts[0](1)=6+1=7. cts={0:2, 4:4, 2:1}. (P6-P0=5-0=5 -> A[0..5]=[4,5,0,-2,-3,1])
                                        # Final count = 7. The logic holds. My trace for [7,4,-3,1,9] K=5 seems wrong somewhere. Let's redo it.
                                        # A = [7,4,-3,1,9], K=5
                                        # P = [0, 7, 11, 8, 9, 18]
                                        # R = [0, 2, 1, 3, 4, 3]
                                        # cts={0:1}, c=0. P0=0, r=0.
                                        # n=7:  P1=7, r=2. c=0. cts={0:1, 2:1}
                                        # n=4:  P2=11, r=1. c=0. cts={0:1, 2:1, 1:1}
                                        # n=-3: P3=8, r=3. c=0. cts={0:1, 2:1, 1:1, 3:1}
                                        # n=1:  P4=9, r=4. c=0. cts={0:1, 2:1, 1:1, 3:1, 4:1}
                                        # n=9:  P5=18, r=3. c+=cts[3](1)=1. cts={0:1, 2:1, 1:1, 3:2, 4:1}
                                        # Final count=1. Subarray A[3..4]=[1,9], sum=10. Okay this seems correct now. Let's find other subarrays div by 5.
                                        # [7,4,-3,1,9] sums:
                                        # [7] 7 no
                                        # [4] 4 no
                                        # [-3] -3 no
                                        # [1] 1 no
                                        # [9] 9 no
                                        # [7,4] 11 no
                                        # [4,-3] 1 no
                                        # [-3,1] -2 no
                                        # [1,9] 10 YES (1)
                                        # [7,4,-3] 8 no
                                        # [4,-3,1] 2 no
                                        # [-3,1,9] 7 no
                                        # [7,4,-3,1] 9 no
                                        # [4,-3,1,9] 11 no
                                        # [7,4,-3,1,9] 18 no
                                        # The expected answer is 1, not 4. Let me update the test case.
        ("7,4,-3,1,9", "5", "1"), 
    ]
    
    correct_count = 0
    total_tests = len(tests)
    
    # Store original sys.argv
    original_argv = sys.argv
    
    for i, (a_str, k_str, expected_str) in enumerate(tests):
        print(f"Test {i+1}:")
        # Simulate command line arguments
        sys.argv = [original_argv[0], a_str, k_str] 
        
        # Capture stdout
        import io
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output
        
        try:
            solve()
            output = redirected_output.getvalue().strip()
            # Restore stdout
            sys.stdout = old_stdout 
            
            if output == expected_str:
                print(f"Input A: {a_str}, K: {k_str}")
                print(f"