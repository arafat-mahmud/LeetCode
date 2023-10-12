class Solution:
   def twoSum(self, nums, target):
       seen = {}
       for i, value in enumerate(nums):
           remain = target - nums[i]
           if remain in seen:
               return [i, seen[remain]]
           seen[value] = i

