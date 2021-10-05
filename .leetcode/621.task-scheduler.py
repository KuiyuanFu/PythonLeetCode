# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (53.33%)
# Likes:    5614
# Dislikes: 1034
# Total Accepted:    298.3K
# Total Submissions: 557.6K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a characters array tasks, representing the tasks a CPU needs to do,
# where each letter represents a different task. Tasks could be done in any
# order. Each task is done in one unit of time. For each unit of time, the CPU
# could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown
# period between two same tasks (the same letter in the array), that is that
# there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish
# all the given tasks.
#
#
# Example 1:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
#
#
# Example 2:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
#
#
# Example 3:
#
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle
# -> idle -> A
#
#
#
# Constraints:
#
#
# 1 <= task.length <= 10^4
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].
#
#
#

# @lc tags=array;greedy;queue

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 相同任务有间隔，问最少总时间。
# 贪心，每次安放合法的，数量最多的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        q = deque([None] * (n + 1))
        d = defaultdict(int)
        for t in tasks:
            d[t] += 1
        h = []
        for k in d.keys():
            v = d[k]
            heappush(h, -v)
        res = 0
        qLength = 0
        while h or qLength:
            res += 1
            v = q[0]
            q.popleft()
            if v:
                qLength -= 1
                heappush(h, v)
            v = None
            if h:
                v = heappop(h) + 1
                if v == 0:
                    v = None
                else:
                    qLength += 1
            q.append(v)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('tasks = ["A","A","A","B","B","B"], n = 2')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('tasks = ["A","A","A","B","B","B"], n = 0')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2')
    print('Exception :')
    print('16')
    print('Output :')
    print(
        str(Solution().leastInterval(
            ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)))
    print()

    pass
# @lc main=end