# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

        :type head: ListNode
        :rtype: bool

        Solution- make a cursor that goes through the list and add a number bigger than the constraint.
        If there's ever a point where the value is bigger than the constraint, then you know you've been there before!

        """
        cur = head
        while cur:
            if cur.val <= 10**5:
                cur.val = cur.val + 10**11
            else: 
                return True
            cur = cur.next
        
        return False