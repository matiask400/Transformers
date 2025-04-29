import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked-lists into one sorted linked-list.

    Args:
        lists: A list of sorted linked-lists.

    Returns:
        The merged sorted linked-list.
    """
    # Use a min-heap to store the nodes of all the linked lists
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))  # (value, list_index, node)

    # Create a dummy head for the merged linked list
    dummy = ListNode()
    tail = dummy

    # Iterate until the heap is empty
    while heap:
        # Get the node with the smallest value from the heap
        val, list_index, node = heapq.heappop(heap)

        # Add the node to the merged linked list
        tail.next = node
        tail = node

        # Add the next node from the same list to the heap if it exists
        if node.next:
            heapq.heappush(heap, (node.next.val, list_index, node.next))
    
    # set the next to None in order to handle case [[]] properly.
    tail.next = None
    return dummy.next


def list_to_linked_list(lst: list) -> ListNode:
    """
    Converts a list to a linked list.

    Args:
        lst: The list to convert.

    Returns:
        The head of the linked list.
    """
    head = None
    tail = None
    for val in lst:
        new_node = ListNode(val)
        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def linked_list_to_list(head: ListNode) -> list:
    """
    Converts a linked list to a list.

    Args:
        head: The head of the linked list.

    Returns:
        The list representation of the linked list.
    """
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst


def test_merge_k_sorted_lists():
    """
    Tests the merge_k_sorted_lists function.
    """
    tests = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[], [1]], [1]),
        ([[1], [2]], [1, 2]),
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,4,5,6,7,8,9]),
        ([[5]],[5])


    ]

    correct_count = 0
    for i, (lists_input, expected_output) in enumerate(tests):
        lists = []
        for lst in lists_input:
            lists.append(list_to_linked_list(lst))

        result_linked_list = merge_k_sorted_lists(lists)
        result_list = linked_list_to_list(result_linked_list)

        if result_list == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Test {i+1} Failed. Expected: {expected_output}, Got: {result_list}")

    print(f"{correct_count}/{len(tests)}")

test_merge_k_sorted_lists()