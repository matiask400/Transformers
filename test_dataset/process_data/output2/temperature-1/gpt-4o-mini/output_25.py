class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        current = head
        while current and count < k:
            current = current.next
            count += 1
        if count < k:
            return head

        prev = None
        current = head
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head.next = self.reverseKGroup(current, k)
        return prev

# Example inputs for testing the implementation
inputs = [([1, 2, 3, 4, 5], 2),
          ([1, 2, 3, 4, 5], 3),
          ([1, 2, 3, 4, 5], 1)]
outputs = [[2, 1, 4, 3, 5], [3, 2, 1, 4, 5], [1, 2, 3, 4, 5]]

for i, (input_data, k) in enumerate(inputs):
    # Create linked list from input data
    head = ListNode(input_data[0])
    current = head
    for value in input_data[1:]:
        current.next = ListNode(value)
        current = current.next
    
    # Apply the solution
    solution = Solution()
    reversed_head = solution.reverseKGroup(head, k)
    
    # Convert linked list back to list for comparison
    output = []
    while reversed_head:
        output.append(reversed_head.val)
        reversed_head = reversed_head.next
    
    # Check if the output matches the expected output
    print(output == outputs[i])