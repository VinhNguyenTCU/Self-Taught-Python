from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentAltitude = maxAltitude = 0
        
        for i in range(len(gain)):
            currentAltitude += gain[i]
            maxAltitude = max(currentAltitude, maxAltitude)

        return maxAltitude
