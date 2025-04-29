class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummyHead = ListNode(0)
    curr = dummyHead
    carry = 0
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        sum_val = l1_val + l2_val + carry
        carry = sum_val // 10
        curr.next = ListNode(sum_val % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummyHead.next

def test_addTwoNumbers():
    test_cases = [
        ([2,4,3], [5,6,4], [7,0,8]),
        ([0], [0], [0]),
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
    ]
    passed = 0
    for l1_vals, l2_vals, expected_vals in test_cases:
        l1 = ListNode(l1_vals[0])
        curr = l1
        for i in range(1, len(l1_vals)):
            curr.next = ListNode(l1_vals[i])
            curr = curr.next
        l2 = ListNode(l2_vals[0])
        curr = l2
        for i in range(1, len(l2_vals)):
            curr.next = ListNode(l2_vals[i])
            curr = curr.next
        result = addTwoNumbers(l1, l2)
        result_vals = []
        while result:
            result_vals.append(result.val)
            result = result.next
        print(f'Test: {l1_vals} + {l2_vals} == {result_vals} - {result_vals == expected_vals}')
        if result_vals == expected_vals:
            passed += 1
    print(f'Passed {passed} out of {len(test_cases)} tests.')

test_addTwoNumbers()