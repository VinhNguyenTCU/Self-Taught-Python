import sys
from typing import List

class linear_scan:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = sys.maxsize
        
        for num in nums:
            if first >= num:
                first = num
            elif second >= num:
                second = num
            else:
                return True

        return False