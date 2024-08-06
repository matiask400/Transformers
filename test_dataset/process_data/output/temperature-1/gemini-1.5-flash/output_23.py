class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    if not lists:
        return None
    
    # Create a min-heap to store the heads of all linked lists.
    import heapq
    heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))
    
    # Initialize the head of the merged list.
    dummy = ListNode(0)
    tail = dummy
    
    # Merge the linked lists.
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        
        # Add the next node of the current list to the heap.
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# Example usage

def convert_to_linked_list(nums):
    head = ListNode()
    curr = head
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return head.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def check_output(input_lists, expected_output):
    merged_list = mergeKLists([convert_to_linked_list(l) for l in input_lists])
    actual_output = linked_list_to_list(merged_list)
    return actual_output == expected_output

# Input 1
input_1 = [[1,4,5],[1,3,4],[2,6]]
output_1 = [1,1,2,3,4,4,5,6]

# Input 2
input_2 = []
output_2 = []

# Input 3
input_3 = [[]]
output_3 = []

# Check results
result_1 = check_output(input_1, output_1)
result_2 = check_output(input_2, output_2)
result_3 = check_output(input_3, output_3)

print(f"Input 1: {result_1}")
print(f"Input 2: {result_2}")
print(f"Input 3: {result_3}")