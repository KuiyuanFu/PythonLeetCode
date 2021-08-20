# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (69.10%)
# Likes:    4308
# Dislikes: 471
# Total Accepted:    204K
# Total Submissions: 294.7K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# You are given an array of people, people, which are the attributes of some
# people in a queue (not necessarily in order). Each people[i] = [hi, ki]
# represents the i^th person of height hi with exactly ki other people in front
# who have a height greater than or equal to hi.
#
# Reconstruct and return the queue that is represented by the input array
# people. The returned queue should be formatted as an array queue, where
# queue[j] = [hj, kj] is the attributes of the j^th person in the queue
# (queue[0] is the person at the front of the queue).
#
#
# Example 1:
#
#
# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# Explanation:
# Person 0 has height 5 with no other people taller or the same height in
# front.
# Person 1 has height 7 with no other people taller or the same height in
# front.
# Person 2 has height 5 with two persons taller or the same height in front,
# which is person 0 and 1.
# Person 3 has height 6 with one person taller or the same height in front,
# which is person 1.
# Person 4 has height 4 with four people taller or the same height in front,
# which are people 0, 1, 2, and 3.
# Person 5 has height 7 with one person taller or the same height in front,
# which is person 1.
# Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
#
#
# Example 2:
#
#
# Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
#
#
#
# Constraints:
#
#
# 1 <= people.length <= 2000
# 0 <= hi <= 10^6
# 0 <= ki < people.length
# It is guaranteed that the queue can be reconstructed.
#
#
#

# @lc tags=greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列人的身高和前面有多少人身高不小于其，对数组进行排序。
# 先按照身高排序，之后从低到高进行插入，因为之后插入的都大于等于其，所以可以根据空位来确定个数。
# 使用线段树来确定空位个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Segment:
    def __init__(self, l, r, lp=None, rp=None) -> None:
        self.l = l
        self.r = r
        self.lp = lp
        self.rp = rp
        self.val = r - l + 1


class Solution:
    def reconstructQueue(self, peoples: List[List[int]]) -> List[List[int]]:
        if len(peoples) <= 1:
            return peoples
        peoples.sort()
        res = [None] * len(peoples)

        def initSegment(l, r):
            root = Segment(l, r)
            if l == r:
                return root
            m = (r + l) // 2
            root.lp = initSegment(l, m)
            root.rp = initSegment(m + 1, r)
            return root

        root = initSegment(0, len(peoples) - 1)

        hPre, nPre = -1, 1
        for people in peoples:
            h, k = people
            if h == hPre:
                k -= nPre
                nPre += 1
            else:
                hPre, nPre = h, 1
            k += 1
            p = root
            while p.l != p.r:
                p.val -= 1
                if p.lp.val == 0 or p.lp.val < k:
                    k -= p.lp.val
                    p = p.rp
                else:
                    p = p.lp
            p.val -= 1
            res[p.l] = people

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().reconstructQueue([])))
    print(str(Solution().reconstructQueue([[1, 0]])))
    print('Example 1:')
    print('Input : ')
    print('people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]')
    print('Exception :')
    print('[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]')
    print('Output :')
    print(
        str(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0],
                                         [6, 1], [5, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]')
    print('Exception :')
    print('[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]')
    print('Output :')
    print(
        str(Solution().reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2],
                                         [2, 2], [1, 4]])))
    print()

    pass
# @lc main=end