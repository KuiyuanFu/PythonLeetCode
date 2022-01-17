# @lc app=leetcode id=816 lang=python3
#
# [816] Ambiguous Coordinates
#

# @lc tags=hash-table;design

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 从去掉','与'.'的二维坐标中恢复原始坐标。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def ambiguousCoordinates(self, s: str) -> List[str]:
        res = []
        s = s[1:len(s) - 1]

        def generateSegments(s: str):

            if len(s) == 1:
                return [s]
            if s[0] == '0' and s[-1] == '0':
                return []
            if s[0] == '0':
                return [s[0] + '.' + s[1:]]
            segments = [s]
            if s[-1] != '0':
                for m in range(1, len(s)):
                    segments.append(s[:m] + '.' + s[m:])
            return segments

        for m in range(1, len(s)):
            ls, rs = s[:m], s[m:]
            lsegments, rsegments = generateSegments(ls), generateSegments(rs)
            for l, r in product(lsegments, rsegments):
                res.append('(' + l + ', ' + r + ')')

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "(123)"')
    print('Exception :')
    print('["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]')
    print('Output :')
    print(str(Solution().ambiguousCoordinates("(123)")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "(0123)"')
    print('Exception :')
    print(
        '["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12,3)"]'
    )
    print('Output :')
    print(str(Solution().ambiguousCoordinates("(0123)")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "(00011)"')
    print('Exception :')
    print('["(0, 0.011)","(0.001, 1)"]')
    print('Output :')
    print(str(Solution().ambiguousCoordinates("(00011)")))
    print()

    pass
# @lc main=end