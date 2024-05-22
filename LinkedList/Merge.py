class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode()
        move = ans
        while list1 and list2:
            if list1.val < list2.val:
                move.next = list1
                list1 = list1.next
            else:
                move.next = list2
                list2 = list2.next
            move = move.next
        if list1:
            move.next = list1
        else:
            move.next = list2
        return ans.next
        