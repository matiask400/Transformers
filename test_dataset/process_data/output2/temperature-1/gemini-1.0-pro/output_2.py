    def addTwoNumbers(l1, l2):
      dummy = curr = ListNode(0)
      carry = 0

      while l1 or l2 or carry:
          val1 = l1.val if l1 else 0
          val2 = l2.val if l2 else 0
          total = val1 + val2 + carry
          carry = total // 10
          curr.next = ListNode(total % 10)

          curr = curr.next
          l1 = l1.next if l1 else None
          l2 = l2.next if l2 else None

      return dummy.next

    # Example 1: Input - l1 = [2,4,3], l2 = [5,6,4]
    result1 = addTwoNumbers([2,4,3], [5,6,4])
    print(result1 == [7,0,8])

    # Example 2: Input - l1 = [0], l2 = [0]
    result2 = addTwoNumbers([0], [0])
    print(result2 == [0])

    # Example 3: Input - l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    result3 = addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])