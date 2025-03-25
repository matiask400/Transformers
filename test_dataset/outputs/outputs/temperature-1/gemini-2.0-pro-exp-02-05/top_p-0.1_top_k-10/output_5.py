import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of k sorted linked lists.

    Returns:
        The head of the merged sorted linked list.
    """

    heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))

    dummy_head = ListNode(0)
    current = dummy_head

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy_head.next

def list_to_linked_list(lst):
    dummy_head = ListNode(0)
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

def run_tests(func):
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [0]], [0,1])
    ]

    passed_tests = 0
    total_tests = len(test_cases)

    for i, (lists_lists, expected_list) in enumerate(test_cases):
        lists = [list_to_linked_list(lst) for lst in lists_lists]
        result_linked_list = func(lists)
        result_list = linked_list_to_list(result_linked_list)

        if result_list == expected_list:
            print("True")
            passed_tests += 1
        else:
            print("False")
            print(f"  Input: lists = {lists_lists}")
            print(f"  Expected: {expected_list}")
            print(f"  Got: {result_list}")

    print(f"{passed_tests}/{total_tests}")

run_tests(mergeKLists)