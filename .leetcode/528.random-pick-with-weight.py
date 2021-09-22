# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#
# https://leetcode.com/problems/random-pick-with-weight/description/
#
# algorithms
# Medium (45.29%)
# Likes:    1472
# Dislikes: 3101
# Total Accepted:    204.2K
# Total Submissions: 450.1K
# Testcase Example:  '["Solution","pickIndex"]\r\n[[[1]],[]]\r'
#
# You are given an array of positive integers w where w[i] describes the weight
# of i^th index (0-indexed).
#
# We need to call the function pickIndex() which randomly returns an integer in
# the range [0, w.length - 1]. pickIndex() should return the integer
# proportional to its weight in the w array. For example, for w = [1, 3], the
# probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the
# probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
#
# More formally, the probability of picking index i is w[i] / sum(w).
#
#
# Example 1:
#
#
# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]
#
# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. Since there is only one single element on
# the array the only option is to return the first element.
#
#
# Example 2:
#
#
# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]
#
# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It's returning the second element (index =
# 1) that has probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It's returning the first element (index =
# 0) that has probability of 1/4.
#
# Since this is a randomization problem, multiple answers are allowed so the
# following outputs can be considered correct :
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.
#
#
#
# Constraints:
#
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定每个索引的权重，按权重随机返回索引。
# 累计权重，二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def __init__(self, ws: List[int]):

        idies = [0]
        for w in ws:
            idies.append(idies[-1] + w)
        self.idies = idies

    def pickIndex(self) -> int:

        r = random.randrange(0, self.idies[-1])
        return bisect_right(self.idies, r) - 1


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end