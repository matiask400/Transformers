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
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
    ([1], 1, [1]),
]

for i, (input_list, k, expected_output) in enumerate(test_cases):
    head = create_linked_list(input_list)
    result_head = reverse_k_group(head, k)
    result_list = linked_list_to_list(result_head)
    print(f'Test case {i+1}: {result_list == expected_output}')