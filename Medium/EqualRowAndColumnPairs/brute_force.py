from typing import List

class brute_force:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        for r in range(n):
            for c in range(n):
                flag = True
                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        flag = False
                        break

                if flag == True:
                    count += 1
        
        return count

# Time Complexity: O(n^3). There are a total of O(n^2) pairs when iterating over each row R and column C. Traversing each element in R and C takes O(n) time.
# Space Complexity: O(1)