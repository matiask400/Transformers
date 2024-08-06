class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        # Reverse group
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp

    return dummy.next


def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test Cases

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
input_1 = [1,2,3,4,5]
k1 = 2
output_1 = [2,1,4,3,5]
result_1 = print_linked_list(reverseKGroup(head1, k1))
print(f'Input 1: {input_1}, k: {k1}')
print(f'Output 1: {result_1}')
print(f'Test 1: {result_1 == output_1}')

# Example 2
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
input_2 = [1,2,3,4,5]
k2 = 3
output_2 = [3,2,1,4,5]
result_2 = print_linked_list(reverseKGroup(head2, k2))
print(f'Input 2: {input_2}, k: {k2}')
print(f'Output 2: {result_2}')
print(f'Test 2: {result_2 == output_2}')

# Example 3
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
input_3 = [1,2,3,4,5]
k3 = 1
output_3 = [1,2,3,4,5]
result_3 = print_linked_list(reverseKGroup(head3, k3))
print(f'Input 3: {input_3}, k: {k3}')
print(f'Output 3: {result_3}')
print(f'Test 3: {result_3 == output_3}')