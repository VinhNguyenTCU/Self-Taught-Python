from typing import List

class brute_force:
    def increasingTriplet(seft, nums: List[int]) -> bool:
        
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i < j and j < k and nums[i] < nums[j] and nums[j] < nums[k]:
                        return True
        
        return False