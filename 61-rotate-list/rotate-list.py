# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head :
            return head 
        
        #size of k if it is greater than length of LL
        length, tail = 1, head

        while tail.next:
            tail = tail.next
            length += 1 

        k = k % length
        if k==0:
            return head

        #Move the pivot and then rotate 
        curr = head 
        for i in range(length - k - 1):
            curr = curr.next
        
        newhead = curr.next
        curr.next = None
        tail.next = head

        return newhead
