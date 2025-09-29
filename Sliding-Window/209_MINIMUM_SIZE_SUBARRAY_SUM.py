class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            if nums[right]== target:
                return 1
            current_sum = current_sum + nums[right]
            while current_sum>=target:
                min_length=min(min_length,right-left+1)
                current_sum-= nums[left]
                left+=1

        return min_length if min_length != float('inf') else 0