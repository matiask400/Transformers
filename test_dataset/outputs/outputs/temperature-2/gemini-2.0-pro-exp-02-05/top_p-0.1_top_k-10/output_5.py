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

def run_tests(func):
    """Runs tests for the mergeKLists function."""
    test_cases = [
        {
            "input": [[1, 4, 5], [1, 3, 4], [2, 6]],
            "expected": [1, 1, 2, 3, 4, 4, 5, 6],
        },
        {
            "input": [],
            "expected": [],
        },
        {
            "input": [[]],
            "expected": [],
        },
        {
            "input": [[1], [0]],
            "expected": [0, 1]
        }
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_lists = [list_to_linked_list(lst) for lst in test_case["input"]]
        expected_list = test_case["expected"]
        result_head = func(input_lists)
        result_list = linked_list_to_list(result_head)
        if result_list == expected_list:
            print(f"True")
            correct_count += 1
        else:
            print(f"False")
            print(f"  Input: {test_case['input']}")
            print(f"  Expected: {expected_list}")
            print(f"  Got: {result_list}")

    print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    run_tests(mergeKLists)