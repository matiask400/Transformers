class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    current = head
    while current and current.next:
        nextPair = current.next.next
        second = current.next
        second.next = current
        current.next = nextPair
        prev.next = second
        prev = current
        current = nextPair
    return dummy.next

# Example 1: Input and Output
input1 = ListNode(1)
input1.next = ListNode(2)
input1.next.next = ListNode(3)
input1.next.next.next = ListNode(4)
output1 = swapPairs(input1)
print(output1.val == 2 and output1.next.val == 1 and output1.next.next.val == 4 and output1.next.next.next.val == 3)

# Example 2: Input and Output
input2 = ListNode(1)
output2 = swapPairs(input2)
print(output2.val == 1)

# Example 3: Input and Output
input3 = None
output3 = swapPairs(input3)
print(output3 == None)