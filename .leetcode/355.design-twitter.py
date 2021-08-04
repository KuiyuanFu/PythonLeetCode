# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (32.61%)
# Likes:    1478
# Dislikes: 244
# Total Accepted:    71K
# Total Submissions: 216.9K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +
#   '[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user, and is able to see the 10 most recent tweets in
# the user's news feed.
#
# Implement the Twitter class:
#
#
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId
# by the user userId. Each call to this function will be made with a unique
# tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs
# in the user's news feed. Each item in the news feed must be posted by users
# who the user followed or by the user themself. Tweets must be ordered from
# most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId
# started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId
# started unfollowing the user with ID followeeId.
#
#
#
# Example 1:
#
#
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed",
# "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]
#
# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2
# tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is
# posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5], since user 1 is no longer following user 2.
#
#
#
# Constraints:
#
#
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 10^4
# All the tweets have unique IDs.
# At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and
# unfollow.
#
#
#

# @lc tags=hash-table;heap;design

# @lc imports=start
from heapq import heapify, heappop, heappush, heappushpop
from imports import *

# @lc imports=end

# @lc idea=start
#
# 设计实现一个简单的Twitter。
# 使用字典，堆，来实现最近消息。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Twitter:
    def __init__(self):
        from queue import Queue
        from collections import defaultdict
        from heapq import heappop, heappush, heappushpop
        self.n = 0
        self.u2p = defaultdict(list)
        self.f = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.n += 1
        self.u2p[userId].append((self.n, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        h = self.u2p[userId][:-11:-1]
        heapify(h)
        followees = self.f[userId]
        for followee in followees:
            ps = self.u2p[followee]
            for p in reversed(ps):
                if len(h) < 10:
                    heappush(h, p)
                else:
                    # 大，说明新，那么ps中就没有更新的了，也就不需要饿了。
                    if h[0] > p:
                        break
                    else:
                        heappushpop(h, p)
        r = []
        while h:
            r.append(heappop(h)[1])

        return r[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.f[followerId]:
            self.f[followerId].remove(followeeId)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))
    pass
# @lc main=end