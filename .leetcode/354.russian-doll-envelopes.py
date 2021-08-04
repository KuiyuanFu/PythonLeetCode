# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (38.56%)
# Likes:    2348
# Dislikes: 62
# Total Accepted:    113.5K
# Total Submissions: 293.9K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
# represents the width and the height of an envelope.
#
# One envelope can fit into another if and only if both the width and height of
# one envelope are greater than the other envelope's width and height.
#
# Return the maximum number of envelopes you can Russian doll (i.e., put one
# inside the other).
#
# Note: You cannot rotate an envelope.
#
#
# Example 1:
#
#
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
#
#
# Example 2:
#
#
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= envelopes.length <= 5000
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^4
#
#
#

# @lc tags=binary-search;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 2D的俄罗斯套娃，给定信封的宽高，都大于，才能套进去。
# 求最大的套娃个数。
# DP，对于每个信封，只有宽高都小于其的才能套进去，那么就在二维平面上形成一个区域，每个点的值，等于其左上角区域元素最大值加一。
# 使用最长递增序列来确定，对信封数组进行排序，按照先宽递增，再高递减的次序。
# 使用dp数组保存套娃个数为索引加一时的最小高度。
# 对信封进行迭代，每运算一个信封时，使用高度减一为值对dp数组进行二分搜索，得到的索引值，就是满足高宽限制的最大套娃值，因为是宽度相同时，按照高递减排序的，所以不用担心使用了同样宽度的信封，同宽度更高的索引一定大于等于得到的索引值。
#
# @lc idea=end

# @lc group=binary-search;dynamic-programming;longest-increasing-subsequence

# @lc rank=10


# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        from bisect import bisect
        envelopes.sort(key=lambda enve: enve[0] * 2 * 10000 - enve[1])
        dp = []

        for w, h in envelopes:
            i = bisect(dp, h - 1)
            if i == len(dp):
                dp.append(h)
            elif h < dp[i]:
                dp[i] = h
        return len(dp)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Exception : 5')
    print(
        str(Solution().maxEnvelopes([[2, 100], [3, 200], [4, 300], [5, 500],
                                     [5, 400], [5, 250], [6, 370], [6, 360],
                                     [7, 380]])))
    print('Exception : 4')
    print(
        str(Solution().maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]])))
    print('Exception : 7')
    print(
        str(Solution().maxEnvelopes([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6],
                                     [5, 5], [6, 7], [7, 8]])))

    print('Example 1:')
    print('Input : ')
    print('envelopes = [[5,4],[6,4],[6,7],[2,3]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('envelopes = [[1,1],[1,1],[1,1]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maxEnvelopes([[1, 1], [1, 1], [1, 1]])))
    print()

    pass
# @lc main=end