def shortest_subarray_to_remove(arr):
    n = len(arr)
    if n <= 1:
        return 0

    prefix_len = 0
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            prefix_len += 1
        else:
            break
    prefix_len += 1

    suffix_len = 0
    for i in range(n - 2, -1, -1):
        if arr[i] <= arr[i+1]:
            suffix_len += 1
        else:
            break
    suffix_len += 1

    if prefix_len == n:
        return 0

    min_removed_len = n

    # Remove suffix starting from prefix end
    min_removed_len = min(min_removed_len, n - prefix_len)

    # Remove prefix until suffix start
    min_removed_len = min(min_removed_len, n - suffix_len)

    prefix_end_index = prefix_len - 1
    suffix_start_index = n - suffix_len

    if prefix_end_index < suffix_start_index - 1:
        if arr[prefix_end_index] <= arr[suffix_start_index]:
            removed_len = suffix_start_index - (prefix_end_index + 1)
            min_removed_len = min(min_removed_len, removed_len)

    if prefix_len == 0:
        min_removed_len = min(min_removed_len, n - 1)
    if suffix_len == 0:
        min_removed_len = min(min_removed_len, n - 1)

    if prefix_len == 0 and suffix_len == 0 and n > 0:
        min_removed_len = n - 1

    if prefix_len + suffix_len >= n:
        min_removed_len = 0


    is_sorted = True
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            is_sorted = False
            break
    if is_sorted:
        min_removed_len = 0


    min_removed_len = min(min_removed_len, n) # Remove all elements is always a valid option

    # Check removing prefix of length prefix_len
    remaining_arr_prefix = arr[prefix_len:]
    is_non_decreasing_prefix = True
    for i in range(1, len(remaining_arr_prefix)):
        if remaining_arr_prefix[i] < remaining_arr_prefix[i-1]:
            is_non_decreasing_prefix = False
            break
    if is_non_decreasing_prefix and n - prefix_len < min_removed_len:
        min_removed_len = n - prefix_len

    # Check removing suffix of length suffix_len
    remaining_arr_suffix = arr[:n-suffix_len]
    is_non_decreasing_suffix = True
    for i in range(1, len(remaining_arr_suffix)):
        if remaining_arr_suffix[i] < remaining_arr_suffix[i-1]:
            is_non_decreasing_suffix = False
            break
    if is_non_decreasing_suffix and n - suffix_len < min_removed_len:
        min_removed_len = n - suffix_len


    for i in range(n + 1):
        for j in range(i - 1, n):
            removed_len = 0
            remaining_arr = []
            if j < i - 1:
                remaining_arr = arr[:]
                removed_len = 0
            else:
                remaining_arr = arr[:i] + arr[j+1:]
                removed_len = j - i + 1

            is_non_decreasing = True
            for k in range