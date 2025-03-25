class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    import heapq

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
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst
def run_tests():
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ]
    
    test_results = []

    correct_tests = 0
    for lists, expected in test_cases:

        linked_lists = [list_to_linked_list(l) for l in lists]

        merged_list = mergeKLists(linked_lists)

        result_list = linked_list_to_list(merged_list)


        test_result = result_list == expected
        test_results.append(test_result)
        if(test_result):
            correct_tests+=1

        print(test_result)


    print(f"{correct_tests}/{len(test_cases)}")

run_tests()