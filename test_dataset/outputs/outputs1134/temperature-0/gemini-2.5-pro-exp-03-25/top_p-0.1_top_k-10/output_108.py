import math
import sys

# Redirect stdout to capture print statements for testing comparison
# This is a common pattern for competitive programming style testing frameworks
# where the output needs to be precisely controlled and compared.
# However, for this specific problem setup where we print True/False per test,
# redirecting stdout might interfere. Let's stick to direct printing.

def ip_to_int(ip_str):
    """Converts a dotted-decimal IP string to a 32-bit integer."""
    parts = ip_str.split('.')
    ip_int = 0
    for part in parts:
        ip_int = (ip_int << 8) + int(part)
    return ip_int

def int_to_ip(ip_int):
    """Converts a 32-bit integer to a dotted-decimal IP string."""
    parts = []
    for _ in range(4):
        parts.append(str(ip_int & 255))
        ip_int >>= 8
    return '.'.join(reversed(parts))

def ip_to_cidr(ip, n):
    """
    Calculates the smallest list of CIDR blocks covering n IPs starting from ip.

    Args:
        ip: The starting IPv4 address string (e.g., "255.0.0.7").
        n: The number of consecutive IP addresses to cover.

    Returns:
        A list of strings, where each string is a CIDR block (e.g., "255.0.0.8/29").
    """
    start_ip_int = ip_to_int(ip)
    remaining_n = n
    result_cidrs = []

    current_ip_int = start_ip_int

    while remaining_n > 0:
        # Calculate the maximum possible prefix length (smallest block size)
        # based on the alignment of the current IP address.
        # The size of the block must be a power of 2, and the IP address
        # must be divisible by the block size.
        # Find the largest power of 2 that divides current_ip_int.
        # This is equivalent to finding the number of trailing zeros in its binary representation.
        
        # Handle the edge case of IP 0.0.0.0 (int 0) separately if needed, though problem constraints likely avoid it.
        # If current_ip_int is 0, it has 32 trailing zeros.
        if current_ip_int == 0:
             max_alignment_bits = 32
        else:
            # Find the value of the least significant bit (LSB) set to 1.
            # This value is the largest power of 2 that divides current_ip_int.
            lsb_power_of_2 = current_ip_int & -current_ip_int
            # The number of trailing zeros (k) is such that 2^k = lsb_power_of_2
            # k = log2(lsb_power_of_2)
            # Using bit_length(): lsb_power_of_2.bit_length() gives k+1
            max_alignment_bits = lsb_power_of_2.bit_length() - 1
            
        # Calculate the maximum possible prefix length based on the remaining count n.
        # We need a block size (2^k) such that 2^k <= remaining_n.
        # Find the largest k such that 2^k <= remaining_n.
        # k = floor(log2(remaining_n))
        if remaining_n == 1:
             max_count_bits = 0
        else:
             # Using bit_length(): remaining_n.bit_length() gives floor(log2(n)) + 1
             # So, floor(log2(n)) = remaining_n.bit_length() - 1
             max_count_bits = remaining_n.bit_length() - 1

        # The actual number of bits we can use for the host part (k) is the minimum
        # of the bits allowed by alignment and the bits allowed by the remaining count.
        k = min(max_alignment_bits, max_count_bits)

        # The size of the CIDR block is 2^k
        block_size = 1 << k
        
        # The prefix length is 32 - k
        prefix_length = 32 - k

        # Add the CIDR block to the result list
        cidr_block = f"{int_to_ip(current_ip_int)}/{prefix_length}"
        result_cidrs.append(cidr_block)

        # Update the current IP and the remaining count
        current_ip_int += block_size
        remaining_n -= block_size

    return result_cidrs

# --- Testing Framework ---

