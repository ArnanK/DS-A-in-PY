#inplace array manipulation
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        

        a=[]

        for i in range(len(nums)):
            if nums[i] > 0:
                a.append(i+1)

        return a
    
#using set
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = set(range(1,len(nums) + 1))
        b = set(nums)
        return a-b