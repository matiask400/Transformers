class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy

    while head and head.next:
        # 1. Save the next two nodes
        first = head
        second = head.next

        # 2. Swap the nodes
        prev.next = second
        first.next = second.next
        second.next = first

        # 3. Move to the next pair
        prev = first
        head = first.next

    return dummy.next

# Test cases

def test_swapPairs(head_list, expected_output):
    head = ListNode(head_list[0])
    current = head
    for val in head_list[1:]:
        current.next = ListNode(val)
        current = current.next

    result = swapPairs(head)
    actual_output = []
    while result:
        actual_output.append(result.val)
        result = result.next

    print(f"Input: {head_list}")
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {actual_output}")
    print(f"Test Passed: {actual_output == expected_output}")
    print()

# Example 1
test_swapPairs([1, 2, 3, 4], [2, 1, 4, 3])

# Example 2
test_swapPairs([], [])

# Example 3
test_swapPairs([1], [1])