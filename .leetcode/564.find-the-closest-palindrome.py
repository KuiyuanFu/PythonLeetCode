# @lc app=leetcode id=564 lang=python3
#
# [564] Find the Closest Palindrome
#
# https://leetcode.com/problems/find-the-closest-palindrome/description/
#
# algorithms
# Hard (20.74%)
# Likes:    407
# Dislikes: 1040
# Total Accepted:    28.2K
# Total Submissions: 135.7K
# Testcase Example:  '"123"'
#
# Given a string n representing an integer, return the closest integer (not
# including itself), which is a palindrome. If there is a tie, return the
# smaller one.
#
# The closest is defined as the absolute difference minimized between two
# integers.
#
#
# Example 1:
#
#
# Input: n = "123"
# Output: "121"
#
#
# Example 2:
#
#
# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest
# which is 0.
#
#
#
# Constraints:
#
#
# 1 <= n.length <= 18
# n consists of only digits.
# n does not have leading zeros.
# n is representing an integer in the range [1, 10^18 - 1].
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找绝对值最近的回文数字。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return chr(ord(n) - 1)

        ord0 = ord('0')

        def diff(n1: str, n2: str):
            length = max(len(n1), len(n2))
            n1, n2 = n1.zfill(length), n2.zfill(length)
            f = n1 >= n2
            if not f:
                n1, n2 = n2, n1
            c = [None] * length
            r = 0
            for i in reversed(range(length)):
                n = ord(n1[i]) - ord(n2[i]) + r

                r = -1 if n < 0 else 0
                n += 10 if n < 0 else 0
                c[i] = chr(n + ord0)
            return f, ''.join(c)

        candidates = []

        m = (len(n) - 1) // 2
        sn = [c for c in n]
        sn[-1:-m - 2:-1] = sn[:m + 1]
        candidates.append(''.join(sn))
        candidates.append('1' + '0' * (len(sn) - 1) + '1')
        candidates.append('9' * (len(sn) - 1))

        l, r = (m, m) if len(n) % 2 == 1 else (m, m + 1)
        bigger = sn
        smaller = sn.copy()
        while l >= 0:
            c = sn[l]
            if c < '9':
                bigger[l] = chr(ord(bigger[l]) + 1)
                bigger[r] = bigger[l]
                candidates.append(''.join(bigger))
            if c > '0':
                smaller[l] = chr(ord(smaller[l]) - 1)
                smaller[r] = smaller[l]
                candidates.append(''.join(smaller))
            bigger[l] = bigger[r] = '0'
            smaller[l] = smaller[r] = '9'
            l -= 1
            r += 1

        res = '9' * (len(sn) + 1)
        dif = res
        for w in candidates:
            w = w.strip('0')
            f, di = diff(w, n)
            if diff(dif, di)[0] and (not diff(di, dif)[0]
                                     or diff(res, w)[0]) and w != n:
                res = w
                dif = di

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().nearestPalindromic("11911")))
    print(str(Solution().nearestPalindromic("1805170081")))
    print('Example 1:')
    print('Input : ')
    print('n = "123"')
    print('Exception :')
    print('"121"')
    print('Output :')
    print(str(Solution().nearestPalindromic("123")))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = "1"')
    print('Exception :')
    print('"0"')
    print('Output :')
    print(str(Solution().nearestPalindromic("1")))
    print()
    print(str(Solution().nearestPalindromic("99")))
    print(str(Solution().nearestPalindromic("999")))
    print(str(Solution().nearestPalindromic("10001")))
    print(str(Solution().nearestPalindromic("10000")))
    print(str(Solution().nearestPalindromic("10011")))
    print(str(Solution().nearestPalindromic("10101")))
    pass
# @lc main=end