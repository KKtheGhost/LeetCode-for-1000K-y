## Given an array of non-negative integers, you are initially positioned at the first index of the array.
## 
## Each element in the array represents your maximum jump length at that position.
## 
## Your goal is to reach the last index in the minimum number of jumps.
## 
## Example:
## 
## Input: [2,3,1,1,4]
## Output: 2
## Explanation: The minimum number of jumps to reach the last index is 2.
##     Jump 1 step from index 0 to 1, then 3 steps to the last index.
## Note:
## 
## You can assume that you can always reach the last index.

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = lastIdx = nextIdx = 0
        while nextIdx < len(A) - 1:
            ans += 1
            lastIdx, nextIdx = nextIdx, max(i + A[i] for i in xrange(lastIdx, nextIdx + 1))
        return ans