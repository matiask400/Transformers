import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __repr__(self):
        return str(self.val)


def mergeKLists(lists):
    min_heap = []
    for l in lists:
        if l:
            heapq.heappush(min_heap, l)

    dummy = ListNode()
    current = dummy

    while min_heap:
        smallest_node = heapq.heappop(min_heap)
        current.next = smallest_node
        current = current.next
        if smallest_node.next:
            heapq.heappush(min_heap, smallest_node.next)

    return dummy.next


def list_to_nodes(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Example 1
lists1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
list_nodes1 = [list_to_nodes(l) for l in lists1]
output1 = nodes_to_list(mergeKLists(list_nodes1))
print(output1 == [1, 1, 2, 3, 4, 4, 5, 6])

# Example 2
lists2 = []
list_nodes2 = [list_to_nodes(l) for l in lists2]
output2 = nodes_to_list(mergeKLists(list_nodes2))
print(output2 == [])

# Example 3
lists3 = [[]]
list_nodes3 = [list_to_nodes(l) for l in lists3]
output3 = nodes_to_list(mergeKLists(list_nodes3))
print(output3 == [])