import json
import tweepy


class TIE():
    def __init__(self, api, filepath = None, count = 200 , limit = 200, name = None, id = None):
        self.limit = limit
        self.screen_name = name
        self.id = id
        self.api = api
        self.count = count
        self.filepath = filepath

    def get_all_tweets(self):
        #initialize a list to hold all the tweepy Tweets
        alltweets = []
        #make initial request for most recent tweets (200 is the maximum allowed count)
        if self.screen_name is not None:
            new_tweets = self.api.user_timeline(screen_name = self.screen_name,count=self.count)
        elif self.id is not None:
            new_tweets = self.api.user_timeline(id = self.id,count=self.count)

        #save most recent tweets
        alltweets.extend(new_tweets)
        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        #keep grabbing tweets until there are no tweets left to grab
        while len(alltweets) < self.limit:
            # print "getting tweets before %s" % (oldest)
            #all subsiquent requests use the max_id param to prevent duplicates
            if self.screen_name is not None:
                new_tweets = self.api.user_timeline(screen_name = self.screen_name,count=self.count,max_id=oldest)
            elif self.id is not None:
                new_tweets = self.api.user_timeline(id = self.id,count=self.count,max_id=oldest)
            #save most recent tweets
            alltweets.extend(new_tweets)
            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1
            print "...%s tweets downloaded so far" % (len(alltweets))

        #transform the tweepy tweets into a 2D array that will populate the csv
        outtweets = [tweet.text.encode("utf-8") for tweet in alltweets]
        return outtweets

        # #write the csv
        # with open('%s_tweets.csv' % screen_name, 'wb') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(["id","created_at","text"])
        #     writer.writerows(outtweets)
        #
        # pass

    def get_user_info(self):
        if self.screen_name is not None:
            user_info = self.api.get_user(self.screen_name)
        elif self.id is not None:
            user_info = self.api.get_user(user_id = self.id)
        return user_info

    def write_json(self):
        user_info = self.get_user_info()
        data = {'screen_name':self.screen_name,
                'name': user_info.name,
                'time_zone': user_info.time_zone,
                'location': user_info.location,
                'followers_count':user_info.followers_count,
                'friend_count':user_info.friends_count,
                'status_count':user_info.statuses_count,
                'lang':user_info.lang,
                'tweets':self.get_all_tweets()}
        jsonData = json.dumps(data,sort_keys=True,indent=4)
        with open(self.filepath, 'a+') as f:
             json.dump((jsonData + '\n').encode('utf-8'), f)
             # f.write('\n')

    def get_json(self):
        user_info = self.get_user_info()
        data = {'screen_name':self.screen_name,
                'name': user_info.name,
                'time_zone': user_info.time_zone,
                'location': user_info.location,
                'followers_count':user_info.followers_count,
                'friend_count':user_info.friends_count,
                'status_count':user_info.statuses_count,
                'lang':user_info.lang,
                'tweets':self.get_all_tweets()}
        jsonData = json.dumps(data,sort_keys=True,indent=4)
        return jsonData

    def get_data(self):
        user_info = self.get_user_info()
        data = {'screen_name':self.screen_name,
                'name': user_info.name,
                'time_zone': user_info.time_zone,
                'location': user_info.location,
                'followers_count':user_info.followers_count,
                'friend_count':user_info.friends_count,
                'status_count':user_info.statuses_count,
                'lang':user_info.lang,
                'tweets':self.get_all_tweets()}
        return data

if __name__ == '__main__':
    #pass in the username of the account you want to download
    auth = tweepy.OAuthHandler("yYZu3hy7HZlYIQuKyXPMsCWOf", "yD1LFjpaArFpKdsK304MAN0FokTamNZ8EZOIMTgrPhaxnP6Pl3")
    auth.set_access_token("763457078044262400-dEWQ8EvB6vW5RRHRUdjDGgCyGBSafok", "xcM83RvjobkEReC1sRTxcnhjgzpkrdKUOkOfnUMpzYBnz")
    api = tweepy.API(auth)
    twitter_info = TIE('J_tsar',api)
    twitter_info.write_json()
    # twitter_info.get_all_tweets()
