from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = defaultdict(int)
    
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in sums:
                return [sums[complement], i]
            
            sums[num] = i
        