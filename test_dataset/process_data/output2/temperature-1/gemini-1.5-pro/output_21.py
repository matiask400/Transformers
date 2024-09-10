class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

def list_to_linked_list(lst):
    dummy = ListNode(0)
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

# Test Cases
input_1 = ([1,2,4], [1,3,4])
output_1 = [1,1,2,3,4,4]

input_2 = ([], [])
output_2 = []

input_3 = ([], [0])
output_3 = [0]

# Verify the solution
print(linked_list_to_list(merge_two_lists(list_to_linked_list(input_1[0]), list_to_linked_list(input_1[1]))) == output_1)
print(linked_list_to_list(merge_two_lists(list_to_linked_list(input_2[0]), list_to_linked_list(input_2[1]))) == output_2)
print(linked_list_to_list(merge_two_lists(list_to_linked_list(input_3[0]), list_to_linked_list(input_3[1]))) == output_3)