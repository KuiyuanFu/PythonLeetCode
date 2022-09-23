# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
# https://leetcode.com/problems/time-based-key-value-store/description/
#
# algorithms
# Medium (52.31%)
# Likes:    2532
# Dislikes: 261
# Total Accepted:    218.8K
# Total Submissions: 418.2K
# Testcase Example:  '["TimeMap","set","get","get","set","get","get"]\n' +
# '[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]'
#
# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a
# certain timestamp.
#
# Implement the TimeMap class:
#
#
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the
# value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was
# called previously, with timestamp_prev <= timestamp. If there are multiple
# such values, it returns the value associated with the largest timestamp_prev.
# If there are no values, it returns "".
#
#
#
# Example 1:
#
#
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo",
# 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along
# with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value
# corresponding to foo at timestamp 3 and timestamp 2, then the only value is
# at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along
# with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
#
#
#
# Constraints:
#
#
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 10^7
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 10^5 calls will be made to set and get.
#
#
#

# @lc tags=greedy

# @lc imports=start
from re import A
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定键值对及其时间戳，根据时间获得当前最新的值。
# 直接二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(lambda: [[], []])

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamps, values = self.timestamps[key]
        timestamps.append(timestamp)
        values.append(value)
        pass

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ''

        timestamps, values = self.timestamps[key]
        idx = bisect_right(timestamps, timestamp) - 1
        if idx == -1:
            return ''
        value = values[idx]
        return value


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    print(obj.get("foo", 1))
    print(obj.get("foo", 3))
    obj.set("foo", "bar2", 4)
    print(obj.get("foo", 4))
    print(obj.get("foo", 5))

# @lc main=end