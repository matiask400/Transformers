from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[ListNode]) -> ListNode:
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2

    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedList1 = mergeTwoLists(lists[0], lists[1])
        lists.pop(0)
        lists.pop(0)
        lists.insert(0, mergedList1)

    return lists[0]


# Example 1: Test Case
input1 = [[1,4,5],[1,3,4],[2,6]]
result1 = mergeKLists(input1)
print(result1.val == 1 and result1.next.val == 1 and result1.next.next.val == 2 and result1.next.next.next.val == 3 and result1.next.next.next.next.val == 4 and result1.next.next.next.next.next.val == 4 and result1.next.next.next.next.next.next.val == 5 and result1.next.next.next.next.next.next.next.val == 6)

# Example 2: Test Case
input2 = []
result2 = mergeKLists(input2)
print(not result2)

# Example 3: Test Case
input3 = [[]]
result3 = mergeKLists(input3)
print(not result3)