class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    import heapq

    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    dummy_head = ListNode(0)
    current = dummy_head

    while heap:
        val, list_index, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, list_index, node.next))

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
    while head:
        lst.append(head.val)
        head = head.next
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