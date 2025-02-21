def mergeKLists(lists):
    import heapq
    min_heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l[0], i, 0))
    result = []
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
    return result

# Example inputs
input_1 = [[1,4,5],[1,3,4],[2,6]]
output_1 = [1,1,2,3,4,4,5,6]
input_2 = []
output_2 = []
input_3 = [[]]
output_3 = []

# Testing the function
print(mergeKLists(input_1) == output_1)  # True
print(mergeKLists(input_2) == output_2)  # True
print(mergeKLists(input_3) == output_3)  # True