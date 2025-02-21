def merge_k_lists(lists):
    import heapq
    heap = []
    for l in lists:
        for value in l:
            heapq.heappush(heap, value)
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    return result

# Test cases
input_1 = [[1,4,5],[1,3,4],[2,6]]
output_1 = [1,1,2,3,4,4,5,6]
input_2 = []
output_2 = []
input_3 = [[]]
output_3 = []

# Verification
print(merge_k_lists(input_1) == output_1)
print(merge_k_lists(input_2) == output_2)
print(merge_k_lists(input_3) == output_3)