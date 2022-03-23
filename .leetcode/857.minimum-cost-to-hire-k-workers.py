# @lc app=leetcode id=857 lang=python3
#
# [857] Minimum Cost to Hire K Workers
#
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/
#
# algorithms
# Hard (51.56%)
# Likes:    1576
# Dislikes: 188
# Total Accepted:    49.1K
# Total Submissions: 95.3K
# Testcase Example:  '[10,20,5]\n[70,50,30]\n2'
#
# There are n workers. You are given two integer arrays quality and wage where
# quality[i] is the quality of the i^th worker and wage[i] is the minimum wage
# expectation for the i^th worker.
#
# We want to hire exactly k workers to form a paid group. To hire a group of k
# workers, we must pay them according to the following rules:
#
#
# Every worker in the paid group should be paid in the ratio of their quality
# compared to other workers in the paid group.
# Every worker in the paid group must be paid at least their minimum wage
# expectation.
#
#
# Given the integer k, return the least amount of money needed to form a paid
# group satisfying the above conditions. Answers within 10^-5 of the actual
# answer will be accepted.
#
#
# Example 1:
#
#
# Input: quality = [10,20,5], wage = [70,50,30], k = 2
# Output: 105.00000
# Explanation: We pay 70 to 0^th worker and 35 to 2^nd worker.
#
#
# Example 2:
#
#
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
# Output: 30.66667
# Explanation: We pay 4 to 0^th worker, 13.33333 to 2^nd and 3^rd workers
# separately.
#
#
#
# Constraints:
#
#
# n == quality.length == wage.length
# 1 <= k <= n <= 10^4
# 1 <= quality[i], wage[i] <= 10^4
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 雇佣工人，共n人，雇佣k人，每一个人有质量和期望薪资，实际薪资必须满足期满薪资，且薪资与质量的比值都相同。
# 比值最大的起决定作用，之后挑小于其的，质量最差的。
# 按照比值排序，之后的元素都满足比例要求，以此元素作为比例基准，滑动窗口找之后最小质量的和。
#
# @lc idea=end

# @lc group=array

# @lc rank=10

# @lc code=start

from collections import *


class Solution:
    def initWage(self, ):
        self.length = len(self.wage)
        self.rqw = sorted([(w / q, q, w)
                           for q, w in zip(self.quality, self.wage)],
                          reverse=True)
        self.quality.sort()
        self.qualityIdx = self.k - 1
        self.qualityMin = 0
        self.qualityDict = defaultdict(int)
        self.invalid = defaultdict(int)
        for i in range(self.qualityIdx):
            quality = self.quality[i]
            self.qualityMin += quality
            self.qualityDict[quality] += 1

    def getMinQuality(self, q):
        # used
        if self.qualityDict[q] > 0:
            return self.qualityMin + self.quality[self.qualityIdx]
        # not used
        else:
            return self.qualityMin + q

    def removeQuality(self, q):
        # used
        if self.qualityDict[q] > 0:
            self.qualityDict[q] -= 1
            self.qualityMin = self.qualityMin - q + self.quality[
                self.qualityIdx]
            self.qualityDict[self.quality[self.qualityIdx]] += 1
            self.qualityIdx += 1
        # not used
        else:
            self.invalid[q] += 1

        while self.qualityIdx < self.length and self.invalid[self.quality[
                self.qualityIdx]] > 0:
            self.invalid[self.quality[self.qualityIdx]] -= 1
            self.qualityIdx += 1

    def traverse(self):
        res = 1000000000000
        for i in range(self.length - self.k + 1):
            r, q, w = self.rqw[i]
            qualityMin = self.getMinQuality(q)
            cost = qualityMin * r
            res = min(res, cost)
            self.removeQuality(q)
        return res

    def mincostToHireWorkers(self, quality: List[int], wage: List[int],
                             k: int) -> float:

        self.quality = quality
        self.wage = wage
        self.k = k
        self.initWage()
        return self.traverse()
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('quality = [10,20,5], wage = [70,50,30], k = 2')
    print('Exception :')
    print('105.00000')
    print('Output :')
    print(str(Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3')
    print('Exception :')
    print('30.66667')
    print('Output :')
    print(
        str(Solution().mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7],
                                            3)))
    print()

    pass
# @lc main=end