from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while True:
            min_val = float('inf')
            min_node = None
            for node in lists:
                if node and node.val < min_val:
                    min_val = node.val
                    min_node = node
            if min_node:
                curr.next = min_node
                curr = curr.next
                min_node = min_node.next
            else:
                break
        return dummy.next


if __name__ == "__main__":
    input1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
    output1 = [1, 1, 2, 3, 4, 4, 5, 6]
    res1 = Solution().mergeKLists(input1)
    print('Correct:', res1 == output1)

    input2 = []
    output2 = []
    res2 = Solution().mergeKLists(input2)
    print('Correct:', res2 == output2)

    input3 = [[]]
    output3 = []
    res3 = Solution().mergeKLists(input3)
    print('Correct:', res3 == output3)