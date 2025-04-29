def mergeTwoLists(l1, l2):
	if not l1 or not l2:
		return l1 if not l2 else l2
	if l1.val < l2.val:
		ret = l1
		ret.next = mergeTwoLists(l1.next, l2)
	else:
		ret = l2
		ret.next = mergeTwoLists(l1, l2.next)
	return ret