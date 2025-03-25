class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummyHead = ListNode(0)
    current = dummyHead
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum = x + y + carry
        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummyHead.next

def list_to_linked_list(lst):
    dummyHead = ListNode(0)
    current = dummyHead
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummyHead.next

def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

def test_addTwoNumbers():
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])
    ]
    
    correct_count = 0
    total_tests = len(test_cases)
    
    for l1_list, l2_list, expected_list in test_cases:
        l1 = list_to_linked_list(l1_list)
        l2 = list_to_linked_list(l2_list)
        result_linked_list = addTwoNumbers(l1, l2)
        result_list = linked_list_to_list(result_linked_list)
        
        if result_list == expected_list:
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{total_tests}")

if __name__ == '__main__':
    test_addTwoNumbers()