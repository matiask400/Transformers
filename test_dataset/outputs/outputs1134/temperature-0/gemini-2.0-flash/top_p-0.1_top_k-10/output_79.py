def get_smallest_string(n: int, k: int) -> str:
    """
    Given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.
    """
    result = ['a'] * n
    k -= n
    for i in range(n - 1, -1, -1):
        if k == 0:
            break
        add = min(25, k)
        result[i] = chr(ord('a') + add)
        k -= add
    return "".join(result)

def test_get_smallest_string():
    test_cases = [
        (3, 27, "aay"),
        (5, 73, "aaszz"),
        (1, 1, "a"),
        (1, 26, "z"),
        (2, 2, "aa"),
        (2, 52, "zz"),
        (4, 104, "zzzz"),
        (4, 4, "aaaa"),
        (4, 5, "aaab"),
        (4, 10, "aaaf"),
        (4, 100, "zzzy"),
        (4, 99, "zzzx"),
        (4, 98, "zzzw"),
        (4, 97, "zzzv"),
        (4, 96, "zzzu"),
        (4, 95, "zzzt"),
        (4, 94, "zzzs"),
        (4, 93, "zzzr"),
        (4, 92, "zzzq"),
        (4, 91, "zzzp"),
        (4, 90, "zzzo"),
        (4, 89, "zzzn"),
        (4, 88, "zzzm"),
        (4, 87, "zzzl"),
        (4, 86, "zzzk"),
        (4, 85, "zzzj"),
        (4, 84, "zzzi"),
        (4, 83, "zzzh"),
        (4, 82, "zzzg"),
        (4, 81, "zzzf"),
        (4, 80, "zzze"),
        (4, 79, "zzzd"),
        (4, 78, "zzzc"),
        (4, 77, "zzzb"),
        (4, 76, "zzza"),
        (4, 75, "zzyz"),
        (4, 74, "zzyy"),
        (4, 73, "zzyx"),
        (4, 72, "zzyw"),
        (4, 71, "zzyv"),
        (4, 70, "zzyu"),
        (4, 69, "zzyt"),
        (4, 68, "zzys"),
        (4, 67, "zzyr"),
        (4, 66, "zzyq"),
        (4, 65, "zzyp"),
        (4, 64, "zzyo"),
        (4, 63, "zzyn"),
        (4, 62, "zzym"),
        (4, 61, "zzyl"),
        (4, 60, "zzyk"),
        (4, 59, "zzyj"),
        (4, 58, "zzyi"),
        (4, 57, "zzyh"),
        (4, 56, "zzyg"),
        (4, 55, "zzyf"),
        (4, 54, "zzye"),
        (4, 53, "zzyd"),
        (4, 52, "zzyc"),
        (4, 51, "zzyb"),
        (4, 50, "zzya"),
        (4, 49, "zzxz"),
        (4, 48, "zzxy"),
        (4, 47, "zzxx"),
        (4, 46, "zzxw"),
        (4, 45, "zzxv"),
        (4, 44, "zzxu"),
        (4, 43, "zzxt"),
        (4, 42, "zzxs"),
        (4, 41, "zzxr"),
        (4, 40, "zzxq"),
        (4, 39, "zzxp"),
        (4, 38, "zzxo"),
        (4, 37, "zzxn"),
        (4, 36, "zzxm"),
        (4, 35, "zzxl"),
        (4, 34, "zzxk"),
        (4, 33, "zzxj"),
        (4, 32, "zzxi"),
        (4, 31, "zzxh"),
        (4, 30, "zzxg"),
        (4, 29, "zzxf"),
        (4, 28, "zzxe"),
        (4, 27, "zzxd"),
        (4, 26, "zzxc"),
        (4, 25, "zzxb"),
        (4, 24, "zzxa"),
        (4, 23, "zzwz"),
        (4, 22, "zzwy"),
        (4, 21, "zzwx"),
        (4, 20, "zzww"),
        (4, 19, "zzwv"),
        (4, 18, "zzwu"),
        (4, 17, "zzwt"),
        (4, 16, "zzws"),
        (4, 15, "zzwr"),
        (4, 14, "zzwq"),
        (4, 13, "zzwp"),
        (4, 12, "zzwo"),
        (4, 11, "zzwn"),
        (4, 10, "zzwm"),
        (4, 9, "zzwl"),
        (4, 8, "zzwk"),
        (4, 7, "zzwj"),
        (4, 6, "zzwi"),
        (4, 5, "zzwh"),
        (4, 4, "zzwg"),
        (4, 3, "zzwf"),
        (4, 2, "zzwe"),
        (4, 1, "zzwd"),
    ]
    
    correct_count = 0
    total_count = len(test_cases)
    
    for n, k, expected in test_cases:
        result = get_smallest_string(n, k)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: n={n}, k={k}")
            print(f"Expected: {expected}")
            print(f"Got: {result}")
    
    print(f"{correct_count}/{total_count}")

test_get_smallest_string()