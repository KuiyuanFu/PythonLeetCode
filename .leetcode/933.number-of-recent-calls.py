# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#
# https://leetcode.com/problems/number-of-recent-calls/description/
#
# algorithms
# Easy (73.12%)
# Likes:    764
# Dislikes: 2471
# Total Accepted:    123.9K
# Total Submissions: 169.5K
# Testcase Example:  '["RecentCounter","ping","ping","ping","ping"]\n[[],[1],[100],[3001],[3002]]'
#
# You have a RecentCounter class which counts the number of recent requests
# within a certain time frame.
#
# Implement the RecentCounter class:
#
#
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in
# milliseconds, and returns the number of requests that has happened in the
# past 3000 milliseconds (including the new request). Specifically, return the
# number of requests that have happened in the inclusive range [t - 3000, t].
#
#
# It is guaranteed that every call to ping uses a strictly larger value of t
# than the previous call.
#
#
# Example 1:
#
#
# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]
#
# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100],
# return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001],
# return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is
# [2,3002], return 3
#
#
#
# Constraints:
#
#
# 1 <= t <= 10^9
# Each test case will call ping with strictly increasing values of t.
# At most 10^4 calls will be made to ping.
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 记录最近访问次数。
# 直接记录
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class RecentCounter:

    def __init__(self):
        self.times = []
        self.idx = 0

    def ping(self, t: int) -> int:
        self.times.append(t)
        s = t - 3000
        while self.times[self.idx] < s:
            self.idx += 1
        return len(self.times) - self.idx


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = RecentCounter()
    print(o.ping(1))
    print(o.ping(100))
    print(o.ping(3001))
    print(o.ping(3002))

    pass
# @lc main=end