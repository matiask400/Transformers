class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds two numbers represented as linked lists.

    Args:
        l1: The first linked list.
        l2: The second linked list.

    Returns:
        A new linked list representing the sum of the two numbers.
    """
    dummy = ListNode()  # Dummy node to simplify code
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum_val = val1 + val2 + carry
        carry = sum_val // 10
        digit = sum_val % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

def list_to_linked_list(nums):
    """Converts a list of integers to a linked list."""
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    """Converts a linked list to a list of integers."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_add_two_numbers():
    """Tests the addTwoNumbers function."""
    tests = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
        ([1], [9, 9], [0, 0, 1])
    ]
    correct_tests = 0
    for i, (l1_nums, l2_nums, expected_nums) in enumerate(tests):
        l1 = list_to_linked_list(l1_nums)
        l2 = list_to_linked_list(l2_nums)
        result = addTwoNumbers(l1, l2)
        actual_nums = linked_list_to_list(result)
        if actual_nums == expected_nums:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"Correct tests: {correct_tests}/{len(tests)}")


if __name__ == '__main__':
    test_add_two_numbers()