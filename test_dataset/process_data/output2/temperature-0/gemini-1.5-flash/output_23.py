class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    # Use a min-heap to store the heads of the linked lists
    import heapq
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)

    dummy = ListNode(0)
    tail = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

# Example 1
lists_1 = [[1,4,5],[1,3,4],[2,6]]
output_1 = [1,1,2,3,4,4,5,6]

# Convert lists_1 to linked lists
head_1 = ListNode(1)
head_1.next = ListNode(4)
head_1.next.next = ListNode(5)
head_2 = ListNode(1)
head_2.next = ListNode(3)
head_2.next.next = ListNode(4)
head_3 = ListNode(2)
head_3.next = ListNode(6)
lists_1 = [head_1, head_2, head_3]

# Merge the linked lists
merged_list_1 = mergeKLists(lists_1)

# Convert the merged list back to a list for comparison
merged_list_1_values = []
while merged_list_1:
    merged_list_1_values.append(merged_list_1.val)
    merged_list_1 = merged_list_1.next

print(merged_list_1_values == output_1)  # Output: True

# Example 2
lists_2 = []
output_2 = []
print(mergeKLists(lists_2) == None)  # Output: True

# Example 3
lists_3 = [[]]
output_3 = []

# Convert lists_3 to linked lists
head_3 = None
lists_3 = [head_3]

# Merge the linked lists
merged_list_3 = mergeKLists(lists_3)

# Convert the merged list back to a list for comparison
merged_list_3_values = []
while merged_list_3:
    merged_list_3_values.append(merged_list_3.val)
    merged_list_3 = merged_list_3.next

print(merged_list_3_values == output_3)  # Output: True