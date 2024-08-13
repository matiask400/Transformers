class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseLinkedList(start, end):
            prev = None
            curr = start
            while curr != end:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            # Reverse the group
            prev = reverseLinkedList(group_prev.next, group_next)
            # Connect with the previous part
            temp = group_prev.next
            group_prev.next = prev
            temp.next = group_next
            group_prev = temp

    # Example inputs
    def list_to_linkedlist(lst):
        dummy = ListNode(0)
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def linkedlist_to_list(head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst

    # Test cases
    inputs = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 1)
    ]
    outputs = [
        [2, 1, 4, 3, 5],
        [3, 2, 1, 4, 5],
        [1, 2, 3, 4, 5]
    ]

    sol = Solution()
    for (input_data, expected_output) in zip(inputs, outputs):
        head = list_to_linkedlist(input_data[0])
        k = input_data[1]
        result = sol.reverseKGroup(head, k)
        print(linkedlist_to_list(result) == expected_output)