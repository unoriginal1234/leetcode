# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        cur = head

        big_head = ListNode()
        big_tail = big_head
        small_head = ListNode()
        small_tail = small_head
            
        cur = head
        

        while cur:
            if cur.val < x:
                small_tail.next = cur
                small_tail = small_tail.next
            else:
                big_tail.next = cur
                big_tail = big_tail.next
            cur = cur.next
        
        big_tail.next=None
        small_tail.next = big_head.next
        return small_head.next
