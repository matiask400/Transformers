def mergeKLists(lists):
    if not lists:
        return []
    merged_list = []
    for linked_list in lists:
        while linked_list:
            merged_list.append(linked_list.val)
            linked_list = linked_list.next
    merged_list.sort()
    return merged_list

# Test the solution with example inputs
input1 = [[1,4,5],[1,3,4],[2,6]]
output1 = [1,1,2,3,4,4,5,6]
print(mergeKLists(input1) == output1)

input2 = []
output2 = []
print(mergeKLists(input2) == output2)

input3 = [[]]
output3 = []
print(mergeKLists(input3) == output3)