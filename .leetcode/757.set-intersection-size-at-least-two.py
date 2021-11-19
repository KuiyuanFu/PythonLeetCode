# @lc app=leetcode id=757 lang=python3
#
# [757] Set Intersection Size At Least Two
#
# https://leetcode.com/problems/set-intersection-size-at-least-two/description/
#
# algorithms
# Hard (42.80%)
# Likes:    405
# Dislikes: 52
# Total Accepted:    14.3K
# Total Submissions: 33.4K
# Testcase Example:  '[[1,3],[1,4],[2,5],[3,5]]'
#
# An integer interval [a, b] (for integers a < b) is a set of all consecutive
# integers from a to b, including a and b.
#
# Find the minimum size of a set S such that for every integer interval A in
# intervals, the intersection of S with A has a size of at least two.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
# Output: 3
# Explanation: Consider the set S = {2, 3, 4}.  For each interval, there are at
# least 2 elements from S in the interval.
# Also, there isn't a smaller size set that fulfills the above condition.
# Thus, we output the size of this set, which is 3.
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
# Output: 5
# Explanation: An example of a minimum sized set is {1, 2, 3, 4, 5}.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 3000
# intervals[i].length == 2
# 0 <= ai < bi <= 10^8
#
#
#

# @lc tags=bit-manipulation;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定间隔，求一个最小的集合，满足集合与每个间隔重叠大小至少为2.
# 贪心。
# 排序后，去掉可以被包含的间隔，之后贪心放置位置。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        intervalsNotFullOverlap = []
        for i in range(len(intervals)):
            # the new interval include in the last interval
            # so the new interval can represent the last interval.
            while intervalsNotFullOverlap and intervalsNotFullOverlap[-1][
                    0] <= intervals[i][0] and intervals[i][
                        1] <= intervalsNotFullOverlap[-1][1]:
                intervalsNotFullOverlap.pop()
            intervalsNotFullOverlap.append(intervals[i])
        length = len(intervalsNotFullOverlap)
        counts = [2] * length
        res = 0
        idx = 0

        while idx != length:
            res += 1
            fp = intervalsNotFullOverlap[idx][1]
            # need two value
            if counts[idx] == 2:
                fp -= 1
            idxT = idx
            while idxT < length and intervalsNotFullOverlap[idxT][0] <= fp:
                counts[idxT] -= 1
                idxT += 1
            while idx < length and counts[idx] == 0:
                idx += 1

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('intervals = [[1,3],[1,4],[2,5],[3,5]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3,
                                                                       5]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('intervals = [[1,2],[2,3],[2,4],[4,5]]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4,
                                                                       5]])))
    print()
    print('Example 2:')
    print('Input : ')
    print('intervals = [[1,3],[3,7],[5,7],[7,8]]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().intersectionSizeTwo([[1, 3], [3, 7], [5, 7], [7,
                                                                       8]])))
    print()
    pass
# @lc main=end