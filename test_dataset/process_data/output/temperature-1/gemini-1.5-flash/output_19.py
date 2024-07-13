class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    
    for i in range(n):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    return dummy.next

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
input_1 = head1
output_1 = removeNthFromEnd(head1, 2)

# Example 2
head2 = ListNode(1)
input_2 = head2
output_2 = removeNthFromEnd(head2, 1)

# Example 3
head3 = ListNode(1, ListNode(2))
input_3 = head3
output_3 = removeNthFromEnd(head3, 1)

# Check if the outputs are correct
result_1 = output_1.val == 1 and output_1.next.val == 2 and output_1.next.next.val == 3 and output_1.next.next.next.val == 5
result_2 = output_2 is None
result_3 = output_3.val == 1

print(f"Input 1: {input_1.val}, Output 1: {output_1.val}, Result 1: {result_1}")
print(f"Input 2: {input_2.val}, Output 2: {output_2}, Result 2: {result_2}")
print(f"Input 3: {input_3.val}, Output 3: {output_3.val}, Result 3: {result_3}")