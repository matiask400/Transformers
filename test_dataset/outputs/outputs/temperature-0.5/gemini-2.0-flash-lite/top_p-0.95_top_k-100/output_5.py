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
    heap = []
    # Add the head of each linked list to the heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))  # (value, list_index, node)

    dummy = ListNode(0)
    current = dummy

    while heap:
        val, list_index, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, list_index, node.next))

    return dummy.next


def list_to_linked_list(lst):
    """Converts a Python list to a linked list."""
    dummy_head = ListNode(0)
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next


def linked_list_to_list(head):
    """Converts a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def run_tests():
    """Runs the test cases and prints the results."""
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1, 2, 3], [], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[1], [2]], [1, 2]),
        ([[5,6,7], [1,2,3,4]], [1,2,3,4,5,6,7]),
        ([[-1, 5, 11], [6, 10], [2, 3, 4, 8, 9]], [-1, 2, 3, 4, 5, 6, 8, 9, 10, 11])
    ]
    correct_count = 0
    total_tests = len(test_cases)

    for i, (lists_input, expected_output) in enumerate(test_cases):
        lists_linked_list = []
        for lst in lists_input:
            lists_linked_list.append(list_to_linked_list(lst))

        merged_list = mergeKLists(lists_linked_list)
        result_list = linked_list_to_list(merged_list)

        if result_list == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"Correct tests: {correct_count}/{total_tests}")

run_tests()