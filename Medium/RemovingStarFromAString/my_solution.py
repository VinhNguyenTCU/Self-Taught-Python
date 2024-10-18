class my_solution:
    def removeStars(self, s: str) -> str:
        
        stack1 = []
        stack2 = []

        for i in range(len(s) - 1, -1, -1):
            stack1.append(s[i])

        while stack1:
            c = stack1.pop()

            if c != '*':
                stack2.append(c)
            else:
                stack2.pop()
            
        return ''.join(stack2)