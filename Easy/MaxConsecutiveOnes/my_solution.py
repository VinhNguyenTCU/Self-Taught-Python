from typing import List

class my_solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = maxCount = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else: 
                count = 0

            if count > maxCount:
                maxCount = count
        
        return maxCount
    
    #Time Complexity: O(N)
    #Space Complexity: O(1)