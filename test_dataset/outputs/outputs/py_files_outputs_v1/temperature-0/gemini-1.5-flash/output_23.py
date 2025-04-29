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

    dummy = ListNode()
    tail = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

# Function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

# Function to convert a linked list to a list
def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

# Test cases
input_1 = [[1,4,5],[1,3,4],[2,6]]
output_1 = [1,1,2,3,4,4,5,6]
input_2 = []
output_2 = []
input_3 = [[]]
output_3 = []

# Convert input lists to linked lists
input_1 = [list_to_linked_list(l) for l in input_1]
input_3 = [list_to_linked_list(l) for l in input_3]

# Run the mergeKLists function
result_1 = mergeKLists(input_1)
result_2 = mergeKLists(input_2)
result_3 = mergeKLists(input_3)

# Convert results back to lists
result_1 = linked_list_to_list(result_1)
result_2 = linked_list_to_list(result_2)
result_3 = linked_list_to_list(result_3)

# Check if the results match the expected outputs
check_1 = result_1 == output_1
check_2 = result_2 == output_2
check_3 = result_3 == output_3

print(f"Input 1: {input_1}")
print(f"Output 1: {output_1}")
print(f"Result 1: {result_1}")
print(f"Check 1: {check_1}")
print(f"Input 2: {input_2}")
print(f"Output 2: {output_2}")
print(f"Result 2: {result_2}")
print(f"Check 2: {check_2}")
print(f"Input 3: {input_3}")
print(f"Output 3: {output_3}")
print(f"Result 3: {result_3}")
print(f"Check 3: {check_3}")