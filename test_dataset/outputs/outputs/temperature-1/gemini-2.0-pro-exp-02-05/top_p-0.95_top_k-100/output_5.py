import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of k sorted linked lists.

    Returns:
        The merged sorted linked list.
    """
    if not lists:
        return None

    heap = []
    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, head))  # Push (value, node)

    dummy = ListNode(0)
    current = dummy

    while heap:
        val, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))

    return dummy.next

def list_to_linked_list(lst):
    dummy_head = ListNode(0)
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

def run_tests():
      test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
          ([[1],[0]],[0,1])
    ]

      correct_count = 0
      total_tests = len(test_cases)

      for lists_input, expected_output in test_cases:
        linked_lists = [list_to_linked_list(lst) for lst in lists_input]
        merged_list = mergeKLists(linked_lists)
        result_list = linked_list_to_list(merged_list)
        if result_list == expected_output:
            print("True")
            correct_count += 1
        else:
          print("False")

      print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    run_tests()