# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (28.51%)
# Likes:    1543
# Dislikes: 3849
# Total Accepted:    245.1K
# Total Submissions: 856.2K
# Testcase Example:  '123'
#
# Convert a non-negative integer num to its English words representation.
#
#
# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# Example 4:
# Input: num = 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
#
#
# Constraints:
#
#
# 0 <= num <= 2^31 - 1
#
#
#

# @lc tags=math;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个数字转换为英文。
# 递归。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split(
        )
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousand = 'Thousand Million Billion'.split()

        def word(num, idx=0):
            if num == 0:
                return []
            if num < 20:
                return [to19[num - 1]]
            if num < 100:
                return [tens[num // 10 - 2]] + word(num % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ['Hundred'] + word(num % 100)

            p, r = num // 1000, num % 1000
            space = [thousand[idx]] if p % 1000 != 0 else []
            return word(p, idx + 1) + space + word(r)

        return ' '.join(word(num)) or 'Zero'


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = 123')
    print('Exception :')
    print('"One Hundred Twenty Three"')
    print('Output :')
    print(str(Solution().numberToWords(123)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = 12345')
    print('Exception :')
    print('"Twelve Thousand Three Hundred Forty Five"')
    print('Output :')
    print(str(Solution().numberToWords(12345)))
    print()

    print('Example 3:')
    print('Input : ')
    print('num = 1234567')
    print('Exception :')
    print(
        '"One Million Two Hundred Thirty Four Thousand Five Hundred SixtySeven"'
    )
    print('Output :')
    print(str(Solution().numberToWords(1234567)))
    print()

    print('Example 4:')
    print('Input : ')
    print('num = 1234567891')
    print('Exception :')
    print(
        '"One Billion Two Hundred Thirty Four Million Five Hundred Sixty SevenThousand Eight Hundred Ninety One"'
    )
    print('Output :')
    print(str(Solution().numberToWords(1234567891)))
    print()

    pass
# @lc main=end