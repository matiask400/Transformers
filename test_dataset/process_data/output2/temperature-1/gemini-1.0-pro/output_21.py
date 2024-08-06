l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

merged_list = mergeTwoLists(l1, l2)
print_list(merged_list)  # Expected output: [1, 1, 2, 3, 4, 4]

l1 = ListNode(0)

l2 = ListNode(-1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)

merged_list = mergeTwoLists(l1, l2)
print_list(merged_list)  # Expected output: [-1, 0, 2, 3]

l1 = ListNode(100)

l2 = ListNode()

merged_list = mergeTwoLists(l1, l2)
print_list(merged_list)  # Expected output: [100]

l1 = ListNode(-1)

l2 = ListNode(-3)
l2.next = ListNode(-3)
l2.next.next = ListNode(-1)

merged_list = mergeTwoLists(l1, l2)
print_list(merged_list)  # Expected output: [-3, -3, -1, -1]

l1 = ListNode(2)

l2 = ListNode(1)
merged_list = mergeTwoLists(l1, l2)
print_list(merged_list)  # Expected output: [1, 2]