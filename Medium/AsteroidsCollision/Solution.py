from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)

            else:
                while stack and stack[-1] < abs(asteroid):
                    stack.pop()

                if len(stack) == 0:
                    res.append(asteroid)

                if stack[-1] == abs(asteroid):
                    stack.pop()

        for ans in stack:
            res.append(ans)

        return res

            
