def reverse_k_nodes(head: ListNode, k: int) -> ListNode:
    if not head or k == 1:
        return head

    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    while curr:
        last_node_of_prev = prev
        last_node_of_current = curr

        i = 0
        while curr and i < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1

        last_node_of_current.next = curr
        last_node_of_prev.next = prev
        prev = last_node_of_current

    return dummy.next


input1 = [1, 2, 3, 4, 5]
output1 = [2, 1, 4, 3, 5]
result1 = reverse_k_nodes(ListNode.construct_from_list(input1), 2)
print("Correct answer?", result1 == ListNode.construct_from_list(output1))


input2 = [1, 2, 3, 4, 5]
output2 = [3, 2, 1, 4, 5]
result2 = reverse_k_nodes(ListNode.construct_from_list(input2), 3)
print("Correct answer?", result2 == ListNode.construct_from_list(output2))


input3 = [1, 2, 3, 4, 5]
output3 = [1, 2, 3, 4, 5]
result3 = reverse_k_nodes(ListNode.construct_from_list(input3), 1)
print("Correct answer?", result3 == ListNode.construct_from_list(output3))