# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#
# https://leetcode.com/problems/positions-of-large-groups/description/
#
# algorithms
# Easy (51.29%)
# Likes:    601
# Dislikes: 111
# Total Accepted:    68.7K
# Total Submissions: 134K
# Testcase Example:  '"abbxxxxzzy"'
#
# In a string s of lowercase letters, these letters form consecutive groups of
# the same character.
#
# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx",
# "z", and "yy".
#
# A group is identified by an interval [start, end], where start and end denote
# the start and end indices (inclusive) of the group. In the above example,
# "xxxx" has the interval [3,6].
#
# A group is considered large if it has 3 or more characters.
#
# Return the intervals of every large group sorted in increasing order by start
# index.
#
#
# Example 1:
#
#
# Input: s = "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the only large group with start index 3 and end index
# 6.
#
#
# Example 2:
#
#
# Input: s = "abc"
# Output: []
# Explanation: We have groups "a", "b", and "c", none of which are large
# groups.
#
#
# Example 3:
#
#
# Input: s = "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# Explanation: The large groups are "ddd", "eeee", and "bbb".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s contains lowercase English letters only.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计连续字符索引。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        res = []
        l = 0
        n = len(s)
        while l < n:
            r = l + 1
            while r < n and s[r] == s[l]:
                r += 1
            if r - l >= 3:
                res.append([l, r - 1])
            l = r
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abbxxxxzzy"')
    print('Exception :')
    print('[[3,6]]')
    print('Output :')
    print(str(Solution().largeGroupPositions("abbxxxxzzy")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "abc"')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().largeGroupPositions("abc")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "abcdddeeeeaabbbcd"')
    print('Exception :')
    print('[[3,5],[6,9],[12,14]]')
    print('Output :')
    print(str(Solution().largeGroupPositions("abcdddeeeeaabbbcd")))
    print()

    pass
# @lc main=end