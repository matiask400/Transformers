class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    curr = head
    while curr and curr.next:
        nxt_pair = curr.next.next
        second = curr.next
        second.next = curr
        curr.next = nxt_pair
        prev.next = second
        prev = curr
        curr = nxt_pair
    return dummy.next

head = [1,2,3,4]
print(swap_pairs(head) == [2, 1, 4, 3])

head = []
print(swap_pairs(head) == [])

head = [1]
print(swap_pairs(head) == [1])