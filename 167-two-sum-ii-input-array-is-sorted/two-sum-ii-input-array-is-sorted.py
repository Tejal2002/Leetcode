class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = set()

        for i in range(0,len(numbers)):
            if target - numbers[i] in seen:
                return [numbers.index(target - numbers[i])+1,i+1]
            else:
                seen.add(numbers[i])

        

        