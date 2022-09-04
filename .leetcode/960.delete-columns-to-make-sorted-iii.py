# @lc app=leetcode id=960 lang=python3
#
# [960] Delete Columns to Make Sorted III
#
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/
#
# algorithms
# Hard (57.09%)
# Likes:    466
# Dislikes: 11
# Total Accepted:    11.1K
# Total Submissions: 19.5K
# Testcase Example:  '["babca","bbazb"]'
#
# You are given an array of n strings strs, all of the same length.
#
# We may choose any deletion indices, and we delete all the characters in those
# indices for each string.
#
# For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0,
# 2, 3}, then the final array after deletions is ["bef", "vyz"].
#
# Suppose we chose a set of deletion indices answer such that after deletions,
# the final array has every string (row) in lexicographic order. (i.e.,
# (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and
# (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]), and so on).
# Return the minimum possible value of answer.length.
#
#
# Example 1:
#
#
# Input: strs = ["babca","bbazb"]
# Output: 3
# Explanation: After deleting columns 0, 1, and 4, the final array is strs =
# ["bc", "az"].
# Both these rows are individually in lexicographic order (ie. strs[0][0] <=
# strs[0][1] and strs[1][0] <= strs[1][1]).
# Note that strs[0] > strs[1] - the array strs is not necessarily in
# lexicographic order.
#
# Example 2:
#
#
# Input: strs = ["edcba"]
# Output: 4
# Explanation: If we delete less than 4 columns, the only row will not be
# lexicographically sorted.
#
#
# Example 3:
#
#
# Input: strs = ["ghi","def","abc"]
# Output: 0
# Explanation: All rows are already lexicographically sorted.
#
#
#
# Constraints:
#
#
# n == strs.length
# 1 <= n <= 100
# 1 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
#
#
#
#
#
#

# @lc tags=depth-first-search;union-find

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字符串数组，可以选定一组索引，删掉每个字符串对应索引元素，使最后每个字符串成为字典序。
# 动态规划，记录以保留此索引时，前面删除最少索引的个数。
# 和比较有关的，都需要记录有关的信息，舍弃无关信息。
# 此位索引保留的话，就与之前的字符无关了。
#
# @lc idea=end

# @lc group=

# @lc rank=10


# @lc code=start
class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        strs.sort(reverse=True)
        strsCounts = len(strs)
        idicesLength = len(strs[0])

        dp = [0]

        for i in range(1, idicesLength):
            deleteCount = i
            for j in range(i):
                f = True
                for k in range(strsCounts):
                    s = strs[k]
                    if s[j] > s[i]:
                        f = False
                        break
                if f:
                    deleteCount = min(deleteCount, dp[j] + (i - j - 1))
            dp.append(deleteCount)
        res = min(n + (idicesLength - i - 1) for i, n in enumerate(dp))
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["babca","bbazb"]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minDeletionSize(["babca", "bbazb"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('strs = ["edcba"]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().minDeletionSize(["edcba"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('strs = ["ghi","def","abc"]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minDeletionSize(["ghi", "def", "abc"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('strs = ["abbba"]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minDeletionSize(["abbba"])))
    print()

    pass
# @lc main=end