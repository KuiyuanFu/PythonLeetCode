# @lc app=leetcode id=768 lang=python3
#
# [768] Max Chunks To Make Sorted II
#
# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/
#
# algorithms
# Hard (50.69%)
# Likes:    884
# Dislikes: 27
# Total Accepted:    34.5K
# Total Submissions: 67.2K
# Testcase Example:  '[5,4,3,2,1]'
#
# You are given an integer array arr.
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
# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3],
# which isn't sorted.
#
#
# Example 2:
#
#
# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks
# possible.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 2000
# 0 <= arr[i] <= 10^8
#
#
#

# @lc tags=two-pointers;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将给定数组分段，每一段排序后合并，等于原始数组排序结果，求最多分成几段。
# 每一段的最大值要小于等于右侧的最小值。
# 保存每一位右侧的最小值，如果左侧最大值小于等于最小值，就新产生一段。
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
    print('arr = [5,4,3,2,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maxChunksToSorted([5, 4, 3, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [2,1,3,4,4]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().maxChunksToSorted([2, 1, 3, 4, 4])))
    print()

    pass
# @lc main=end