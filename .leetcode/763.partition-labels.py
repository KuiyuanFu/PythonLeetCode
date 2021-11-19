# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (78.29%)
# Likes:    5785
# Dislikes: 237
# Total Accepted:    303.5K
# Total Submissions: 387K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# You are given a string s. We want to partition the string into as many parts
# as possible so that each letter appears in at most one part.
#
# Return a list of integers representing the size of these parts.
#
#
# Example 1:
#
#
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits s into less parts.
#
#
# Example 2:
#
#
# Input: s = "eccbbbbdec"
# Output: [10]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.
#
#
#

# @lc tags=string;recursion

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将字符串分割，每种字符在同一段，求最大段数。
# 计算同字母区域，排序，找区间。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [i, i]
            else:

                d[c][1] = i
        intervals = list(d.values())
        intervals.sort()
        res = []
        idx = 0
        length = len(intervals)
        while idx < length:

            left, right = intervals[idx]
            idx += 1
            while idx < length and right > intervals[idx][0]:
                right = max(right, intervals[idx][1])
                idx += 1
            res.append(right - left + 1)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ababcbacadefegdehijhklij"')
    print('Exception :')
    print('[9,7,8]')
    print('Output :')
    print(str(Solution().partitionLabels("ababcbacadefegdehijhklij")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "eccbbbbdec"')
    print('Exception :')
    print('[10]')
    print('Output :')
    print(str(Solution().partitionLabels("eccbbbbdec")))
    print()

    pass
# @lc main=end