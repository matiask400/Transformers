def ip_to_int(ip_str):
    parts = ip_str.split('.')
    ip_int = 0
    for part in parts:
        ip_int = (ip_int << 8) + int(part)
    return ip_int

def int_to_ip(ip_int):
    parts = []
    for _ in range(4):
        parts.insert(0, str(ip_int & 255))
        ip_int >>= 8
    return ".".join(parts)

def get_cidr(ip_int, prefix_len):
    ip_str = int_to_ip(ip_int)
    return f"{ip_str}/{prefix_len}"

def get_block_size(prefix_len):
    return 1 << (32 - prefix_len)

def ip_to_cidr(ip, n):
    start_ip_int = ip_to_int(ip)
    result = []
    while n > 0:
        best_prefix_len = 32
        for prefix_len in range(31, 0, -1):
            block_size = get_block_size(prefix_len)
            if start_ip_int % block_size == 0 and block_size <= n:
                best_prefix_len = prefix_len
                break
        block_size = get_block_size(best_prefix_len)
        result.append(get_cidr(start_ip_int, best_prefix_len))
        start_ip_int += block_size
        n -= block_size
    return result

def test_ip_to_cidr():
    test_cases = [
        {
            "ip": "255.0.0.7",
            "n": 10,
            "expected": ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]
        },
        {
            "ip": "10.0.0.0",
            "n": 8,
            "expected": ["10.0.0.0/29"]
        },
        {
            "ip": "10.0.0.0",
            "n": 9,
            "expected": ["10.0.0.0/29", "10.0.0.8/32"]
        },
        {
            "ip": "10.0.0.0",
            "n": 1,
            "expected": ["10.0.0.0/32"]
        },
        {
            "ip": "10.0.0.1",
            "n": 1,
            "expected": ["10.0.0.1/32"]
        },
        {
            "ip": "10.0.0.1",
            "n": 2,
            "expected": ["10.0.0.1/32", "10.0.0.2/31"]
        },
        {
            "ip": "10.0.0.1",
            "n": 3,
            "expected": ["10.0.0.1/32", "10.0.0.2/31", "10.0.0.4/32"]
        },
        {
            "ip": "10.0.0.1",
            "n": 4,
            "expected": ["10.0.0.1/32", "10.0.0.2/31", "10.0.0.4/30"]
        },
        {
            "ip": "10.0.0.0",
            "n": 16,
            "expected": ["10.0.0.0/28"]
        },
        {
            "ip": "10.0.0.0",
            "n": 17,
            "expected": ["10.0.0.0/28", "10.0.0.16/32"]
        }


    ]
    correct_tests = 0
    total_tests = len(test_cases)
    for i, case in enumerate(test_cases):
        ip = case["ip"]
        n = case["n"]
        expected = case["expected"]
        actual = ip_to_cidr(ip, n)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: ip = {ip}, n = {n}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")
    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_ip_to_cidr()