from typing import List

class merge_sorted_arrays:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1 = sorted(nums1)