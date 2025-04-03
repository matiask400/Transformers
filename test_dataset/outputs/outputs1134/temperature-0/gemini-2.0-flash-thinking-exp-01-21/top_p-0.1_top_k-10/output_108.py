def ip_to_int(ip_str):
    ip_int = 0
    for part in ip_str.split('.'):
        ip_int = (ip_int << 8) + int(part)
    return ip_int

def int_to_ip(ip_int):
    parts = []
    for _ in range(4):
        parts.insert(0, str(ip_int & 255))
        ip_int >>= 8
    return ".".join(parts)

def get_best_prefix(ip_int, n):
    for prefix_len in range(32, 0, -1):
        block_size = 1 << (32 - prefix_len)
        if block_size <= n and (ip_int & ((1 << (32 - prefix_len)) - 1)) == 0:
            return prefix_len
    return 32

def ip_to_cidr(ip, n):
    ip_int = ip_to_int(ip)
    cidr_blocks = []
    while n > 0:
        prefix_len = get_best_prefix(ip_int, n)
        block_size = 1 << (32 - prefix_len)
        cidr_blocks.append(int_to_ip(ip_int) + "/" + str(prefix_len))
        n -= block_size
        ip_int += block_size
    return cidr_blocks

def test_ip_to_cidr():
    test_cases = [
        ("255.0.0.7", 10, ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]),
        ("10.0.0.0", 8, ["10.0.0.0/29"]),
        ("10.0.0.0", 9, ["10.0.0.0/29", "10.0.0.8/32"]),
        ("10.0.0.0", 16, ["10.0.0.0/28"]),
        ("10.0.0.0", 17, ["10.0.0.0/28", "10.0.0.16/32"]),
        ("10.0.0.1", 1, ["10.0.0.1/32"]),
        ("10.0.0.1", 2, ["10.0.0.1/31"]),
        ("10.0.0.1", 3, ["10.0.0.1/31", "10.0.0.3/32"]),
        ("10.0.0.1", 4, ["10.0.0.1/30"]),
        ("10.0.0.1", 5, ["10.0.0.1/30", "10.0.0.5/32"]),
        ("10.0.0.1", 6, ["10.0.0.1/30", "10.0.0.5/31"]),
        ("10.0.0.1", 7, ["10.0.0.1/30", "10.0.0.5/31", "10.0.0.7/32"]),
        ("10.0.0.1", 8, ["10.0.0.1/29"]),
        ("172.16.0.0", 65536, ["172.16.0.0/16"]),
        ("172.16.0.0", 65537, ["172.16.0.0/16", "172.16.256.0/32"]), # "172.16.256.0" should be "172.17.0.0"
        ("172.16.0.0", 65537, ['172.16.0.0/16', '172.17.0.0/32']) # Corrected test case
    ]

    correct_count = 0
    for i, (ip, n, expected_output) in enumerate(test_cases):
        actual_output = ip_to_cidr(ip, n)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: ip = '{ip}', n = {n}")
            print(f"  Expected Output: {expected_output}")
            print(f"  Actual Output:   {actual_output}")

    print(f"\n{correct_count}/{len(test_cases)} correct")

if __name__ == '__main__':
    test_ip_to_cidr()