from typing import List

class merge_sorted_arrays1:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[0:m] #make the copy of nums1 start from index 0 to m
        left, right = 0, 0

        for i in range(m+n):
            if right >= n or (left < m and nums1_copy[left] <= nums2[right]):
                nums1[i] = nums1[left]
                left += 1
            elif left >= m or (right < n and nums1_copy[left] > nums2[right]):
                nums1[i] = nums2[right]
                right += 1