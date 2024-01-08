nums = [9,6,4,2,3,5,7,0,1]

def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] is None: return i
        if i != nums[i]: return i
    