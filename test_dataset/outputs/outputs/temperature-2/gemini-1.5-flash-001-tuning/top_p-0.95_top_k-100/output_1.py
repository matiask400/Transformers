class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummyHead = ListNode(0)
    current = dummyHead
    carry = 0
    
    while l1 or l2 or carry:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        
        sumVal = l1Val + l2Val + carry
        carry = sumVal // 10
        
        current.next = ListNode(sumVal % 10)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummyHead.next

def test_addTwoNumbers():
    test_cases = [
        ([2,4,3], [5,6,4], [7,0,8]),
        ([0], [0], [0]),
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
    ]

    passed_tests = 0

    for case in test_cases:
        l1 = ListNode(case[0][0])
        l1_curr = l1
        for val in case[0][1:]:
            l1_curr.next = ListNode(val)
            l1_curr = l1_curr.next
            
        l2 = ListNode(case[1][0])
        l2_curr = l2
        for val in case[1][1:]:
            l2_curr.next = ListNode(val)
            l2_curr = l2_curr.next
            
        expected = ListNode(case[2][0])
        expected_curr = expected
        for val in case[2][1:]:
            expected_curr.next = ListNode(val)
            expected_curr = expected_curr.next
            
        result = addTwoNumbers(l1, l2)

        result_list = []
        while result:
            result_list.append(result.val)
            result = result.next

        print(f"True: {result_list == case[2]}")
        if result_list == case[2]:
            passed_tests += 1

    print(f"Passed {passed_tests}/{len(test_cases)} tests")

test_addTwoNumbers()