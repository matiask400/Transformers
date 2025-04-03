def ip_to_int(ip):
    parts = ip.split('.')
    result = 0
    for part in parts:
        result = (result << 8) + int(part)
    return result

def int_to_ip(ip_int):
    parts = []
    for _ in range(4):
        parts.insert(0, str(ip_int % 256))
        ip_int //= 256
    return '.'.join(parts)

def ip_to_cidr(ip, n):
    ip_int = ip_to_int(ip)
    result = []
    while n > 0:
        prefix_len = 32
        while prefix_len > 0:
            mask = (1 << (32 - prefix_len)) - 1
            if (ip_int & mask) != 0:
                break
            if (1 << (32 - prefix_len)) > n:
                break
            prefix_len -= 1
        result.append(int_to_ip(ip_int) + "/" + str(prefix_len))
        block_size = 1 << (32 - prefix_len)
        ip_int += block_size
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
            "ip": "1.2.3.4",
            "n": 1,
            "expected": ["1.2.3.4/32"]
        },
        {
            "ip": "1.2.3.4",
            "n": 2,
            "expected": ["1.2.3.4/31"]
        },
        {
            "ip": "1.2.3.4",
            "n": 4,
            "expected": ["1.2.3.4/30"]
        },
        {
            "ip": "1.2.3.4",
            "n": 8,
            "expected": ["1.2.3.4/29"]
        },
         {
            "ip": "170.168.162.158",
            "n": 4,
            "expected": ['170.168.162.158/30']
        },
        {
            "ip": "170.168.162.158",
            "n": 5,
            "expected": ['170.168.162.158/30', '170.168.162.162/32']
        }
    ]

    num_correct = 0
    for i, test_case in enumerate(test_cases):
        ip = test_case["ip"]
        n = test_case["n"]
        expected = test_case["expected"]
        actual = ip_to_cidr(ip, n)
        if actual == expected:
            print("True")
            num_correct += 1
        else:
            print("False")
            print(f"Test case {i + 1} failed:")
            print(f"  Input: ip = {ip}, n = {n}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")

    print(f"{num_correct}/{len(test_cases)}")

if __name__ == "__main__":
    test_ip_to_cidr()