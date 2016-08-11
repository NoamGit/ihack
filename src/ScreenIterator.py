from twython import Twython

def get_tweets_by_hashtag(hashtag):

    TWITTER_APP_KEY = 'z1WOwQaa2Bd6mpXrUJCHzjb6w' #supply the appropriate value
    TWITTER_APP_KEY_SECRET = 'ckk6o5RtV6rpie1s8E2Ev8OTq4XTqMoPnmDjoixfHbhHYw83P0'
    TWITTER_ACCESS_TOKEN = '202681219-FJgmXR9s2Bks0MZt9OYS0s5FVnwk90zqnGPukNex'
    TWITTER_ACCESS_TOKEN_SECRET = 'KRsQL796D0JASy2drHEt8dboyaQimOFyUaqKBea2D1jfR'

    t = Twython(app_key=TWITTER_APP_KEY,
                app_secret=TWITTER_APP_KEY_SECRET,
                oauth_token=TWITTER_ACCESS_TOKEN,
                oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

    search = t.search(q='#'+hashtag, count=200)

    tweets = search['statuses']

    for tweet in tweets:
        yield (tweet['user']['screen_name']).encode("utf-8")
        # yield tweet['id_str'].encode("utf-8")+'    '.encode("utf-8")+ tweet['text'].encode("utf-8")

def get_user_by_hash(api, hash_name, max_attemps = 100, max_tweets = 500):
    user_counts = 0
    max_attemps                    =   100
    max_tweets   =   500

    for i in range(0,max_attemps):

        if(max_tweets < user_counts):
            break

        # STEP 1: Query Twitter
        if(0 == i):
            # Query twitter for data.
            results    = api.search(q=hash_name,count='100')
        else:
            # After the first call we should have max_id from result of previous call. Pass it in query.
            results = api.search(q=hash_name,include_entities='true',max_id=next_max_id, count = '100')

        # STEP 2: Save the returned tweets
        for result in results['statuses']:
            user_id = (result['user']['screen_name']).encode("utf-8")
            user_counts += 1
            yield user_id

        # STEP 3: Get the next max_id
        try:
            # Parse the data returned to get max_id to be passed in consequent call.
            next_results_url_params    = results['search_metadata']['next_results']
            next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
        except:
            # No more next pages
            break

if __name__ == '__main__':
    TWITTER_APP_KEY = 'z1WOwQaa2Bd6mpXrUJCHzjb6w' #supply the appropriate value
    TWITTER_APP_KEY_SECRET = 'ckk6o5RtV6rpie1s8E2Ev8OTq4XTqMoPnmDjoixfHbhHYw83P0'
    TWITTER_ACCESS_TOKEN = '202681219-FJgmXR9s2Bks0MZt9OYS0s5FVnwk90zqnGPukNex'
    TWITTER_ACCESS_TOKEN_SECRET = 'KRsQL796D0JASy2drHEt8dboyaQimOFyUaqKBea2D1jfR'

    api = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

    # tweets = get_tweets_unlimited(api, '#BDS')
    # print len(tweets)
    count = 0
    for tweet_user in get_user_by_hash(api, '#BDS'):
        print tweet_user
        count += 1
        print count