# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/
#
# algorithms
# Medium (56.60%)
# Likes:    1492
# Dislikes: 164
# Total Accepted:    61K
# Total Submissions: 107K
# Testcase Example:  '[4,3,2,1,0]'
#
# You are given an integer array arr of length n that represents a permutation
# of the integers in the range [0, n - 1].
#
# We split arr into some number of chunks (i.e., partitions), and individually
# sort each chunk. After concatenating them, the result should equal the sorted
# array.
#
# Return the largest number of chunks we can make to sort the array.
#
#
# Example 1:
#
#
# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2],
# which isn't sorted.
#
#
# Example 2:
#
#
# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks
# possible.
#
#
#
# Constraints:
#
#
# n == arr.length
# 1 <= n <= 10
# 0 <= arr[i] < n
# All the elements of arr are unique.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 同上。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        dp = [100000000] * (len(arr) + 1)
        for i in reversed(range(len(arr))):
            dp[i] = min(dp[i + 1], arr[i])
        res = 0
        m = 0
        for i in range(len(arr)):
            if m <= dp[i]:
                res += 1
            m = max(m, arr[i])
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [4,3,2,1,0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maxChunksToSorted([4, 3, 2, 1, 0])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [1,0,2,3,4]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().maxChunksToSorted([1, 0, 2, 3, 4])))
    print()

    pass
# @lc main=end