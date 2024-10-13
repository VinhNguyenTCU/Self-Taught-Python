from typing import List

class built_inFuction:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]
    
    """ nums1 = set(nums1)
        nums2 = set(nums2)

        list1 = nums1.difference(nums2) --> nums1.difference(nums2) == set(nums1) - set(nums2)
        list2 = nums2.difference(nums1) --> nums2.difference(nums1) == set(nums2) - set(nums1)

        return [list1, list2]"""