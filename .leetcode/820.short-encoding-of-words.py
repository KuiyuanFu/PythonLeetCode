# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc tags=depth-first-search;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 编码，给定一组字符串，编码到一个参考字符串中，对于每一个字符串，都有索引值，满足此字符串等于在参考字符串对应位置至下一个‘#’间的字符串。
# 直接字典树。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:

        s = set()

        words.sort(key=len, reverse=True)

        l = 0
        for w in words:
            if w not in s:
                for i in range(len(w)):
                    s.add(w[i:])
                l += len(w) + 1
        return l
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["time", "me", "bell"]')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().minimumLengthEncoding(["time", "me", "bell"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["t"]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minimumLengthEncoding(["t"])))
    print()

    pass
# @lc main=end