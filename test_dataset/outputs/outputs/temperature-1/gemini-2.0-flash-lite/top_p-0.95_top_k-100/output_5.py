import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of sorted linked lists.

    Returns:
        The merged sorted linked list.
    """
    # Use a min-heap to efficiently merge the lists
    heap = []
    # Add the first node of each list to the heap
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))  # (value, list_index, node)

    dummy = ListNode()
    current = dummy

    while heap:
        val, list_index, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        # Add the next node from the same list to the heap
        if node.next:
            heapq.heappush(heap, (node.next.val, list_index, node.next))

    return dummy.next

def list_to_linked_list(nums):
    """Converts a list of integers to a linked list."""
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next.next

def linked_list_to_list(head):
    """Converts a linked list to a list of integers."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_merge_k_sorted_lists():
    """Tests the merge_k_sorted_lists function."""
    tests = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[1, 3, 5], [2, 4, 6]], [1, 2, 3, 4, 5, 6]),
        ([[-1, 5, 10], [2, 8], [1, 9, 12, 15]], [-1, 1, 2, 5, 8, 9, 10, 12, 15])
    ]
    correct_tests = 0
    for i, (lists_input, expected_output) in enumerate(tests):
        lists = [list_to_linked_list(lst) for lst in lists_input]
        result = merge_k_sorted_lists(lists)
        actual_output = linked_list_to_list(result)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected_output}, Actual: {actual_output})")
    print(f"Correct tests: {correct_tests}/{len(tests)}")


if __name__ == '__main__':
    test_merge_k_sorted_lists()