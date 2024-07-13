def swapPairs(head):
      dummy = ListNode()
      dummy.next = head
      prev = dummy
      
      while head and head.next:
            nextPair = head.next.next
            second = head.next
            second.next = head
            head.next = nextPair
            prev.next = second
            prev = head
            head = nextPair
      return dummy.next