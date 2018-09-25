# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        location = ListNode(0)
        result = location
        sum=0
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 or l2:
            if l1:
                sum += l1.val
                l1=l1.next
            if l2:
                sum += l2.val
                l2=l2.next
            location.next = ListNode(sum%10)
            location = location.next
            sum = int(sum //10)
        return result.next
