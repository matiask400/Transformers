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
    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, head))

    dummy = ListNode(0)
    tail = dummy

    while heap:
        val, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))

    return dummy.next

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

    for i, (lists_input, expected_list) in enumerate(test_cases):
        linked_lists = [list_to_linked_list(lst) for lst in lists_input]
        result_linked_list = func(linked_lists)
        result_list = linked_list_to_list(result_linked_list)

        if result_list == expected_list:
            print("True")
            passed_tests += 1
        else:
            print("False")
            print(f"  Input: lists = {lists_input}")
            print(f"  Expected: {expected_list}")
            print(f"  Got: {result_list}")

    print(f"{passed_tests}/{total_tests}")

run_tests(mergeKLists)