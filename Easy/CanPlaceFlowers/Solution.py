from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
            
            if flowerbed[i] == 0:
                available_left = (i == 0) or (flowerbed[i - 1] == 0)
                available_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if available_left and available_right:
                    flowerbed[i] = 1
                    count += 1
                
        return count >= n