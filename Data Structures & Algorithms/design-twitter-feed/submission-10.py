class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.tweets:
            self.tweets[userId]=set()
        self.tweets[userId].add((self.count,tweetId))
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        users = [userId]
        for followee in self.following.get(userId, set()):
            users.append(followee)

        heap = []

        for user in users:
            for tweet in self.tweets.get(user, set()):
                heapq.heappush(heap, tweet)

        ret = []

        while len(ret)<10 and len(heap)>0:
            ret.append(heapq.heappop(heap)[1])
        return ret
        # tweets = [
        #     tweet
        #     for user in users
        #     for tweet in self.tweets.get(user, set())
        # ]

        # heapq.heapify(tweets)
        
        # tweets.sort(key=lambda tweet: tweet[0], reverse=True)
        # tweets = [ tweet[1] for tweet in tweets]
        #print(tweets,"tweets")
        # return tweets[:10]
        
        

        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.following:
            self.following[followerId]=set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        
        
