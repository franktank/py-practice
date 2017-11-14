"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
"""
# Partially correct answer
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        # Calculate prefix sum
        prefix = list(A)
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] + prefix[i]

        max_sum = prefix[0]
        for i in range(len(A)):
            for j in range(i + 1):
                if A[j] - prefix[j] + prefix[i] > max_sum:
                    max_sum = A[j] - prefix[j] + prefix[i]

        return max_sum
