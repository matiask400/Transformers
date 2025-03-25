class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        digit = total_sum % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

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

def run_tests(addTwoNumbers):
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([9,9], [1], [0,0,1])
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for l1_list, l2_list, expected_list in test_cases:
        l1 = list_to_linked_list(l1_list)
        l2 = list_to_linked_list(l2_list)
        result = addTwoNumbers(l1, l2)
        result_list = linked_list_to_list(result)
        if result_list == expected_list:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"  Input: l1={l1_list}, l2={l2_list}")
            print(f"  Expected: {expected_list}")
            print(f"  Got: {result_list}")


    print(f"{correct_count}/{total_tests}")

run_tests(addTwoNumbers)