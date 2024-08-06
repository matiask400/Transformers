from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev = dummy
    curr = head
    while curr:
        last = prev
        for i in range(k):
            if not curr:
                break
            curr = curr.next
            last = last.next
        if not curr:
            break
        start = last.next
        end = last
        while start != end:
            tmp = start.next
            start.next = end
            end = start
            start = tmp
        prev.next = last
        prev = last
        curr = last.next
    return dummy.next


input1 = [1,2,3,4,5]
input2 = [1,2,3,4,5]
input3 = [1,2,3,4,5]
input4 = [1]

output1 = [2,1,4,3,5]
output2 = [3,2,1,4,5]
output3 = [1,2,3,4,5]
output4 = [1]

print(reverse_k_group(None, 1) == None)
print(reverse_k_group(ListNode(1), 1) == ListNode(1))
print(reverse_k_group(ListNode(1, ListNode(2)), 1) == ListNode(1, ListNode(2)))
print(reverse_k_group(ListNode(1, ListNode(2, ListNode(3))), 1) == ListNode(1, ListNode(2, ListNode(3)))
print(reverse_k_group(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1) == ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))) 

print(reverse_k_group(ListNode(*input1), 2) == ListNode(*output1))
print(reverse_k_group(ListNode(*input2), 3) == ListNode(*output2))
print(reverse_k_group(ListNode(*input3), 1) == ListNode(*output3))
print(reverse_k_group(ListNode(*input4), 3) == ListNode(*output4))