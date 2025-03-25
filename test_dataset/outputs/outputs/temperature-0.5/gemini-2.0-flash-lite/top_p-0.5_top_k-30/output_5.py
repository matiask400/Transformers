import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of sorted linked lists.

    Returns:
        The merged sorted linked list.
    """
    # Use a min-heap to efficiently merge the lists
    heap = []
    # Add the head of each list to the heap
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))  # (value, list_index, node)

    dummy = ListNode()
    current = dummy

    while heap:
        # Get the smallest node from the heap
        val, list_index, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        # Add the next node from the same list to the heap
        if node.next:
            heapq.heappush(heap, (node.next.val, list_index, node.next))

    return dummy.next

def list_to_linked_list(lst):
    """Converts a list to a linked list."""
    dummy_head = ListNode()
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def linked_list_to_list(head):
    """Converts a linked list to a list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def run_tests():
    """Runs the tests and prints the results."""
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[1, 2], [3, 4, 5]], [1, 2, 3, 4, 5]),
        ([[1], [2]], [1, 2]),
        ([[1, 2, 3], [], [4, 5]], [1, 2, 3, 4, 5]),
        ([[-1, 5, 10, 11], [0, 2, 6, 12], [1, 3, 7, 9]], [-1, 0, 1, 2, 3, 5, 6, 7, 9, 10, 11, 12])
    ]
    correct_tests = 0
    for i, (lists_input, expected_output) in enumerate(test_cases):
        lists_linked_list = []
        for lst in lists_input:
            lists_linked_list.append(list_to_linked_list(lst))
        result_linked_list = mergeKLists(lists_linked_list)
        result_list = linked_list_to_list(result_linked_list)
        if result_list == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"Correct tests: {correct_tests}/{len(test_cases)}")

run_tests()