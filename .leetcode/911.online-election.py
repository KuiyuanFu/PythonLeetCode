# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#
# https://leetcode.com/problems/online-election/description/
#
# algorithms
# Medium (51.52%)
# Likes:    682
# Dislikes: 508
# Total Accepted:    39.3K
# Total Submissions: 76.1K
# Testcase Example:  '["TopVotedCandidate","q","q","q","q","q","q"]\n' +
# '[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]'
#
# You are given two integer arrays persons and times. In an election, the i^th
# vote was cast for persons[i] at time times[i].
#
# For each query at a time t, find the person that was leading the election at
# time t. Votes cast at time t will count towards our query. In the case of a
# tie, the most recent vote (among tied candidates) wins.
#
# Implement the TopVotedCandidate class:
#
#
# TopVotedCandidate(int[] persons, int[] times) Initializes the object with the
# persons and times arrays.
# int q(int t) Returns the number of the person that was leading the election
# at time t according to the mentioned rules.
#
#
#
# Example 1:
#
#
# Input
# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
# [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15],
# [24], [8]]
# Output
# [null, 0, 1, 1, 0, 0, 1]
#
# Explanation
# TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0,
# 1, 0], [0, 5, 10, 15, 20, 25, 30]);
# topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is
# leading.
# topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and
# 1 is leading.
# topVotedCandidate.q(25); // return 1, At time 25, the votes are
# [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
# topVotedCandidate.q(15); // return 0
# topVotedCandidate.q(24); // return 0
# topVotedCandidate.q(8); // return 1
#
#
#
#
# Constraints:
#
#
# 1 <= persons.length <= 5000
# times.length == persons.length
# 0 <= persons[i] < persons.length
# 0 <= times[i] <= 10^9
# times is sorted in a strictly increasing order.
# times[0] <= t <= 10^9
# At most 10^4 calls will be made to q.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 投标，排序。
# 堆。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        length = len(persons)
        h = []
        votes = [0] * length
        leadings = []
        for i, p in enumerate(persons):

            votes[p] += 1
            heappush(h, (-votes[p], -i, p))
            leadings.append(h[0][2])

        self.times = times
        self.leadings = leadings

    def q(self, t: int) -> int:

        return self.leadings[bisect_right(self.times, t) - 1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(o.q(3))
    print(o.q(12))
    print(o.q(25))
    print(o.q(15))
    print(o.q(24))
    print(o.q(8))

    pass
# @lc main=end