class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
     def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = None
        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        return node