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
        The sum of the two numbers as a linked list.
    """

    carry = 0
    head = None
    tail = None

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum_vals = val1 + val2 + carry
        digit = sum_vals % 10
        carry = sum_vals // 10

        new_node = ListNode(digit)

        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return head

def list_to_linked_list(lst: list) -> ListNode:
    """
    Converts a list to a linked list.

    Args:
        lst: The list to convert.

    Returns:
        The head of the linked list.
    """
    head = None
    tail = None
    for val in lst:
        new_node = ListNode(val)
        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def linked_list_to_list(head: ListNode) -> list:
    """
    Converts a linked list to a list.

    Args:
        head: The head of the linked list.

    Returns:
        The list representation of the linked list.
    """
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst


def test_add_two_numbers():
    """
    Tests the addTwoNumbers function.
    """
    tests = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [5, 6, 4], [6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),

    ]

    correct_count = 0
    for i, (l1_list, l2_list, expected_output) in enumerate(tests):
        l1 = list_to_linked_list(l1_list)
        l2 = list_to_linked_list(l2_list)
        result_linked_list = addTwoNumbers(l1, l2)
        result_list = linked_list_to_list(result_linked_list)

        if result_list == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Test {i+1} Failed. Expected: {expected_output}, Got: {result_list}")
            

    print(f"{correct_count}/{len(tests)}")

test_add_two_numbers()