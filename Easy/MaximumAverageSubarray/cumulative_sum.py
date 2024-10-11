from typing import List

class cumulative_sum:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum_arr = []
        total = 0

        """nums = [1,12,-5,-6,50,3], k = 4
            --> sum = [1, 13, 8, 2, 52, 55]"""

        for i in range(n):
            total += nums[i]
            sum_arr.append(total)

        "k - 1 because k is length so k - 1 is the index of the number at k"
        res = sum_arr[k - 1] / k 

        for i in range(k, n):
            res = max(res, (nums[i] - nums[i - k]) / k)
        
        return res
        