from typing import List

class brute_force:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = []
        n = len(nums)
        left = 0
        right = n - 1

        while right + k < n:
            left = right
            total = 0
            right_bound = right + k

            while left < right_bound:
                total += nums[left]
                left += 1

            average = total / k
            ans.append(average)
            right += 1

        return max(ans)
        