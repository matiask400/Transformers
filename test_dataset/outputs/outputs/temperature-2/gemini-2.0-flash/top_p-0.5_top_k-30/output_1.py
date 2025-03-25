class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    """
    Adds two numbers represented as linked lists.

    Args:
        l1: The first linked list.
        l2: The second linked list.

    Returns:
        The sum as a linked list.
    """
    carry = 0
    dummy_head = ListNode(0)
    current = dummy_head

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

    return dummy_head.next

def linked_list_to_list(head):
    """
    Converts a linked list to a Python list.

    Args:
        head: The head of the linked list.

    Returns:
        A Python list representing the linked list.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def list_to_linked_list(lst):
    """
    Converts a Python list to a linked list.

    Args:
        lst: The Python list.

    Returns:
        The head of the linked list.
    """
    dummy_head = ListNode(0)
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def test_add_two_numbers():
    """
    Tests the add_two_numbers function.
    """
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1], [9,9,9], [0,0,0,1]),
        ([9,9], [1], [0,0,1])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for l1_list, l2_list, expected_list in test_cases:
        l1 = list_to_linked_list(l1_list)
        l2 = list_to_linked_list(l2_list)
        result_head = add_two_numbers(l1, l2)
        result_list = linked_list_to_list(result_head)

        if result_list == expected_list:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_add_two_numbers()