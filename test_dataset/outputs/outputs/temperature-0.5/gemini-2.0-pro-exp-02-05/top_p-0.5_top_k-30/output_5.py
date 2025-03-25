import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    dummy = ListNode(-1)
    tail = dummy
    heap = []

    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))

    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

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

def run_tests(mergeKLists):
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ]

    passed_tests = 0
    total_tests = len(test_cases)

    for i, (lists_input, expected_list) in enumerate(test_cases):
        linked_lists = [list_to_linked_list(lst) for lst in lists_input]
        result = mergeKLists(linked_lists)
        result_list = linked_list_to_list(result)

        if result_list == expected_list:
            print(f"Test {i + 1}: True")
            passed_tests += 1
        else:
            print(f"Test {i + 1}: False")

    print(f"\n{passed_tests}/{total_tests} tests passed.")

run_tests(mergeKLists)