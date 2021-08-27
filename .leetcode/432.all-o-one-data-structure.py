# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
# https://leetcode.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (34.09%)
# Likes:    873
# Dislikes: 111
# Total Accepted:    44K
# Total Submissions: 129K
# Testcase Example:  '["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]\n' +
#   '[[],["hello"],["hello"],[],[],["leet"],[],[]]'
#
# Design a data structure to store the strings' count with the ability to
# return the strings with minimum and maximum counts.
#
# Implement the AllOne class:
#
#
# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not
# exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of
# key is 0 after the decrement, remove it from the data structure. It is
# guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element
# exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element
# exists, return an empty string "".
#
#
#
# Example 1:
#
#
# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey",
# "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]
#
# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"
#
#
#
# Constraints:
#
#
# 1 <= key.length <= 10
# key consists of lowercase English letters.
# It is guaranteed that for each call to dec, key is existing in the data
# structure.
# At most 5 * 10^4 calls will be made to inc, dec, getMaxKey, and getMinKey.
#
#
#

# @lc tags=design

# @lc imports=start
from sys import setcheckinterval
from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计当前每个字符串的个数，之后返回数量最小的和最大的。
# 使用一个字典保存数量，和两个堆保存个数与字符串的元组，每次增减都直接插入一个新的元组，使用字典判断数据是否过期。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class AllOne:
    def __init__(self):
        self.count = defaultdict(int)
        self.mi = []
        self.ma = []

    def inc(self, key: str) -> None:
        c = self.count[key] + 1
        self.count[key] = c
        heappush(self.mi, (c, key))
        heappush(self.ma, (-c, key))

    def dec(self, key: str) -> None:
        c = self.count[key] - 1
        self.count[key] = c
        if self.count[key] == 0:
            self.count.pop(key)
        heappush(self.mi, (c, key))
        heappush(self.ma, (-c, key))

    def getMaxKey(self) -> str:
        if len(self.count) == 0:
            return ''
        while True:
            c, key = self.ma[0]
            if key in self.count \
                and -c == self.count[key]:
                return key
            else:
                heappop(self.ma)

    def getMinKey(self) -> str:
        if len(self.count) == 0:
            return ''
        while True:
            c, key = self.mi[0]
            if key in self.count \
                and c == self.count[key]:
                return key
            else:
                heappop(self.mi)


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