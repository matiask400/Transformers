from heapq import heappop, heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            heappush(min_heap, (lst[0], i, 0))

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, lst_idx, ele_idx = heappop(min_heap)
        current.next = ListNode(val)
        current = current.next

        if ele_idx + 1 < len(lists[lst_idx]):
            heappush(min_heap, (lists[lst_idx][ele_idx + 1], lst_idx, ele_idx + 1))

    return dummy.next

# Example inputs
input_1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
expected_output_1 = [1, 1, 2, 3, 4, 4, 5, 6]
output_1 = mergeKLists(input_1)
print(output_1 == expected_output_1)  # True

input_2 = []
expected_output_2 = []
output_2 = mergeKLists(input_2)
print(output_2 == expected_output_2)  # True

input_3 = [[]]
expected_output_3 = []
output_3 = mergeKLists(input_3)
print(output_3 == expected_output_3)  # True