"""
important functions:
user.followers_count
API.statuses_lookup(id[, include_entities][, trim_user][, map])
API.get_user(id/user_id/screen_name)
"""
import tweepy
from twython import Twython
import ScreenIterator as si
import TwitterInfoExtracter as ti

# const

list_bad = ['bds','sjp', 'occupation', 'appartheid' ,'seperation wall', 'genocide', 'baby killer', 'discrimination',
            'segregation', 'nazis', 'nazi', 'hitler', 'demon', 'vampire', 'freedom fighter', 'intifada', 'martyr', 'shahid',
            'resistence', 'violence', 'boycott', 'divestment', 'senction','jvp', 'palestine', 'palestinians','jewish voice for peace',
            'iran', 'hezbollah', 'hamas', 'abbas','gaza', 'free', 'checkpoint', 'protest', 'vandalism','swastika','propaganda']
list_good = ['refugees', 'israel', 'terror', 'victims', 'zionism', 'human rights', 'democracy','security', 'indigenous', 'native', 'ancient',
             'historical','homeland', 'holyland', 'western wall','jewish','jew','jews', 'peace', 'hope', 'advocate', 'freedom',
             'soldiers', 'barrier','fence']
list_hashtags = ['#freepalestine','#fromtherivertothesea','#apartheidwall','#checkpoint','#bds','#boycott']
list_ambig = ['#humanrights','#israel','#westbank','#peace']

toy_user_id = '11512282'

# authentikation

path = "C:\\Users\\Noam\\Documents\\GitHub\\ihack\\Data"
TWITTER_APP_KEY = "yYZu3hy7HZlYIQuKyXPMsCWOf"
TWITTER_APP_KEY_SECRET = "yD1LFjpaArFpKdsK304MAN0FokTamNZ8EZOIMTgrPhaxnP6Pl3"
TWITTER_ACCESS_TOKEN= "763457078044262400-dEWQ8EvB6vW5RRHRUdjDGgCyGBSafok"
TWITTER_ACCESS_TOKEN_SECRET = "xcM83RvjobkEReC1sRTxcnhjgzpkrdKUOkOfnUMpzYBnz"
auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api_tweepy = tweepy.API(auth)
api = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

users_itr = si.get_tweets_unlimited(api, '#freepalestine')
count =0
user_obj = ti.TIE( api_tweepy, filepath = path + "\\test.JSON", id = toy_user_id)
toy_data = user_obj.get_data()

for screen_name in users_itr:
    user_obj = ti.TIE( api_tweepy, filepath = path + "\\test.JSON", name = screen_name)
    user_obj.write_json()
    count += 1
    if count > 4 :
        break

print 'Done!'

## feature generation

user_obj.get_user_info()

