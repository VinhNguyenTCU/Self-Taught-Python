from typing import List

class brute_force:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        "Find the largest candies, take O(n) time complexity"
        max_candy = max(candies) 

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)

        return res