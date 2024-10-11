from typing import List


class brute_force:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = maxCount = 0

        for i in range(len(nums)):
            count = 0
            k = 1

            for j in range(j, len(nums)):
                if nums[i] == 1:
                    count += 1
                elif nums[i] == 0 and k == 1:
                    count += 1
                    k -= 1
                elif nums[i] == 0 and k == 0:
                    break
            
            if count > maxCount:
                maxCount = count
            
        return maxCount
    
    # Time Complexity: O(N^2)
    # Space Complexity: O(1)
                    