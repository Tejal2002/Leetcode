# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        #note that here no head pointer is given 
        #so copy the value of next node to node to deleted 
        #then point it to next of next

        node.val = node.next.val
        node.next = node.next.next
