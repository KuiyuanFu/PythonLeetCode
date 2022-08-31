# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#
# https://leetcode.com/problems/delete-columns-to-make-sorted/description/
#
# algorithms
# Easy (69.76%)
# Likes:    392
# Dislikes: 2064
# Total Accepted:    70.7K
# Total Submissions: 101.3K
# Testcase Example:  '["cba","daf","ghi"]'
#
# You are given an array of n strings strs, all of the same length.
#
# The strings can be arranged such that there is one on each line, making a
# grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:
#
#
# abc
# bce
# cae
#
#
# You want to delete the columns that are not sorted lexicographically. In the
# above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e')
# are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column
# 1.
#
# Return the number of columns that you will delete.
#
#
# Example 1:
#
#
# Input: strs = ["cba","daf","ghi"]
# Output: 1
# Explanation: The grid looks as follows:
# ⁠ cba
# ⁠ daf
# ⁠ ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1
# column.
#
#
# Example 2:
#
#
# Input: strs = ["a","b"]
# Output: 0
# Explanation: The grid looks as follows:
# ⁠ a
# ⁠ b
# Column 0 is the only column and is sorted, so you will not delete any
# columns.
#
#
# Example 3:
#
#
# Input: strs = ["zyx","wvu","tsr"]
# Output: 3
# Explanation: The grid looks as follows:
# ⁠ zyx
# ⁠ wvu
# ⁠ tsr
# All 3 columns are not sorted, so you will delete all 3.
#
#
#
# Constraints:
#
#
# n == strs.length
# 1 <= n <= 100
# 1 <= strs[i].length <= 1000
# strs[i] consists of lowercase English letters.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字符串数组，每行一个字符串，按照列组成新字符串，判断有多少个不是字典序。
# 直接比较
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:

        return Counter(
            Counter(strs[j][i] <= strs[j + 1][i]
                    for j in range(len(strs) - 1))[True] == len(strs) - 1
            for i in range(len(strs[0])))[False]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["cba","daf","ghi"]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minDeletionSize(["cba", "daf", "ghi"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('strs = ["a","b"]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minDeletionSize(["a", "b"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('strs = ["zyx","wvu","tsr"]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minDeletionSize(["zyx", "wvu", "tsr"])))
    print()

    pass
# @lc main=end