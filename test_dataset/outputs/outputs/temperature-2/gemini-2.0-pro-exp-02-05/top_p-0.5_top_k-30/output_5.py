import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of k sorted linked lists.

    Returns:
        The head of the merged sorted linked list.
    """
    min_heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(min_heap, (head.val, i, head))

    dummy = ListNode()
    tail = dummy

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next

def list_to_linked_list(lst):
    """Converts a list to a linked list."""
    dummy = ListNode()
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

def linked_list_to_list(head):
    """Converts a linked list to a list."""
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

def test_mergeKLists(lists, expected_output):
    """
    Tests the mergeKLists function.

    Args:
        lists: A list of k sorted linked lists.
        expected_output: The expected output list.
    """
    input_linked_lists = [list_to_linked_list(lst) for lst in lists]
    merged_list = mergeKLists(input_linked_lists)
    output_list = linked_list_to_list(merged_list)
    return output_list == expected_output

def run_tests():
    """Runs test cases for the mergeKLists function."""
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [0]], [0, 1]),
    ]

    passed_tests = 0
    total_tests = len(test_cases)

    for i, (lists, expected_output) in enumerate(test_cases):
        result = test_mergeKLists(lists, expected_output)
        print(result)
        if result:
            passed_tests += 1

    print(f"{passed_tests}/{total_tests} tests passed")

if __name__ == "__main__":
    run_tests()