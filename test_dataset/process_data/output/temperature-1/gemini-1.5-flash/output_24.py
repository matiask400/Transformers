class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
        # 1. Define the nodes to be swapped
        node1 = prev.next
        node2 = prev.next.next

        # 2. Swap the nodes
        prev.next = node2
        node1.next = node2.next
        node2.next = node1

        # 3. Move prev to the next pair
        prev = node1

    return dummy.next

# Test the function
def test_swapPairs():
    # Example 1
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    expected_output1 = [2, 1, 4, 3]
    result1 = swapPairs(head1)
    output1 = []
    while result1:
        output1.append(result1.val)
        result1 = result1.next
    print(f"Example 1: Input: {expected_output1}, Output: {output1}, Result: {output1 == expected_output1}")

    # Example 2
    head2 = None
    expected_output2 = []
    result2 = swapPairs(head2)
    output2 = []
    while result2:
        output2.append(result2.val)
        result2 = result2.next
    print(f"Example 2: Input: {expected_output2}, Output: {output2}, Result: {output2 == expected_output2}")

    # Example 3
    head3 = ListNode(1)
    expected_output3 = [1]
    result3 = swapPairs(head3)
    output3 = []
    while result3:
        output3.append(result3.val)
        result3 = result3.next
    print(f"Example 3: Input: {expected_output3}, Output: {output3}, Result: {output3 == expected_output3}")

test_swapPairs()