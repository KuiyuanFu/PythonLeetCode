# @lc app=leetcode id=710 lang=python3
#
# [710] Random Pick with Blacklist
#
# https://leetcode.com/problems/random-pick-with-blacklist/description/
#
# algorithms
# Hard (33.27%)
# Likes:    497
# Dislikes: 83
# Total Accepted:    22.2K
# Total Submissions: 66.8K
# Testcase Example:  '["Solution","pick","pick","pick","pick","pick","pick","pick"]\n' +
# '[[7,[2,3,5]],[],[],[],[],[],[],[]]'
#
# You are given an integer n and an array of unique integers blacklist. Design
# an algorithm to pick a random integer in the range [0, n - 1] that is not in
# blacklist. Any integer that is in the mentioned range and not in blacklist
# should be equally likely to be returned.
#
# Optimize your algorithm such that it minimizes the number of calls to the
# built-in random function of your language.
#
# Implement the Solution class:
#
#
# Solution(int n, int[] blacklist) Initializes the object with the integer n
# and the blacklisted integers blacklist.
# int pick() Returns a random integer in the range [0, n - 1] and not in
# blacklist.
#
#
#
# Example 1:
#
#
# Input
# ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
# [[7, [2, 3, 5]], [], [], [], [], [], [], []]
# Output
# [null, 0, 4, 1, 6, 1, 0, 4]
#
# Explanation
# Solution solution = new Solution(7, [2, 3, 5]);
# solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note
# that for every call of pick,
# ⁠                // 0, 1, 4, and 6 must be equally likely to be returned
# (i.e., with probability 1/4).
# solution.pick(); // return 4
# solution.pick(); // return 1
# solution.pick(); // return 6
# solution.pick(); // return 1
# solution.pick(); // return 0
# solution.pick(); // return 4
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
# 0 <= blacklist.length <- min(10^5, n - 1)
# 0 <= blacklist[i] < n
# All the values of blacklist are unique.
# At most 2 * 10^4 calls will be made to pick.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 随机数，有黑名单。
# 生成随机数，得到的随机数，就是在空白位置上的索引。
# 将黑名单排序，得到每个空白区域前面的黑名单数量，得到跳跃的个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        blacklist.sort()

        blc = []
        preb = -1
        prec = 0
        for b in blacklist:

            if b == preb:
                blc.append(prec)
            else:
                prec = b - len(blc)
                blc.append(prec)

            preb = b

        self.blc = blc
        self.s = n - len(self.blc)

    def pick(self) -> int:

        r = random.randint(0, self.s - 1)
        idx = bisect_right(self.blc, r)
        r += idx
        return r


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = Solution(7, [2, 3, 5])
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
    pass
# @lc main=end