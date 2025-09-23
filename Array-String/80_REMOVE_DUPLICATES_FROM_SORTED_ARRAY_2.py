class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1

        del nums[i:]
        return len(nums)


nums = [1,1,1,2,2,3]
result = []
[result.append(num) for num in nums if result.count(num) <2]
print(result)