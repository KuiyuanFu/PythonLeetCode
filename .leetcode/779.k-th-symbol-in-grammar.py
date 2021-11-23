# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#
# https://leetcode.com/problems/k-th-symbol-in-grammar/description/
#
# algorithms
# Medium (39.28%)
# Likes:    1301
# Dislikes: 225
# Total Accepted:    70K
# Total Submissions: 177.5K
# Testcase Example:  '1\n1'
#
# We build a table of n rows (1-indexed). We start by writing 0 in the 1^st
# row. Now in every subsequent row, we look at the previous row and replace
# each occurrence of 0 with 01, and each occurrence of 1 with 10.
#
#
# For example, for n = 3, the 1^st row is 0, the 2^nd row is 01, and the 3^rd
# row is 0110.
#
#
# Given two integer n and k, return the k^th (1-indexed) symbol in the n^th row
# of a table of n rows.
#
#
# Example 1:
#
#
# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0
#
#
# Example 2:
#
#
# Input: n = 2, k = 1
# Output: 0
# Explanation:
# row 1: 0
# row 2: 01
#
#
# Example 3:
#
#
# Input: n = 2, k = 2
# Output: 1
# Explanation:
# row 1: 0
# row 2: 01
#
#
# Example 4:
#
#
# Input: n = 3, k = 1
# Output: 0
# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110
#
#
#
# Constraints:
#
#
# 1 <= n <= 30
# 1 <= k <= 2^n - 1
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 0 to 01 , 1 to 10，求第n行的第k个，直接二进制。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return '0'
        k -= 1
        s = '0'
        d = ['01', '10']
        ord0 = ord('0')
        for c in bin(k)[2:].zfill(n - 1):
            s = d[ord(s) - ord0][ord(c) - ord0]
        return s
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1, k = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().kthGrammar(1, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2, k = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().kthGrammar(2, 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 2, k = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().kthGrammar(2, 2)))
    print()

    print('Example 4:')
    print('Input : ')
    print('n = 3, k = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().kthGrammar(3, 1)))
    print()
    print('Example 4:')
    print('Input : ')
    print('n = 3, k = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().kthGrammar(3, 1)))
    print(str(Solution().kthGrammar(3, 1)))
    print(str(Solution().kthGrammar(3, 2)))
    print(str(Solution().kthGrammar(3, 3)))
    print(str(Solution().kthGrammar(3, 4)))
    print()
    print(str(Solution().kthGrammar(4, 1)))
    print(str(Solution().kthGrammar(4, 2)))
    print(str(Solution().kthGrammar(4, 3)))
    print(str(Solution().kthGrammar(4, 4)))
    print(str(Solution().kthGrammar(4, 5)))
    print(str(Solution().kthGrammar(4, 6)))
    print(str(Solution().kthGrammar(4, 7)))
    print(str(Solution().kthGrammar(4, 8)))

    pass
# @lc main=end