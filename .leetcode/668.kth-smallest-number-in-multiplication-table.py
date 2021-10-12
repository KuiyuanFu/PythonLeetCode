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
# 直接优先队列。超时了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findKthNumber(self, rows: int, cols: int, k: int) -> int:

        if cols < rows:
            rows, cols = cols, rows
        h = []
        for j in range(1, cols + 1):
            heappush(h, (j, (1, j), True))
        for i in range(2, rows + 1):
            heappush(h, (i * cols, (i, cols), True))
        for _ in range(k - 1):
            _, (i, j), f = heappop(h)
            if f and i <= rows and j <= rows and j > i:
                heappush(h, (i * j, (i, j), False))
            else:
                i += 1
                j -= 1
                if i <= rows and j >= 1 and j >= i:
                    heappush(h, (i * j, (i, j), True))
        return h[0][0]


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
    # 2840762
    print(str(Solution().findKthNumber(14095, 1517, 8568032)))
    # 31666344
    print(str(Solution().findKthNumber(9895, 28405, 100787757)))
    pass
# @lc main=end