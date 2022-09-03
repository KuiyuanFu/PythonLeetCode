# @lc app=leetcode id=955 lang=python3
#
# [955] Delete Columns to Make Sorted II
#
# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/
#
# algorithms
# Medium (34.52%)
# Likes:    504
# Dislikes: 75
# Total Accepted:    16.4K
# Total Submissions: 47.5K
# Testcase Example:  '["ca","bb","ac"]'
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
# the final array has its elements in lexicographic order (i.e., strs[0] <=
# strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value
# of answer.length.
#
#
# Example 1:
#
#
# Input: strs = ["ca","bb","ac"]
# Output: 1
# Explanation:
# After deleting the first column, strs = ["a", "b", "c"].
# Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
# We require at least 1 deletion since initially strs was not in lexicographic
# order, so the answer is 1.
#
#
# Example 2:
#
#
# Input: strs = ["xc","yb","za"]
# Output: 0
# Explanation:
# strs is already in lexicographic order, so we do not need to delete anything.
# Note that the rows of strs are not necessarily in lexicographic order:
# i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)
#
#
# Example 3:
#
#
# Input: strs = ["zyx","wvu","tsr"]
# Output: 3
# Explanation: We have to delete every column.
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

# @lc tags=tree

# @lc imports=start
from operator import ne
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定等长字符串数组，可以选定一组索引，所有字符串对应位置的字符都会被删除，要使剩下的字符串数组是字典序，最少需要删除多少个位置。
# 首先建立每个比较的字符串对，按照字符索引遍历，如果这个索引上有一个字符串对不符合字典序，那么就需要删掉这个索引。
# 如果保留了索引，那么所有已经确认符合字典序的字符串对可以删掉了。即明确小于，而不是等于。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        length = len(strs[0])

        res = 0
        pairs = set(pairwise(strs))

        for idx in range(length):
            removePairs = []
            needRemove = False
            for p in pairs:
                s1, s2 = p
                c1, c2 = s1[idx], s2[idx]
                if c1 < c2:
                    removePairs.append(p)
                elif c1 > c2:
                    needRemove = True
                    break
            if needRemove:
                res += 1
            else:
                for p in removePairs:
                    pairs.remove(p)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["ca","bb","ac"]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minDeletionSize(["ca", "bb", "ac"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('strs = ["xc","yb","za"]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minDeletionSize(["xc", "yb", "za"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('strs = ["zyx","wvu","tsr"]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minDeletionSize(["zyx", "wvu", "tsr"])))

    print()
    print('Example 3:')
    print('Input : ')
    print('strs = ["jwkwdc","etukoz"]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minDeletionSize(["jwkwdc", "etukoz"])))
    print()

    pass
# @lc main=end