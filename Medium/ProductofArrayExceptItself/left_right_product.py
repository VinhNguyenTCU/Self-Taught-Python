from typing import List

class left_right_product:
    def productExceptItself(self, nums: List[int]) -> List[int]:

        length = len(nums)
        left_product_list = [0] * length
        right_product_list = [0] * length
        ans = [0] * length

        "No element to the left of index 0, so we have to assign left-most value equals 1"
        left_product_list[0] = 1
        for i in range(1, length):
            left_product_list[i] = left_product_list[i - 1] * nums[i - 1]

        "No element to the right of index 0, so we have to assign right-most value equals 1"
        right_product_list[length - 1] = 1
        for i in range(length - 2, -1, -1):
            right_product_list[i] = right_product_list[i + 1] * nums[i + 1]

        "Multiply both of the left and right product list and put each value to the answer list"
        for i in range(length):
            ans[i] = left_product_list[i] * right_product_list[i]

        return ans