<<<<<<< HEAD
## Given an array of integers, return indices of the two numbers such that they add up to a specific target.
## 
## You may assume that each input would have exactly one solution, and you may not use the same element twice.
## 
## Example:
## 
## Given nums = [2, 7, 11, 15], target = 9,
## 
## Because nums[0] + nums[1] = 2 + 7 = 9,
## return [0, 1].

=======
>>>>>>> 0229a893e36caee8674fa2dba214e502d5a758fe
class Solution(object):
    def twoSum(self, nums, target):
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
<<<<<<< HEAD
                keys[nums[i]] = i     
=======
                keys[nums[i]] = i      
>>>>>>> 0229a893e36caee8674fa2dba214e502d5a758fe
