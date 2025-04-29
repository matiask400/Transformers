import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    dummy = ListNode(0)
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

def run_tests(lists_input, expected_list):
    lists = [list_to_linked_list(lst) for lst in lists_input]
    result = mergeKLists(lists)
    result_list = linked_list_to_list(result)
    return result_list == expected_list

def main():
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [0]], [0,1])
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for lists_input, expected_list in test_cases:
        test_result = run_tests(lists_input, expected_list)
        print(test_result)
        if test_result:
            correct_count += 1

    print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    main()