def run_tests():
    tests = [
        # Example 1 from description
        {"input": {"ip": "255.0.0.7", "n": 10}, "expected": ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]},
        # Single IP
        {"input": {"ip": "192.168.1.1", "n": 1}, "expected": ["192.168.1.1/32"]},
        # Power of 2 range starting at aligned address
        {"input": {"ip": "10.0.0.0", "n": 256}, "expected": ["10.0.0.0/24"]},
        # Power of 2 range starting at unaligned address
        {"input": {"ip": "10.0.0.1", "n": 4}, "expected": ["10.0.0.1/32", "10.0.0.2/31", "10.0.0.4/32"]}, # 1, 2-3, 4
        # Range crossing a /24 boundary
        {"input": {"ip": "192.168.0.254", "n": 4}, "expected": ["192.168.0.254/31", "192.168.1.0/31"]}, # 254-255, 0-1
        # Larger range
        {"input": {"ip": "172.16.0.10", "n": 500}, "expected": [
            '172.16.0.10/31', '172.16.0.12/30', '172.16.0.16/28', '172.16.0.32/27',
            '172.16.0.64/26', '172.16.0.128/25', '172.16.1.0/25', '172.16.1.128/26',
            '172.16.1.192/27', '172.16.1.224/28', '172.16.1.240/29', '172.16.1.248/30',
            '172.16.1.252/31', '172.16.1.254/32'
        ]}, # Covers 2+2+4+8+16+32+64+128+128+64+32+16+8+4+2+1 = 500 IPs? Let's check sizes: 2+4+16+32+64+128+128+64+32+16+8+4+2+1 = 501. Hmm, let's re-calculate the expected for 500.
        # Recalculating expected for 172.16.0.10, n=500
        # 172.16.0.10 (int ...00001010) -> /31 (size 2) -> 172.16.0.10, 172.16.0.11. n=498. next=172.16.0.12
        # 172.16.0.12 (int ...00001100) -> /30 (size 4) -> 172.16.0.12-15. n=494. next=172.16.0.16
        # 172.16.0.16 (int ...00010000) -> /28 (size 16) -> 172.16.0.16-31. n=478. next=172.16.0.32
        # 172.16.0.32 (int ...00100000) -> /27 (size 32) -> 172.16.0.32-63. n=446. next=172.16.0.64
        # 172.16.0.64 (int ...01000000) -> /26 (size 64) -> 172.16.0.64-127. n=382. next=172.16.0.128
        # 172.16.0.128(int ...10000000) -> /25 (size 128) -> 172.16.0.128-255. n=254. next=172.16.1.0
        # 172.16.1.0  (int ...00000000) -> /25 (size 128) -> 172.16.1.0-127. n=126. next=172.16.1.128
        # 172.16.1.128(int ...10000000) -> /26 (size 64) -> 172.16.1.128-191. n=62. next=172.16.1.192
        # 172.16.1.192(int ...11000000) -> /27 (size 32) -> 172.16.1.192-223. n=30. next=172.16.1.224
        # 172.16.1.224(int ...11100000) -> /28 (size 16) -> 172.16.1.224-239. n=14. next=172.16.1.240
        # 172.16.1.240(int ...11110000) -> /29 (size 8) -> 172.16.1.240-247. n=6. next=172.16.1.248
        # 172.16.1.248(int ...11111000) -> /30 (size 4) -> 172.16.1.248-251. n=2. next=172.16.1.252
        # 172.16.1.252(int ...11111100) -> /31 (size 2) -> 172.16.1.252-253. n=0. next=172.16.1.254
        # Total IPs = 2+4+16+32+64+128+128+64+32+16+8+4+2 = 500. Correct.
        {"input": {"ip": "172.16.0.10", "n": 500}, "expected": [
            '172.16.0.10/31', '172.16.0.12/30', '172.16.0.16/28', '172.16.0.32/27',
            '172.16.0.64/26', '172.16.0.128/25', '172.16.1.0/25', '172.16.1.128/26',
            '172.16.1.192/27', '172.16.1.224/28', '172.16.1.240/29', '172.16.1.248/30',
            '172.16.1.252/31'
        ]},
         # Test case from a similar LeetCode problem (751)
        {"input": {"ip": "0.0.0.0", "n": 2}, "expected": ["0.0.0.0/31"]},
        {"input": {"ip": "1.2.3.4", "n": 3}, "expected": ["1.2.3.4/32", "1.2.3.5/32", "1.2.3.6/32"]}, # Incorrect calculation in thought process, let's re-run
        # 1.2.3.4 (int ...0100) -> /32 (size 1). n=2. next=1.2.3.5
        # 1.2.3.5 (int ...0101) -> /32 (size 1). n=1. next=1.2.3.6
        # 1.2.3.6 (int ...0110) -> /32 (size 1). n=0. next=1.2.3.7
        # Expected: ["1.2.3.4/32", "1.2.3.5/32", "1.2.3.6/32"] - Corrected.
        {"input": {"ip": "1.2.3.4", "n": 3}, "expected": ["1.2.3.4/32", "1.2.3.5/32", "1.2.3.6/32"]}, # Re-adding corrected test
        {"input": {"ip": "10.0.0.5", "n": 6}, "expected": ["10.0.0.5/32", "10.0.0.6/31", "10.0.0.8/30", "10.0.0.10/32"]}, # Let's trace this
        # 10.0.0.5 (...0101) -> /32 (size 1). n=5. next=10.0.0.6
        # 10.0.0.6 (...0110) -> /31 (size 2). n=3. next=10.0.0.8
        # 10.0.0.8 (...1000) -> /30 (size 4 > n=3). Can't use /30. Try /31 (size 2). Yes. n=1. next=10.0.0.10
        # 10.0.0.10(...1010) -> /32