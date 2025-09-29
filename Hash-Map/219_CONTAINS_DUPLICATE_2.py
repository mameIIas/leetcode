class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict

        container = defaultdict(int)

        for i, num in enumerate(nums):
            if num in container:
                previous_index = container[num]
                distance = i - previous_index
                
                if distance <= k:
                    return True 
            
            container[num] = i  
        
        return False