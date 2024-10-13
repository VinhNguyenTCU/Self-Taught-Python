from typing import List

class brute_force:
    def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # nums1 = [1,2,3], nums2 = [2,4,6]
        # [[1,3],[4,6]]
        ans = []
        set1 = set()
        set2 = set()

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                continue
            set1.add(nums1[i])
        
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                continue
            set2.add(nums2[i])
        
        ans.append(set1)
        ans.append(set2)

        return ans
