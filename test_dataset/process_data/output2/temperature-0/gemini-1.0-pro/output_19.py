class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next

# Example 1: head = [1,2,3,4,5], n = 2
input1 = ListNode(1)
input1.next = ListNode(2)
input1.next.next = ListNode(3)
input1.next.next.next = ListNode(4)
input1.next.next.next.next = ListNode(5)
n1 = 2
output1 = removeNthFromEnd(input1, n1)
print(output1.val == 1 and output1.next.val == 2 and output1.next.next.val == 3 and output1.next.next.next.val == 5)

# Example 2: head = [1], n = 1
input2 = ListNode(1)
n2 = 1
output2 = removeNthFromEnd(input2, n2)
print(output2 == None)

# Example 3: head = [1,2], n = 1
input3 = ListNode(1)
input3.next = ListNode(2)
n3 = 1
output3 = removeNthFromEnd(input3, n3)
print(output3.val == 1)