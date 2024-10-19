class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)

c = Solution() 
string = "leet**cod*e"
print(c.removeStars(string))

# Time Complexity: O(N) for loop and O(1) for the action do with the stack. --> O(N)
# Space Complexity: O(N) the worst case is no asterisk