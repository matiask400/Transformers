class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
  if not head:
    return None

  slow_ptr = fast_ptr = head
  for _ in range(n):
    fast_ptr = fast_ptr.next
  
  while fast_ptr:
    slow_ptr = slow_ptr.next
    fast_ptr = fast_ptr.next

  if not slow_ptr:
    return head.next
  else:
    slow_ptr.next = slow_ptr.next.next
    return head

# Example 1: head = [1,2,3,4,5], n = 2
input1 = ListNode(1)
input1.next = ListNode(2)
input1.next.next = ListNode(3)
input1.next.next.next = ListNode(4)
input1.next.next.next.next = ListNode(5)
output1 = remove_nth_from_end(input1, 2)
print(output1.val == 1 and output1.next.val == 2 and output1.next.next.val == 3 and output1.next.next.next.val == 5)
# Example 2: head = [1], n = 1
input2 = ListNode(1)
output2 = remove_nth_from_end(input2, 1)
print(output2 == None)
# Example 3: head = [1,2], n = 1
input3 = ListNode(1)
input3.next = ListNode(2)
output3 = remove_nth_from_end(input3, 1)
print(output3.val == 1)