def shortest_encoding(words):
    """
    Calculates the length of the shortest reference string possible of any valid encoding of words.

    Args:
        words: A list of strings.

    Returns:
        The length of the shortest reference string.
    """
    words = sorted(words, key=len, reverse=True)
    s = ""
    for word in words:
        if word + "#" not in s:
            s += word + "#"
    return len(s)

def test_shortest_encoding():
    """
    Tests the shortest_encoding function with several test cases.
    """
    test_cases = [
        (["time", "me", "bell"], 10),
        (["t"], 2),
        (["time", "me", "timee"], 12),
        (["time", "me", "bell", "ell"], 10),
        (["time", "me", "bell", "time"], 10),
        (["time", "me", "bell", "time", "me"], 10),
        (["time", "me", "bell", "time", "me", "bell"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me"], 10),
        (["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell"], 10),
        (["feffee", "effe", "ee"], 10),
        (["time", "atime", "btime"], 12),
        (["time", "atime", "btime", "ctime"], 14),
        (["time", "atime", "btime", "ctime", "dtime"], 16),
        (["time", "atime", "btime", "ctime", "dtime", "etime"], 18),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime"], 20),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime"], 22),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime"], 24),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime"], 26),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime"], 28),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime", "ktime"], 30),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime", "ktime", "ltime"], 32),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime", "ktime", "ltime", "mtime"], 34),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime", "ktime", "ltime", "mtime", "ntime"], 36),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime", "ktime", "ltime", "mtime", "ntime", "otime"], 38),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime", "ktime", "ltime", "mtime", "ntime", "otime", "ptime"], 40),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime", "ktime", "ltime", "mtime", "ntime", "otime", "ptime", "qtime"], 42),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime", "ktime", "ltime", "mtime", "ntime", "otime", "ptime", "qtime", "rtime"], 44),
        (["time", "atime", "btime", "ctime", "dtime", "etime", "ftime", "gtime", "htime", "itime", "jtime", "ktime", "ltime", "mtime", "ntime", "otime", "ptime", "qtime", "rtime", "stime"], 46),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for words, expected in test_cases:
        result = shortest_encoding(words)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: {words}, Expected: {expected}, Got: {result}")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_shortest_encoding()