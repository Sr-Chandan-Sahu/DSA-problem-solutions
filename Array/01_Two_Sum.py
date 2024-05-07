"""
Try it here :
https://leetcode.com/problems/two-sum/
"""
def twoSum(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    num_dict = {}  # Dictionary to store values and indices   
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_dict:
            return [num_dict[diff], i]           
        num_dict[num] = i
        
    return []


