# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

    # using arrays but space = O(n)

        # nums = []

        # while head:
        #     nums.append(head.val)
        #     head = head.next
        
        # l,r = 0 , len(nums) - 1

        # while l <= r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True
    
    # By using slow - fast pointer and reversing the second half

        # Get the middle 
        slow , fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half
        prev = None
        curr = slow 
        while curr:
            tmp = curr.next
            curr.next = prev 
            prev = curr
            curr = tmp
        
        # check palindrome
        left , right = head , prev 

        while right:
            if left.val != right.val:
                return False 
            left = left.next
            right = right.next
        return True

        