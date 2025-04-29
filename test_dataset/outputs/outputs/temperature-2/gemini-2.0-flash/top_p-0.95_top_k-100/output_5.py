class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6

    Example 2:
    Input: lists = []
    Output: []

    Example 3:
    Input: lists = [[]]
    Output: []

    Constraints:
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.

    The sum of lists[i].length won't exceed 10^4.
    """
    import heapq

    heap = []
    for i, linked_list in enumerate(lists):
      if linked_list:
          heapq.heappush(heap, (linked_list.val, i, linked_list))

    dummy = ListNode(0)
    curr = dummy
    
    while heap:
      val, list_idx, node = heapq.heappop(heap)
      curr.next = node
      curr = curr.next

      if node.next:
        heapq.heappush(heap, (node.next.val, list_idx, node.next))

    return dummy.next
  
def list_to_linked_list(lst):
    dummyHead = ListNode(0)
    current = dummyHead
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummyHead.next

def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

def test_mergeKLists():
    test_cases = [
        ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
        ([], []),
        ([[]], [])
    ]

    correct_count = 0
    total_tests = len(test_cases)

    def lists_to_linked_lists(list_of_lists):
      linked_list_array = []
      for lst in list_of_lists:
        if lst:
          linked_list_array.append(list_to_linked_list(lst))
        else:
          linked_list_array.append(None)
      return linked_list_array
    
    for lists_input, expected_output in test_cases:
        lists_as_linked_lists = lists_to_linked_lists(lists_input)
        
        result_linked_list = mergeKLists(lists_as_linked_lists)

        if result_linked_list is None:
           result = []
        else:
           result = linked_list_to_list(result_linked_list)

        if result == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{total_tests}")

if __name__ == '__main__':
    test_mergeKLists()