# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/
#
# algorithms
# Hard (48.58%)
# Likes:    851
# Dislikes: 26
# Total Accepted:    29.6K
# Total Submissions: 60.8K
# Testcase Example:  '3\n3\n5'
#
# Nearly everyone has used the Multiplication Table. The multiplication table
# of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
#
# Given three integers m, n, and k, return the k^th smallest element in the m x
# n multiplication table.
#
#
# Example 1:
#
#
# Input: m = 3, n = 3, k = 5
# Output: 3
# Explanation: The 5^th smallest number is 3.
#
#
# Example 2:
#
#
# Input: m = 2, n = 3, k = 6
# Output: 6
# Explanation: The 6^th smallest number is 6.
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 3 * 10^4
# 1 <= k <= m * n
#
#
#

# @lc tags=binary-search

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 求乘法表的第k小值。
# 将每一左下到右上的斜线，作为一列，在这一列上经过变换，满足单调递增。
# 之后二分搜索可能值。超时了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findKthNumber(self, row: int, col: int, k: int) -> int:

        if col < row:
            row, col = col, row

        def idx(i, j, value):
            l, r = -1, min(row - i + 1, min(j, row)) - 1

            l1 = max(0, j - row)

            while l < r:
                middle = (l + r + 1) // 2
                o = min(middle, l1)
                o += max(0, (middle - l1) // 2)
                middleValue = (i + o) * (j - o)

                if middleValue >= value:
                    r = middle - 1
                else:
                    l = middle

            return l + 1

        l, r = 1, row * col
        while l < r:
            middle = (l + r + 1) // 2
            s = 0
            for j in range(1, col + 1):
                s += idx(1, j, middle)
            for i in range(2, row + 1):
                s += idx(i, col, middle)
            if s < k:
                l = middle
            else:
                r = middle - 1
        return l


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().findKthNumber(5, 5, 25)))
    print('Example 1:')
    print('Input : ')
    print('m = 3, n = 3, k = 5')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findKthNumber(3, 3, 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('m = 2, n = 3, k = 6')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().findKthNumber(2, 3, 6)))
    print()
    print(str(Solution().findKthNumber(5, 5, 1)))
    print(str(Solution().findKthNumber(5, 5, 2)))
    print(str(Solution().findKthNumber(5, 5, 3)))
    print(str(Solution().findKthNumber(5, 5, 4)))
    print(str(Solution().findKthNumber(5, 5, 5)))
    print(str(Solution().findKthNumber(5, 5, 6)))
    print(str(Solution().findKthNumber(5, 5, 7)))
    print(str(Solution().findKthNumber(5, 5, 8)))
    print(str(Solution().findKthNumber(5, 5, 9)))
    print(str(Solution().findKthNumber(5, 5, 10)))
    print(str(Solution().findKthNumber(5, 5, 21)))
    print(str(Solution().findKthNumber(5, 5, 22)))
    print(str(Solution().findKthNumber(5, 5, 23)))
    print(str(Solution().findKthNumber(5, 5, 24)))
    print(str(Solution().findKthNumber(5, 5, 25)))
    print(str(Solution().findKthNumber(5, 6, 1)))
    print(str(Solution().findKthNumber(5, 6, 2)))
    print(str(Solution().findKthNumber(5, 6, 3)))
    print(str(Solution().findKthNumber(5, 6, 4)))
    print(str(Solution().findKthNumber(5, 6, 5)))
    print(str(Solution().findKthNumber(5, 6, 6)))
    print(str(Solution().findKthNumber(5, 6, 7)))
    print(str(Solution().findKthNumber(5, 6, 8)))
    print(str(Solution().findKthNumber(5, 6, 9)))
    print(str(Solution().findKthNumber(5, 6, 10)))
    print(str(Solution().findKthNumber(5, 6, 21)))
    print(str(Solution().findKthNumber(5, 6, 22)))
    print(str(Solution().findKthNumber(5, 6, 23)))
    print(str(Solution().findKthNumber(5, 6, 24)))
    print(str(Solution().findKthNumber(5, 6, 25)))
    print(str(Solution().findKthNumber(5, 6, 26)))
    print(str(Solution().findKthNumber(5, 6, 27)))
    print(str(Solution().findKthNumber(5, 6, 28)))
    print(str(Solution().findKthNumber(5, 6, 29)))
    print(str(Solution().findKthNumber(5, 6, 30)))
    print(str(Solution().findKthNumber(14095, 1517, 8568032)))
    pass
# @lc main=end