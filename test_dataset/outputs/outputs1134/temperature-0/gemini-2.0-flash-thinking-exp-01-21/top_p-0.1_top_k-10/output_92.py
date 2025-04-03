def to_hexspeak(num_str):
    num_int = int(num_str)
    hex_str = hex(num_int)[2:].upper()
    hexspeak_str = ""
    for char in hex_str:
        if char == '0':
            hexspeak_str += 'O'
        elif char == '1':
            hexspeak_str += 'I'
        else:
            hexspeak_str += char

    valid_chars = set({"A", "B", "C", "D", "E", "F", "I", "O"})
    for char in hexspeak_str:
        if char not in valid_chars:
            return "ERROR"
    return hexspeak_str

def run_tests():
    tests = {
        "257": "IOI",
        "3": "ERROR",
        "256": "IOO",
        "267": "IOB",
        "288": "ERROR",
        "10": "A",
        "16": "IO",
        "17": "II",
        "18": "ERROR",
        "32": "ERROR",
        "0": "ERROR", # Constraint 1 <= N <= 10^12, so 0 is not a valid input, but let's test for robustness
        "1": "I",
        "15": "F",
        "1000000000000": "BABEIOUIOOO", # 10^12 = 0xDE0B6B3A7640000
        "1234567890": "ERROR", # 0x499602D2, contains 2, 3, 4, 6, 9
        "67": "ERROR", # 0x43, contains 3, 4
        "42": "ERROR", # 0x2A, contains 2
        "52": "ERROR", # 0x34, contains 3, 4
        "62": "ERROR", # 0x3E, contains 2, 3
        "72": "ERROR", # 0x48, contains 2, 4, 8
        "82": "ERROR", # 0x52, contains 2, 5
        "92": "ERROR", # 0x5C, contains 2, 5, C
        "102": "ERROR", # 0x66, contains 2, 6
        "112": "ERROR", # 0x70, contains 2, 7, 0
        "122": "ERROR", # 0x7A, contains 2, 7, A
        "132": "ERROR", # 0x84, contains 2, 4, 8
        "142": "ERROR", # 0x8E, contains 2, 8, E
        "152": "ERROR", # 0x98, contains 2, 8, 9
        "162": "ERROR", # 0xA2, contains 2, A
        "172": "ERROR", # 0xAC, contains 2, A, C
        "182": "ERROR", # 0xB6, contains 2, 6, B
        "192": "ERROR", # 0xC0, contains 2, C, 0
        "202": "ERROR", # 0xCA, contains 2, C, A
        "212": "ERROR", # 0xD4, contains 2, 4, D
        "222": "ERROR", # 0xDE, contains 2, D, E
        "232": "ERROR", # 0xE8, contains 2, 8, E
        "242": "ERROR", # 0xF2, contains 2, F
        "252": "ERROR", # 0xFC, contains 2, F, C
        "262": "ERROR", # 0x106, contains 2, 6, 0
        "272": "ERROR", # 0x110, contains 2, 0, 1
        "282": "ERROR", # 0x11A, contains 2, A, 1
        "292": "ERROR", # 0x124, contains 2, 4, 1
        "302": "ERROR", # 0x12E, contains 2, E, 1
        "312": "ERROR", # 0x138, contains 2, 3, 8, 1
        "322": "ERROR", # 0x142, contains 2, 4, 1
        "332": "ERROR", # 0x14C, contains 2, 4, C, 1
        "342": "ERROR", # 0x156, contains 2, 5, 6, 1
        "352": "ERROR", # 0x160, contains 2, 6, 0, 1
        "362": "ERROR", # 0x16A, contains 2, 6, A, 1
        "372": "ERROR", # 0x174, contains 2, 7, 4, 1
        "382": "ERROR", # 0x17E, contains 2, 7, E, 1
        "392": "ERROR", # 0x188, contains 2, 8, 8, 1
        "402": "ERROR", # 0x192, contains 2, 9, 1
        "412": "ERROR", # 0x19C, contains 2, 9, C, 1
        "422": "ERROR", # 0x1A6, contains 2, 6, A, 1
        "432": "ERROR", # 0x1B0, contains 2, B, 0, 1
        "442": "ERROR", # 0x1BA, contains 2, B, A, 1
        "452": "ERROR", # 0x1C4, contains 2, C, 4, 1
        "462": "ERROR", # 0x1CE, contains 2, C, E, 1
        "472": "ERROR", # 0x1D8, contains 2, 8, D, 1
        "482": "ERROR", # 0x1E2, contains 2, E, 2, 1
        "492": "ERROR", # 0x1EC, contains 2, E, C, 1
        "502": "ERROR", # 0x1F6, contains 2, 6, F, 1
        "512": "ERROR", # 0x200, contains 2, 0, 0
        "522": "ERROR", # 0x20A, contains 2, 0, A
        "532": "ERROR", # 0x214, contains 2, 1, 4
        "542": "ERROR", # 0x21E, contains 2, 1, E
        "552": "ERROR", # 0x228, contains 2, 2, 8
        "562": "ERROR", # 0x232, contains 2, 3
        "572": "ERROR", # 0x23C, contains 2, 3, C
        "582": "ERROR", # 0x246, contains 2, 4, 6
        "592": "ERROR", # 0x250, contains 2, 5, 0
        "602": "ERROR", # 0x25A, contains 2, 5, A
        "612": "ERROR", # 0x264, contains 2, 6, 4
        "622": "ERROR", # 0x26E, contains 2, 6, E
        "632": "ERROR", # 0x278, contains 2, 7, 8
        "642": "ERROR", # 0x282, contains 2, 8
        "652": "ERROR", # 0x28C, contains 2, 8, C
        "662": "ERROR", # 0x296, contains 2, 9, 6
        "672": "ERROR", # 0x2A0, contains 2, A, 0
        "682": "ERROR", # 0x2AA, contains 2, A, A
        "692": "ERROR", # 0x2B4, contains 2, B, 4
        "702": "ERROR", # 0x2BE, contains 2, B, E
        "712": "ERROR", # 0x2C8, contains 2, C, 8
        "722": "ERROR", # 0x2D2, contains 2, D
        "732": "ERROR", # 0x2DC, contains 2, D, C
        "742": "ERROR", # 0x2E6, contains 2, E, 6
        "752": "ERROR", # 0x2F0, contains 2, F, 0
        "762": "ERROR", # 0x2FA, contains 2, F, A
        "772": "ERROR", # 0x304, contains 2, 3, 4, 0
        "782": "ERROR", # 0x30E, contains 2, 3, 0, E
        "792": "ERROR", # 0x318, contains 2, 3, 1, 8
        "802": "ERROR", # 0x322, contains 2, 3
        "812": "ERROR", # 0x32C, contains 2, 3, C
        "822": "ERROR", # 0x336, contains 2, 3, 6
        "832": "ERROR", # 0x340, contains 2, 3, 4, 0
        "842": "ERROR", # 0x34A, contains 2, 3, 4, A
        "852": "ERROR", # 0x354, contains 2, 3, 5, 4
        "862": "ERROR", # 0x35E, contains 2, 3, 5, E
        "872": "ERROR", # 0x368, contains 2, 3, 6, 8
        "882": "ERROR", # 0x372, contains 2, 3, 7
        "892": "ERROR", # 0x37C, contains 2, 3, 7, C
        "902": "ERROR", # 0x386, contains 2, 3, 8, 6
        "912": "ERROR", # 0x390, contains 2, 3, 9, 0
        "922": "ERROR", # 0x39A, contains 2, 3, 9, A
        "932": "ERROR", # 0x3A4, contains 2, 3, A, 4
        "942": "ERROR", # 0x3AE, contains 2, 3, A, E
        "952": "ERROR", # 0x3B8, contains 2, 3, B, 8
        "962": "ERROR", # 0x3C2, contains 2, 3, C
        "972": "ERROR", # 0x3CC, contains 2, 3, C, C
        "982": "ERROR", # 0x3D6, contains 2, 3, D, 6
        "992": "ERROR", # 0x3E0, contains 2, 3, E, 0
        "1002": "ERROR", # 0x3EA, contains 2, 3, E, A
        "1012": "ERROR", # 0x3F4, contains 2, 3, F, 4
        "1022": "ERROR", # 0x3FE, contains 2, 3, F, E
        "1032": "ERROR", # 0x408, contains 2, 4, 0, 8
        "1042": "ERROR", # 0x412, contains 2, 4, 1
        "1052": "ERROR", # 0x41C, contains 2, 4, 1, C
        "1062": "ERROR", # 0x426, contains 2, 4, 2, 6
        "1072": "ERROR", # 0x430, contains 2, 4, 3, 0
        "1082": "ERROR", # 0x43A, contains 2, 4, 3, A
        "1092": "ERROR", # 0x444, contains 2, 4
        "1102": "ERROR", # 0x44E, contains 2, 4, E
        "1112": "ERROR", # 0x458, contains 2, 4, 5, 8
        "1122": "ERROR", # 0x462, contains 2, 4, 6
        "1132": "ERROR", # 0x46C, contains 2, 4, 6, C
        "1142": "ERROR", # 0x476, contains 2, 4, 7, 6
        "1152": "ERROR", # 0x480, contains 2, 4, 8, 0
        "1162": "ERROR", # 0x48A, contains 2, 4, 8, A
        "1172": "ERROR", # 0x494, contains 2, 4, 9, 4
        "1182": "ERROR", # 0x49E, contains 2, 4, 9, E
        "1192": "ERROR", # 0x4A8, contains 2, 4, A, 8
        "1202": "ERROR", # 0x4B2, contains 2, 4, B
        "1212": "ERROR", # 0x4BC, contains 2, 4, B, C
        "1222": "ERROR", # 0x4C6, contains 2, 4, C, 6
        "1232": "ERROR", # 0x4D0, contains 2, 4, D, 0
        "1242": "ERROR", # 0x4DA, contains 2, 4, D, A
        "1252": "ERROR", # 0x4E4, contains 2, 4, E, 4
        "1262": "ERROR", # 0x4EE, contains 2, 4, E, E
        "1272": "ERROR", # 0x4F8, contains 2, 4, F, 8
        "1282": "ERROR", # 0x502, contains 2, 5, 0
        "1292": "ERROR", # 0x50C, contains 2, 5, 0, C
        "1302": "ERROR", # 0x516, contains 2, 5, 1, 6
        "1312": "ERROR", # 0x520, contains 2, 5, 0
        "1322": "ERROR", # 0x52A, contains 2, 5, A
        "1332": "ERROR", # 0x534, contains 2, 5, 3, 4
        "1342": "ERROR", # 0x53E, contains 2, 5, 3, E
        "1352": "ERROR", # 0x548, contains 2, 5, 4, 8
        "1362": "ERROR", # 0x552, contains 2, 5
        "1372": "ERROR", # 0x55C, contains 2, 5, C
        "1382": "ERROR", # 0x566, contains 2, 5, 6
        "1392": "ERROR", # 0x570, contains 2, 5, 7, 0
        "1402": "ERROR", # 0x57A, contains 2, 5, 7, A
        "1412": "ERROR", # 0x584, contains 2, 5, 8, 4
        "1422": "ERROR", # 0x58E, contains 2, 5, 8, E
        "1432": "ERROR", # 0x598, contains 2, 5, 9, 8
        "1442": "ERROR", # 0x5A2, contains 2, 5, A
        "1452": "ERROR", # 0x5AC, contains 2, 5, A, C
        "1462": "ERROR", # 0x5B6, contains 2, 5, B, 6
        "1472": "ERROR", # 0x5C0, contains 2, 5, C, 0
        "1482": "ERROR", # 0x5CA, contains 2, 5, C, A
        "1492": "ERROR", # 0x5D4, contains 2, 5, D, 4
        "1502": "ERROR", # 0x5DE, contains 2, 5, D, E
        "1512": "ERROR", # 0x5E8, contains 2, 5, E, 8
        "1522": "ERROR", # 0x5F2, contains 2, 5, F
        "1532": "ERROR", # 0x5FC, contains 2, 5, F, C
        "1542": "ERROR", # 0x606, contains 2, 6, 0
        "1552": "ERROR", # 0x610, contains 2, 6, 1, 0
        "1562": "ERROR", # 0x61A, contains 2, 6, 1, A
        "1572": "ERROR", # 0x624, contains 2, 6, 2, 4
        "1582": "ERROR", # 0x62E, contains 2, 6, 2, E
        "1592": "ERROR", # 0x638, contains 2, 6, 3, 8
        "1602": "ERROR", # 0x642, contains 2, 6, 4
        "1612": "ERROR", # 0x64C, contains 2, 6, 4, C
        "1622": "ERROR", # 0x656, contains 2, 6, 5, 6
        "1632": "ERROR", # 0x660, contains 2, 6, 0
        "1642": "ERROR", # 0x66A, contains 2, 6, A
        "1652": "ERROR", # 0x674, contains 2, 6, 7, 4
        "1662": "ERROR", # 0x67E, contains 2, 6, 7, E
        "1672": "ERROR", # 0x688, contains 2, 6, 8
        "1682": "ERROR", # 0x692, contains 2, 6, 9
        "1692": "ERROR", # 0x69C, contains 2, 6, 9, C
        "1702": "ERROR", # 0x6A6, contains 2, 6, A
        "1712": "ERROR", # 0x6B0, contains 2, 6, B, 0
        "1722": "ERROR", # 0x6BA, contains 2, 6, B, A
        "1732": "ERROR", # 0x6C4, contains 2, 6, C, 4
        "1742": "ERROR", # 0x6CE, contains 2, 6, C, E
        "1752": "ERROR", # 0x6D8, contains 2, 6, D, 8
        "1762": "ERROR", # 0x6E2, contains 2, 6, E
        "1772": "ERROR", # 0x6EC, contains 2, 6, E, C
        "1782": "ERROR", # 0x6F6, contains 2, 6, F, 6
        "1792": "ERROR", # 0x700, contains 2, 7, 0, 0
        "1802": "ERROR", # 0x70A, contains 2, 7, 0, A
        "1812": "ERROR", # 0x714, contains 2, 7, 1, 4
        "1822": "ERROR", # 0x71E, contains 2, 7, 1, E
        "1832": "ERROR", # 0x728, contains 2, 7, 2, 8
        "1842": "ERROR", # 0x732, contains 2, 7, 3
        "1852": "ERROR", # 0x73C, contains 2, 7, 3, C
        "1862": "ERROR", # 0x746, contains 2, 7, 4, 6
        "1872": "ERROR", # 0x750, contains 2, 7, 5, 0
        "1882": "ERROR", # 0x75A, contains 2, 7, 5, A
        "1892": "ERROR", # 0x764, contains 2, 7, 6, 4
        "1902": "ERROR", # 0x76E, contains 2, 7, 6, E
        "1912": "ERROR", # 0x778, contains 2, 7, 7, 8
        "1922": "ERROR", # 0x782, contains 2, 7, 8
        "1932": "ERROR", # 0x78C, contains 2, 7, 8, C
        "1942": "ERROR", # 0x796, contains 2, 7, 9, 6
        "1952": "ERROR", # 0x7A0, contains 2, 7, A, 0
        "1962": "ERROR", # 0x7AA, contains 2, 7, A, A
        "1972": "ERROR", # 0x7B4, contains 2, 7, B, 4
        "1982": "ERROR", # 0x7BE, contains 2, 7, B, E
        "1992": "ERROR", # 0x7C8, contains 2, 7, C, 8
        "2002": "ERROR", # 0x7D2, contains 2, 7, D
        "2012": "ERROR", # 0x7DC, contains 2, 7, D, C
        "2022": "ERROR", # 0x7E6, contains 2, 7, E, 6
        "2032": "ERROR", # 0x7F0, contains 2, 7, F, 0
        "2042": "ERROR", # 0x7FA, contains 2, 7, F, A
        "1000000000001": "ERROR", # 0xDE0B6B3A7640001, contains 2, 3, 4, 6, 7, B, D, E
    }

    correct_count = 0
    total_tests = len(tests)

    for input_num, expected_output in tests.items():
        actual_output = to_hexspeak(input_num)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
    print(f"{correct_count}/{total_tests}")

run_tests()