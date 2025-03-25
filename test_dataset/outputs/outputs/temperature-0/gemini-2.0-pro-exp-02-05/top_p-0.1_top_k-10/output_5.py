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

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

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
    while head:
        lst.append(head.val)
        head = head.next
    return lst

def run_tests(mergeKLists):
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [0]], [0,1])
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for lists_input, expected_list in test_cases:
        linked_lists = [list_to_linked_list(lst) for lst in lists_input]
        result = mergeKLists(linked_lists)
        result_list = linked_list_to_list(result)

        if result_list == expected_list:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"  Input: lists = {lists_input}")
            print(f"  Expected: {expected_list}")
            print(f"  Got: {result_list}")

    print(f"{correct_count}/{total_tests}")

run_tests(mergeKLists)