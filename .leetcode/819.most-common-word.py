# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc tags=dynamic-programming

# @lc imports=start
from time import time
from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计字符
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        symbols = "!?',;. "
        times = defaultdict(int)
        l, r = 0, 0
        while l < len(paragraph):
            if r == len(paragraph) or paragraph[r] in symbols:
                s = paragraph[l:r].strip().lower()
                if len(s) > 0:
                    times[s] += 1
                r += 1
                l = r
            else:
                r += 1
        t, s = 0, 0
        for p in times.items():
            k, v = p
            if v > t and k not in banned:
                t, s = v, k
        return s
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",banned = ["hit"]'
    )
    print('Exception :')
    print('"ball"')
    print('Output :')
    print(
        str(Solution().mostCommonWord(
            "Bob hit a ball, the hit BALL flew far after it was hit.",
            ["hit"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('paragraph = "a.", banned = []')
    print('Exception :')
    print('"a"')
    print('Output :')
    print(str(Solution().mostCommonWord("a.", [])))
    print()
    print('Input : ')
    print('paragraph ="Bob. hIt, baLl", banned = ["bob", "hit"]')
    print('Exception :')
    print('"ball"')
    print('Output :')
    print(str(Solution().mostCommonWord("Bob. hIt, baLl", ["bob", "hit"])))
    print()

    pass
# @lc main=end