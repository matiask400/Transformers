class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        # reverse group
        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # connect with previous and next groups
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

    return dummy.next

def get_kth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# Test Cases
inputs = [
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5], 1),
    ([1], 1)
]
outputs = [
    [2, 1, 4, 3, 5],
    [3, 2, 1, 4, 5],
    [1, 2, 3, 4, 5],
    [1]
]

for i in range(len(inputs)):
    head = create_linked_list(inputs[i][0])
    k = inputs[i][1]
    result = linked_list_to_list(reverse_k_group(head, k))
    print(result == outputs[i])