class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of k sorted linked lists.

    Returns:
        The merged sorted linked list.
    """
    import heapq

    heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

def list_to_linked_list(lst):
    """
    Converts a list to a linked list.

    Args:
        lst: The list to convert.

    Returns:
        The linked list.
    """
    dummy_head = ListNode(0)
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def linked_list_to_list(head):
    """
    Converts a linked list to a list.

    Args:
        head: The head of the linked list.

    Returns:
        The list.
    """
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

def test_merge_k_lists():
    """
    Tests the merge_k_lists function.
    """
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[1, 5], [2, 4], [3, 6]], [1, 2, 3, 4, 5, 6])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for lists_of_lists, expected_output in test_cases:
        linked_lists = [list_to_linked_list(lst) for lst in lists_of_lists]
        result_list = linked_list_to_list(merge_k_lists(linked_lists))

        if result_list == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_merge_k_lists()