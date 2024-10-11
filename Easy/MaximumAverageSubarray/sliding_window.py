from typing import List

class sliding_window:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        #Assign n equals length of given list
        n = len(nums)

        #Initialize currSum and maxSum
        currSum = 0
        maxSum = 0

        #Traverse the given list until it reaches k - 1 element
        for i in range(k):
            currSum += nums[i]

        #currSum is now holding the total sum of first k elements, and we assign it to maxSum to compare later
        maxSum = currSum

        #Traverse the given list from k - 1 elements to the end
        for i in range(k, n):

            # Subtract the left element of the window and add the next right element of the window
            currSum = currSum - nums[i - k] + nums[i]

            # Compare the current sum with the max sum and update the max sum
            if currSum > maxSum:
                maxSum = currSum

        # Divide by K from the max sum will return the the largest average
        return maxSum / k 
