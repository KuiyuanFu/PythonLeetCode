# @lc app=leetcode id=842 lang=python3
#
# [842] Split Array into Fibonacci Sequence
#
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/
#
# algorithms
# Medium (37.68%)
# Likes:    809
# Dislikes: 246
# Total Accepted:    29.9K
# Total Submissions: 79.5K
# Testcase Example:  '"1101111"'
#
# You are given a string of digits num, such as "123456579". We can split it
# into a Fibonacci-like sequence [123, 456, 579].
#
# Formally, a Fibonacci-like sequence is a list f of non-negative integers such
# that:
#
#
# 0 <= f[i] < 2^31, (that is, each integer fits in a 32-bit signed integer
# type),
# f.length >= 3, and
# f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
#
#
# Note that when splitting the string into pieces, each piece must not have
# extra leading zeroes, except if the piece is the number 0 itself.
#
# Return any Fibonacci-like sequence split from num, or return [] if it cannot
# be done.
#
#
# Example 1:
#
#
# Input: num = "1101111"
# Output: [11,0,11,11]
# Explanation: The output [110, 1, 111] would also be accepted.
#
#
# Example 2:
#
#
# Input: num = "112358130"
# Output: []
# Explanation: The task is impossible.
#
#
# Example 3:
#
#
# Input: num = "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not
# valid.
#
#
#
# Constraints:
#
#
# 1 <= num.length <= 200
# num contains only digits.
#
#
#

# @lc tags=Unknown

# @lc imports=start
import numbers
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将数字分割成类似斐波那契数列的格式。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        length = len(num)

        sMax = str(1 << 31)

        def getLengthMaxI() -> int:
            if num[0] == '0':
                return 1
            l = min(len(sMax), length // 2)
            if l < len(sMax):
                return l
            if num[l] < sMax:
                return l
            else:
                return l - 1

        def getLengthMaxJ(idx: int) -> int:
            if num[idx] == '0':
                return min(idx + 1, length - 1)
            l = min(len(sMax), length - 1 - idx)
            if l < len(sMax):
                return idx + l
            if num[idx:idx + l] < sMax:
                return idx + l
            else:
                return idx + l - 1

        def generateRes(nl: int, nr: int, l: int):
            res = [nl, nr]
            while l < length:
                nl, nr = nr, nl + nr
                res.append(nr)
                l += len(str(nr))
            return res

        def getNext(nl, nr, idx):
            nNext = nl + nr
            nNextString = str(nNext)
            if len(nNextString) > len(sMax) or (len(nNextString) == len(sMax)
                                                and nNextString > sMax):
                return 0, 0, length + 1
            # corret
            if num[idx:idx + len(nNextString)] == nNextString:
                return nr, nNext, idx + len(nNextString)
            else:
                return 0, 0, length + 1

        lim = getLengthMaxI()
        for li in range(1, lim + 1):
            ljm = getLengthMaxJ(li)
            ni = int(num[:li])
            for lj in range(li + 1, ljm + 1):
                nj = int(num[li:lj])
                nl, nr, idx = ni, nj, lj
                while idx <= length:
                    # end
                    if idx == length:
                        return generateRes(ni, nj, lj)
                    nl, nr, idx = getNext(nl, nr, idx)

        return []
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = "1101111"')
    print('Exception :')
    print('[11,0,11,11]')
    print('Output :')
    print(str(Solution().splitIntoFibonacci("1101111")))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = "112358130"')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().splitIntoFibonacci("112358130")))
    print()

    print('Example 3:')
    print('Input : ')
    print('num = "0123"')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().splitIntoFibonacci("0123")))
    print()
    print(str(Solution().splitIntoFibonacci("112358130")))
    print(
        str(Solution().splitIntoFibonacci(
            "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
        )))
    print(
        str(Solution().splitIntoFibonacci(
            "502113822114324228146342470570616913086148370223967883880490627727810157768164350462659281443027860696206741126485341822692082949177424771869507721046921249291642202139633432706879765292084310"
        )))
    pass
# @lc main=end