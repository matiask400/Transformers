class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next

# Helper function to convert list to linked list

def build_linked_list(elements):
    head = ListNode(elements[0]) if elements else None
    current = head
    for el in elements[1:]:
        current.next = ListNode(el)
        current = current.next
    return head

# Helper function to convert linked list to list

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

inputs = [({'l1': [1, 2, 4], 'l2': [1, 3, 4]}, [1, 1, 2, 3, 4, 4]), 
          ({'l1': [], 'l2': []}, []), 
          ({'l1': [], 'l2': [0]}, [0])]

for i, (input_data, expected_output) in enumerate(inputs, start=1):
    l1 = build_linked_list(input_data['l1'])
    l2 = build_linked_list(input_data['l2'])
    merged_list = mergeTwoLists(l1, l2)
    output = linked_list_to_list(merged_list)
    print(f"Input {i}: {'True' if output == expected_output else 'False'}")
