l1 = [1,2,4]
l2 = [1,3,4]
print(mergeTwoLists(l1, l2) == [1,1,2,3,4,4])  # True

l1 = []
l2 = []
print(mergeTwoLists(l1, l2) == [])  # True

l1 = []
l2 = [0]
print(mergeTwoLists(l1, l2) == [0])  # True


def mergeTwoLists(list1, list2):
    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2