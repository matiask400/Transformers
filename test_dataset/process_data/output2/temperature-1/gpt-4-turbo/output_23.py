import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    min_heap = []
    dummy = ListNode(-1)
    current = dummy
    for index, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst.val, index, lst))
    while min_heap:
        value, index, node = heapq.heappop(min_heap)
        current.next = ListNode(value)
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, index, node.next))
    return dummy.next

def convert_to_list(lists):
    result = []
    for root in lists:
        values = []
        while root:
            values.append(root.val)
            root = root.next
        result.append(values)
    return result

# Test cases
input_1 = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
expected_1 = [1,1,2,3,4,4,5,6]
print(convert_to_list([merge_k_lists(input_1)]) == [expected_1])

input_2 = []
expected_2 = []
print(convert_to_list([merge_k_lists(input_2)]) == [expected_2])

input_3 = [[]]
expected_3 = []
print(convert_to_list([merge_k_lists(input_3)]) == [expected_3])