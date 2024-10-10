from typing import List

class max_number_of_K_sum:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = n - 1
        left = 0
        count = 0
        nums.sort()

        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                count += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -=  1

        return count