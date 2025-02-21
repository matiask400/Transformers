def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

# Test cases
print(mergeTwoLists([1,2,4], [1,3,4]) == [1,1,2,3,4,4])
print(mergeTwoLists([], []) == [])
print(mergeTwoLists([], [0]) == [0])