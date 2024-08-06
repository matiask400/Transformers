class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists:
        return None

    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            mergedLists.append(mergeTwoLists(l1, l2))
        lists = mergedLists
    return lists[0]

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


inputs = [[[1,4,5],[1,3,4],[2,6]], [], [[]]]
outputs = [[1,1,2,3,4,4,5,6], [], []]

results = []
for i in range(len(inputs)):
    input_linked_lists = [list_to_linked_list(lst) for lst in inputs[i]]
    merged_linked_list = mergeKLists(input_linked_lists)
    output_list = linked_list_to_list(merged_linked_list)
    results.append(output_list == outputs[i])

print(results) # Output: [True, True, True]