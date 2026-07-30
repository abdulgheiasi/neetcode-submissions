class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []

        users = self.following[userId] | {userId}

        for user in users:
            for time, tweetId in self.tweets[user][-10:]:
                heapq.heappush(min_heap, (time, tweetId))

                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        result = []

        while min_heap:
            time, tweetId = heapq.heappop(min_heap)
            result.append(tweetId)

        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
