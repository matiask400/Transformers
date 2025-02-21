import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val})'

import heapq

def merge_k_lists(lists):
    min_heap = []

    for l in lists:
        if l:
            heapq.heappush(min_heap, (l.val, l))

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, node = heapq.heappop(min_heap)
        current.next = ListNode(val)
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, node.next))

    return dummy.next

# Helper functions to convert list to ListNode and vice-versa

def list_to_nodes(lst):
    pre_head = ListNode(-1)
    prev = pre_head
    for value in lst:
        prev.next = ListNode(value)
        prev = prev.next
    return pre_head.next

def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test(input_lists, expected_output):
    list_nodes = [list_to_nodes(l) for l in input_lists]
    merged_node = merge_k_lists(list_nodes)
    merged_list = nodes_to_list(merged_node)
    print(merged_list == expected_output)

# Example 1
test([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6])
# Example 2
test([], [])
# Example 3
test([[]], [])