l1 = []
l2 = []
print(mergeTwoLists(l1, l2))

l1 = [1,2,4]
l2 = [1,3,4]
print(mergeTwoLists(l1, l2))

l1 = []
l2 = [0]
print(mergeTwoLists(l1, l2))
def mergeTwoLists(l1, l2):
    dummy = ListNode()
    pre = dummy
    cur1, cur2 = l1, l2
    while cur1 and cur2:
        if cur1.val <= cur2.val:
            pre.next = cur1
            cur1 = cur1.next
        else:
            pre.next = cur2
            cur2 = cur2.next
        pre = pre.next
    pre.next = cur1 or cur2
    return dummy.next

class ListNode:
    def __init__(self, x=0):
        self.val = x