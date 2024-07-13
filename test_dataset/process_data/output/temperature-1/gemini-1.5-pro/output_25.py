class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        # reverse group
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # connect with previous and next groups
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp

    return dummy.next

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for i in range(1, len(values)):
        curr.next = ListNode(values[i])
        curr = curr.next
    return head

def linkedListToValues(head):
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values


inputs = [([1,2,3,4,5], 2), ([1,2,3,4,5], 3), ([1,2,3,4,5], 1)]
outputs = [[2,1,4,3,5], [3,2,1,4,5], [1,2,3,4,5]]

results = []
for i in range(len(inputs)):
    input_list, k = inputs[i]
    head = createLinkedList(input_list)
    result_head = reverseKGroup(head, k)
    result = linkedListToValues(result_head)
    results.append(result == outputs[i])

print(results)