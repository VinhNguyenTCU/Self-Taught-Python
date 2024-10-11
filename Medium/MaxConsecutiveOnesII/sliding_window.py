from typing import List

class sliding_window:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:  
        left, right = 0, 0
        numsZero = 0
        maxLength = 0

        while right < len(nums): # While our window is in bound
            if nums[right] == 0: # Increase numsZero if the rightmost element is 0
                numsZero += 1
            
            while numsZero == 2: # While numsZero is equal 2
                if nums[left] == 0: #Contract our window
                    numsZero -= 1
                left += 1

            currentLength = right - left + 1 # The length of current consecutive ones
            if currentLength > maxLength:
                maxLength = currentLength
        
        return maxLength
    
    # Time Complexity: O(N). Since both pointers only move forward, each of the left and right pointers traverse a maximum of n steps.
    # Space Complexity: O(1). Because we don't store anything other than variables