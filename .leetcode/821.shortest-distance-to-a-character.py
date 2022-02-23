# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc tags=union-find

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计距离。
# 反向
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        res = [len(s)] * len(s)
        l = len(s)
        for i in range(len(s)):
            l += 1
            if s[i] != c:
                res[i] = l
            else:
                l = 0
                for j in range(i + 1):
                    if res[i - j] <= j:
                        break
                    else:
                        res[i - j] = j
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "loveleetcode", c = "e"')
    print('Exception :')
    print('[3,2,1,0,1,0,0,1,2,2,1,0]')
    print('Output :')
    print(str(Solution().shortestToChar("loveleetcode", "e")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "aaab", c = "b"')
    print('Exception :')
    print('[3,2,1,0]')
    print('Output :')
    print(str(Solution().shortestToChar("aaab", "b")))
    print()

    pass
# @lc main=end