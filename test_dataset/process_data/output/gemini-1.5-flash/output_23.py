class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    
    # Use a min-heap to store the heads of the linked lists
    import heapq
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    
    dummy = ListNode(0)
    tail = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# Test cases

def test_mergeKLists(lists, expected_output):
    output = mergeKLists(lists)
    
    # Convert linked lists to lists for comparison
    output_list = []
    while output:
        output_list.append(output.val)
        output = output.next
    
    print(f"Input: {lists}")
    print(f"Output: {output_list}")
    print(f"Expected Output: {expected_output}")
    print(f"Result: {output_list == expected_output}")
    print("---")

# Example 1
lists1 = [[1,4,5],[1,3,4],[2,6]]
output1 = [1,1,2,3,4,4,5,6]
test_mergeKLists(lists1, output1)

# Example 2
lists2 = []
output2 = []
test_mergeKLists(lists2, output2)

# Example 3
lists3 = [[]]
output3 = []
test_mergeKLists(lists3, output3)