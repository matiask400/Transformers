class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum = val1 + val2 + carry
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

def test_addTwoNumbers():
    test_cases = [
        ([2,4,3], [5,6,4], [7,0,8]),
        ([0], [0], [0]),
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
    ]
    passed = 0
    for l1_vals, l2_vals, expected_vals in test_cases:
        l1 = ListNode()
        curr = l1
        for val in l1_vals[::-1]:
            curr.next = ListNode(val)
            curr = curr.next
        l1 = l1.next

        l2 = ListNode()
        curr = l2
        for val in l2_vals[::-1]:
            curr.next = ListNode(val)
            curr = curr.next
        l2 = l2.next

        result = addTwoNumbers(l1, l2)
        actual_vals = []
        while result:
            actual_vals.append(result.val)
            result = result.next

        print(f"Test case: l1 = {l1_vals}, l2 = {l2_vals}, expected = {expected_vals}, actual = {actual_vals} - {actual_vals == expected_vals}")
        if actual_vals == expected_vals:
            passed += 1
    print(f"Passed {passed} out of {len(test_cases)} tests")

test_addTwoNumbers()