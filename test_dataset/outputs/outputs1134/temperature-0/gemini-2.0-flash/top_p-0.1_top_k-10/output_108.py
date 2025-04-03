def ip_to_int(ip):
    parts = ip.split('.')
    result = 0
    for i in range(4):
        result = (result << 8) + int(parts[i])
    return result

def int_to_ip(num):
    parts = []
    for i in range(4):
        parts.insert(0, str(num & 255))
        num >>= 8
    return '.'.join(parts)

def ip_to_cidr(ip, n):
    start = ip_to_int(ip)
    result = []
    while n > 0:
        mask = 32
        while mask > 0:
            masked_start = start & ((1 << mask) - 1) ^ start
            if masked_start != 0 or (n < (1 << (32 - mask))):
                mask -= 1
            else:
                break
        result.append(int_to_ip(start) + '/' + str(mask))
        start += (1 << (32 - mask))
        n -= (1 << (32 - mask))
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
            "n": 1,
            "expected": ["10.0.0.0/32"]
        },
        {
            "ip": "10.0.0.0",
            "n": 2,
            "expected": ["10.0.0.0/31"]
        },
        {
            "ip": "10.0.0.0",
            "n": 3,
            "expected": ["10.0.0.0/32", "10.0.0.1/31"]
        },
        {
            "ip": "10.0.0.0",
            "n": 4,
            "expected": ["10.0.0.0/30"]
        },
        {
            "ip": "10.0.0.0",
            "n": 5,
            "expected": ["10.0.0.0/32", "10.0.0.1/30"]
        },
        {
            "ip": "10.0.0.0",
            "n": 6,
            "expected": ["10.0.0.0/31", "10.0.0.2/31"]
        },
        {
            "ip": "10.0.0.0",
            "n": 7,
            "expected": ["10.0.0.0/32", "10.0.0.1/32", "10.0.0.2/30"]
        },
        {
            "ip": "10.0.0.0",
            "n": 9,
            "expected": ["10.0.0.0/29", "10.0.0.8/32"]
        },
        {
            "ip": "1.2.3.4",
            "n": 5,
            "expected": ["1.2.3.4/32", "1.2.3.5/30"]
        }
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        ip = test_case["ip"]
        n = test_case["n"]
        expected = test_case["expected"]
        actual = ip_to_cidr(ip, n)

        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: ip={ip}, n={n}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")

    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_ip_to_cidr()