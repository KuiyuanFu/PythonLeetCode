# @lc app=leetcode id=822 lang=python3
#
# [822] Card Flipping Game
#

# @lc tags=string

# @lc imports=start
from turtle import back
from imports import *

# @lc imports=end

# @lc idea=start
#
# 每个卡票有上下两面，求与上面都不同的最小下面，可以交换上下面。
# 只有同张卡片的上下面相同，这个值就不行。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        candidates = set()
        impossibilities = set()
        for i in range(len(fronts)):
            f, b = fronts[i], backs[i]
            if f == b:
                if f in candidates:
                    candidates.remove(f)
                impossibilities.add(f)
            else:
                if f not in impossibilities:
                    candidates.add(f)
                if b not in impossibilities:
                    candidates.add(b)
        return min(candidates) if len(candidates) > 0 else 0
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('fronts = [1,2,4,4,7], backs = [1,3,4,1,3]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().flipgame([1, 2, 4, 4, 7], [1, 3, 4, 1, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('fronts = [1], backs = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().flipgame([1], [1])))
    print()

    pass
# @lc main=end