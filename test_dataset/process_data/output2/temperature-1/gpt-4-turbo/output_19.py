class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

def list_to_nodes(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_case(lst, n, expected):
    head = list_to_nodes(lst)
    new_head = removeNthFromEnd(head, n)
    result = nodes_to_list(new_head)
    return result == expected

# Test examples
print(test_case([1,2,3,4,5], 2, [1,2,3,5]))  # Example 1
print(test_case([1], 1, []))  # Example 2
print(test_case([1,2], 1, [1]))  # Example 3