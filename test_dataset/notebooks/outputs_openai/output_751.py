import math

def ip_to_int(ip):
    parts = list(map(int, ip.split('.')))
    return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]

def int_to_ip(x):
    return f"{(x >> 24) & 255}.{(x >> 16) & 255}.{(x >> 8) & 255}.{x & 255}"

def ipToCIDR(ip, n):
    result = []
    current = ip_to_int(ip)
    while n > 0:
        # Find the largest power of two block
        max_size = current & -current
        max_power = 1 << (n.bit_length() - 1)
        size = min(max_size, max_power)
        # Calculate prefix length
        prefix = 32 - int(math.log2(size))
        result.append(f"{int_to_ip(current)}/{prefix}")
        current += size
        n -= size
    return result

# Test cases: (ip, n, expected_output)
test_cases = [
    (
        "255.0.0.7",
        10,
        ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
    ),
    (
        "192.168.1.0",
        256,
        ["192.168.1.0/24"]
    ),
    (
        "0.0.0.0",
        1,
        ["0.0.0.0/32"]
    ),
    (
        "255.255.255.255",
        1,
        ["255.255.255.255/32"]
    ),
    (
        "192.168.0.0",
        4,
        ["192.168.0.0/30"]
    ),
    (
        "10.0.0.0",
        5,
        ["10.0.0.0/29", "10.0.0.8/32"]
    ),
    (
        "1.2.3.4",
        7,
        ["1.2.3.4/32", "1.2.3.5/32", "1.2.3.6/31", "1.2.3.8/32"]
    ),
    (
        "123.45.67.89",
        10,
        ["123.45.67.89/32","123.45.67.90/31","123.45.67.92/30","123.45.67.96/32"]
    )
]

correct = 0
total = len(test_cases)

for ip, n, expected in test_cases:
    output = ipToCIDR(ip, n)
    if output == expected:
        print("True")
        correct +=1
    else:
        print("False")

print(f"{correct}/{total}")