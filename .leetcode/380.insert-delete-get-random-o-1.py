# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (49.70%)
# Likes:    3925
# Dislikes: 229
# Total Accepted:    367K
# Total Submissions: 737.3K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' +
#   '[[],[1],[2],[2],[],[1],[2],[]]'
#
# Implement the RandomizedSet class:
#
#
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns
# true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns
# true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements
# (it's guaranteed that at least one element exists when this method is
# called). Each element must have the same probability of being returned.
#
#
# You must implement the functions of the class such that each function works
# in average O(1) time complexity.
#
#
# Example 1:
#
#
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
#
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was
# inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now
# contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2
# randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now
# contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set,
# getRandom() will always return 2.
#
#
#
# Constraints:
#
#
# -2^31 <= val <= 2^31 - 1
# At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is
# called.
#
#
#

# @lc tags=array;hash-table;design

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 构建一个类，加入、移除元素，之后获得现有的一个随机值。
# 字典。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class RandomizedSet:
    def __init__(self):
        self.d, self.l = {}, []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.l.append(val)
        self.d[val] = len(self.l) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        self.d[self.l[-1]] = self.d[val]
        self.l[self.d[val]] = self.l[-1]
        self.l.pop()
        self.d.pop(val)
        return True

    def getRandom(self) -> int:
        return self.l[randint(0, len(self.l) - 1)]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__()))
    print()

    pass
# @lc main=end