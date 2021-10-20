# @lc app=leetcode id=691 lang=python3
#
# [691] Stickers to Spell Word
#
# https://leetcode.com/problems/stickers-to-spell-word/description/
#
# algorithms
# Hard (46.12%)
# Likes:    615
# Dislikes: 59
# Total Accepted:    26.1K
# Total Submissions: 56.3K
# Testcase Example:  '["with","example","science"]\n"thehat"'
#
# We are given n different types of stickers. Each sticker has a lowercase
# English word on it.
#
# You would like to spell out the given string target by cutting individual
# letters from your collection of stickers and rearranging them. You can use
# each sticker more than once if you want, and you have infinite quantities of
# each sticker.
#
# Return the minimum number of stickers that you need to spell out target. If
# the task is impossible, return -1.
#
# Note: In all test cases, all words were chosen randomly from the 1000 most
# common US English words, and target was chosen as a concatenation of two
# random words.
#
#
# Example 1:
#
#
# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the
# target "thehat".
# Also, this is the minimum number of stickers necessary to form the target
# string.
#
#
# Example 2:
#
#
# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# Explanation:
# We cannot form the target "basicbasic" from cutting letters from the given
# stickers.
#
#
#
# Constraints:
#
#
# n == stickers.length
# 1 <= n <= 50
# 1 <= stickers[i].length <= 10
# 1 <= target <= 15
# stickers[i] and target consist of lowercase English letters.
#
#
#

# @lc tags=dynamic-programming;backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列字符串，切断拼接成指定字符串。求最少使用的字符串数。
# 动态规划。递归备忘录。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # statistics the char of target
        maps = {}
        countT = []
        for c in target:
            if c not in maps:
                maps[c] = len(maps)
                countT.append(1)
            else:
                countT[maps[c]] += 1
        length = len(countT)
        ls = list(range(length))
        # statistics the char of stickers
        counts = []
        for sticker in stickers:
            d = [0] * length
            for c in sticker:
                if c in maps:
                    d[maps[c]] += 1
            counts.append(d)
        # dp
        buffer = {}

        def minus(cs1, cs2):
            return tuple(max(0, cs1[i] - cs2[i]) for i in ls)

        def belowerOrEqualZero(cs):
            for i in cs:
                if i > 0:
                    return False
            return True

        def recur(cs: List[int]):
            k = cs
            if k in buffer:
                return buffer[k]
            res = 0

            if not belowerOrEqualZero(cs):
                res = 16
                for ct in counts:
                    csn = minus(cs, ct)
                    if csn == cs:
                        continue
                    r = recur(csn)
                    r = r if r >= 0 else 16
                    res = min(res, r)
                res += 1
            if res == 17:
                res = -1
            buffer[k] = res
            return res

        return recur(tuple(countT))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('stickers = ["with","example","science"], target = "thehat"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minStickers(["with", "example", "science"],
                                     "thehat")))
    print()

    print('Example 2:')
    print('Input : ')
    print('stickers = ["notice","possible"], target = "basicbasic"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().minStickers(["notice", "possible"], "basicbasic")))
    print()

    pass
# @lc main=end