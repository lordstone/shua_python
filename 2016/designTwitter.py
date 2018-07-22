import heapq

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.users = {}  # userId: [tweets, userId}
        self.token = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.users:
            self.users[userId][0].append((self.token, tweetId))
        else:
            self.users[userId] = [[(self.token, tweetId)], set()]
        self.token += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users: return []
        res = []
        hq = []
        ptr = {}
        candidates = list(self.users[userId][1]) + [userId]
        for i in candidates:
            if len(self.users[i][0]) > 0:
                tweet = self.users[i][0][len(self.users[i][0]) - 1]
                ptr[i] = len(self.users[i][0]) - 1
                heapq.heappush(hq, (-tweet[0], tweet[1], i))
        for i in range(10):
            if len(hq) == 0: break
            token, tid, uid = heapq.heappop(hq)
            res.append(tid)
            ptr[uid] -= 1
            if ptr[uid] >= 0:
                tweet = self.users[uid][0][ptr[uid]]
                heapq.heappush(hq, (-tweet[0], tweet[1], uid))
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.users:
            self.users[followerId][1].add(followeeId)
        else:
            self.users[followerId] = [[], set([followeeId])]
        if followeeId not in self.users:
            self.users[followeeId] = [[], set()]

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.users:
            if followeeId in self.users[followerId][1]:
                self.users[followerId][1].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
obj = Twitter()

