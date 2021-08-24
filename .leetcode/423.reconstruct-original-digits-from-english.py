# @lc app=leetcode id=423 lang=python3
#
# [423] Reconstruct Original Digits from English
#
# https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
#
# algorithms
# Medium (51.23%)
# Likes:    377
# Dislikes: 1105
# Total Accepted:    43.9K
# Total Submissions: 85.7K
# Testcase Example:  '"owoztneoer"'
#
# Given a string s containing an out-of-order English representation of digits
# 0-9, return the digits in ascending order.
#
#
# Example 1:
# Input: s = "owoztneoer"
# Output: "012"
# Example 2:
# Input: s = "fviefuro"
# Output: "45"
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is one of the characters
# ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
# s is guaranteed to be valid.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定乱序数字的英文表示，求数字，以正序给出。
# 根据每个数字的特殊字符来确定个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def originalDigits(self, s: str) -> str:
        d = defaultdict(int)
        b = [
            ['6', 'x', 'six'],
            ['0', 'z', 'zero'],
            ['2', 'w', 'two'],
            ['4', 'u', 'four'],
            ['1', 'o', 'one'],
            ['8', 'g', 'eight'],
            ['3', 'h', 'three'],
            ['5', 'f', 'five'],
            ['7', 's', 'seven'],
            ['9', 'e', 'nine'],
        ]
        for c in s:
            d[c] += 1
        r = defaultdict(int)
        for i, f, s in b:
            count = d[f]
            for c in s:
                d[c] -= count
            r[i] = count
        res = []
        for c in '0123456789':
            res.append(c * r[c])

        return ''.join(res)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "owoztneoer"')
    print('Exception :')
    print('"012"')
    print('Output :')
    print(str(Solution().originalDigits("owoztneoer")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "fviefuro"')
    print('Exception :')
    print('"45"')
    print('Output :')
    print(str(Solution().originalDigits("fviefuro")))
    print()
    print(
        str(Solution().originalDigits(
            "zeroonetwothreefourfivesixseveneightnine")))
    pass
# @lc main=end