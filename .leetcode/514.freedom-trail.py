# @lc app=leetcode id=514 lang=python3
#
# [514] Freedom Trail
#
# https://leetcode.com/problems/freedom-trail/description/
#
# algorithms
# Hard (45.56%)
# Likes:    600
# Dislikes: 29
# Total Accepted:    24.5K
# Total Submissions: 53.7K
# Testcase Example:  '"godding"\n"gd"'
#
# In the video game Fallout 4, the quest "Road to Freedom" requires players to
# reach a metal dial called the "Freedom Trail Ring" and use the dial to spell
# a specific keyword to open the door.
#
# Given a string ring that represents the code engraved on the outer ring and
# another string key that represents the keyword that needs to be spelled,
# return the minimum number of steps to spell all the characters in the
# keyword.
#
# Initially, the first character of the ring is aligned at the "12:00"
# direction. You should spell all the characters in key one by one by rotating
# ring clockwise or anticlockwise to make each character of the string key
# aligned at the "12:00" direction and then by pressing the center button.
#
# At the stage of rotating the ring to spell the key character key[i]:
#
#
# You can rotate the ring clockwise or anticlockwise by one place, which counts
# as one step. The final purpose of the rotation is to align one of ring's
# characters at the "12:00" direction, where this character must equal
# key[i].
# If the character key[i] has been aligned at the "12:00" direction, press the
# center button to spell, which also counts as one step. After the pressing,
# you could begin to spell the next character in the key (next stage).
# Otherwise, you have finished all the spelling.
#
#
#
# Example 1:
#
#
# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
# For the first key character 'g', since it is already in place, we just need 1
# step to spell this character.
# For the second key character 'd', we need to rotate the ring "godding"
# anticlockwise by two steps to make it become "ddinggo".
# Also, we need 1 more step for spelling.
# So the final output is 4.
#
#
# Example 2:
#
#
# Input: ring = "godding", key = "godding"
# Output: 13
#
#
#
# Constraints:
#
#
# 1 <= ring.length, key.length <= 100
# ring and key consist of only lower case English letters.
# It is guaranteed that key could always be spelled by rotating ring.
#
#
#

# @lc tags=divide-and-conquer;dynamic-programming;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个圆环，上面有字母，问按次序读所有给定的字符需要多少次。
# 相邻的相同字符可以分为一组。需要访问这个字符时，只需要访问每组离上一个位置最近的端点即可。
# 分成间隔。
#
# @lc idea=end

# @lc group=depth-first-search

# @lc rank=10


# @lc code=start
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        orda = ord('a')
        ring = [ord(c) - orda for c in ring]
        key = [ord(c) - orda for c in key]
        lr = len(ring)
        lk = len(key)
        intervals = [[] for _ in range(26)]
        buffer = {}

        for i, r in enumerate(ring):
            b = intervals[r]
            if len(b) == 0 or b[-1][-1] != i - 1:
                b.append([i, i])
            else:
                b[-1][-1] = i

        def dist(s, d):

            if s > d:
                s, d = d, s
            return min(d - s, s + lr - d)

        def recur(idxR, idxK):
            if idxK == lk:
                return 0
            k = (idxR, idxK)
            if k in buffer:
                return buffer[k]
            res = 100000
            if ring[idxR] == key[idxK]:
                res = recur(idxR, idxK + 1)
            else:
                ls = intervals[key[idxK]]
                for l, r in ls:
                    if l == r:
                        d = dist(l, idxR)
                        res = min(res, d + recur(l, idxK + 1))
                    else:
                        ld = dist(l, idxR)
                        rd = dist(r, idxR)
                        if ld <= rd:
                            res = min(res, ld + recur(l, idxK + 1))
                        if ld >= rd:
                            res = min(res, rd + recur(r, idxK + 1))

            buffer[k] = res
            return res

        return recur(0, 0) + lk

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('ring = "godding", key = "gd"')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().findRotateSteps("godding", "gd")))
    print()

    print('Example 2:')
    print('Input : ')
    print('ring = "godding", key = "godding"')
    print('Exception :')
    print('13')
    print('Output :')
    print(str(Solution().findRotateSteps("godding", "godding")))
    print()
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().findRotateSteps("flrrf", "rrlff")))
    pass
# @lc main=end