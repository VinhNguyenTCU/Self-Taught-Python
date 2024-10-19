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