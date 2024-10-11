from typing import List

class sliding_window:
    def longestOnes(self, nums: List[int], k: int) -> int: 

        left, right = 0, 0
        maxCount = 0
        numsZero = 0

        while right < len(nums):
            if nums[right] == 0:
                numsZero += 1
            
            while numsZero > k:
                if nums[left] == 0:
                    numsZero -= 1
                left += 1

            if right - left + 1 > maxCount:
                maxCount = right - left + 1
            
            right += 1
        return maxCount
    
    # Time Complexity: O(N). Since both pointers only move forward, each of the left and right pointers traverse a maximum of n steps.
    # Space Complexity: O(1). Because we don't store anything other than variables