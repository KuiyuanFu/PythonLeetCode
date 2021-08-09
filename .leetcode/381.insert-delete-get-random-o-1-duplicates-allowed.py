# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
#
# algorithms
# Hard (35.22%)
# Likes:    1249
# Dislikes: 99
# Total Accepted:    91K
# Total Submissions: 258.3K
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n' +
#   '[[],[1],[1],[2],[],[1],[]]'
#
# Implement the RandomizedCollection class:
#
#
# RandomizedCollection() Initializes the RandomizedCollection object.
# bool insert(int val) Inserts an item val into the multiset if not present.
# Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the multiset if present.
# Returns true if the item was present, false otherwise. Note that if val has
# multiple occurrences in the multiset, we only remove one of them.
# int getRandom() Returns a random element from the current multiset of
# elements (it's guaranteed that at least one element exists when this method
# is called). The probability of each element being returned is linearly
# related to the number of same values the multiset contains.
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
# ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove",
# "getRandom"]
# [[], [1], [1], [2], [], [1], []]
# Output
# [null, true, false, true, 2, true, 1]
#
# Explanation
# RandomizedCollection randomizedCollection = new RandomizedCollection();
# randomizedCollection.insert(1);   // return True. Inserts 1 to the
# collection. Returns true as the collection did not contain 1.
# randomizedCollection.insert(1);   // return False. Inserts another 1 to the
# collection. Returns false as the collection contained 1. Collection now
# contains [1,1].
# randomizedCollection.insert(2);   // return True. Inserts 2 to the
# collection, returns true. Collection now contains [1,1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 with the
# probability 2/3, and returns 2 with the probability 1/3.
# randomizedCollection.remove(1);   // return True. Removes 1 from the
# collection, returns true. Collection now contains [1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 and 2 both
# equally likely.
#
#
#
# Constraints:
#
#
# -2^31 <= val <= 2^31 - 1
# At most 2 * 10^5  calls will be made to insert, remove, and getRandom.
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
# 构建一个类，加入、移除元素，之后获得现有的一个随机值。元素可以重复。
# 字典，集合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class RandomizedCollection:
    def __init__(self):
        self.d, self.l = defaultdict(set), []

    def insert(self, val: int) -> bool:
        f = len(self.d[val]) == 0
        self.d[val].add(len(self.l))
        self.l.append(val)
        return f

    def remove(self, val: int) -> bool:
        if len(self.d[val]) == 0:
            return False

        #  last value
        lv = self.l[-1]

        # remove value index set
        vi = self.d[val].pop()

        # laset value index set
        lvs = self.d[lv]

        # move last value to index
        self.l[vi] = lv

        # laset value add new index
        lvs.add(vi)

        # remove val
        self.l.pop()

        # laset value remove old index
        lvs.remove(len(self.l))

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