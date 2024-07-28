class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        #using hashset
        # seen = set()

        # for i in range(0,len(numbers)):
        #     if target - numbers[i] in seen:
        #         return [numbers.index(target - numbers[i])+1,i+1]
        #     else:
        #         seen.add(numbers[i])

        #using two pointer 

        l,r  = 0, len(numbers)-1

        while l<r :
            curr_sum = numbers[l] + numbers[r]

            if curr_sum < target :
                l += 1
            elif curr_sum > target :
                r -= 1
            else:
                return [l+1, r+1]
            
            




        

        