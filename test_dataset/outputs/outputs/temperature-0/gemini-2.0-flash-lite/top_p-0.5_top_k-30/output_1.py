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
        The sum as a linked list.
    """
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next

        carry = sum_val // 10
        current.next = ListNode(sum_val % 10)
        current = current.next

    return dummy_head.next

def list_to_linked_list(lst):
    """Converts a list to a linked list."""
    dummy_head = ListNode(0)
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def linked_list_to_list(head):
    """Converts a linked list to a list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
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
    for i, (l1_list, l2_list, expected_list) in enumerate(tests):
        l1 = list_to_linked_list(l1_list)
        l2 = list_to_linked_list(l2_list)
        result_linked_list = addTwoNumbers(l1, l2)
        result_list = linked_list_to_list(result_linked_list)
        if result_list == expected_list:
            print(True)
            correct_tests += 1
        else:
            print(False)
    print(f"{correct_tests}/{len(tests)}")

if __name__ == '__main__':
    test_add_two_numbers()