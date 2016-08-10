"""
important functions:
user.followers_count
API.statuses_lookup(id[, include_entities][, trim_user][, map])
API.get_user(id/user_id/screen_name)
"""
import tweepy

screen_name_toy = ;

# authentikation
auth = tweepy.OAuthHandler("yYZu3hy7HZlYIQuKyXPMsCWOf ", "yD1LFjpaArFpKdsK304MAN0FokTamNZ8EZOIMTgrPhaxnP6Pl3")
auth.set_access_token("763457078044262400-dEWQ8EvB6vW5RRHRUdjDGgCyGBSafok", "xcM83RvjobkEReC1sRTxcnhjgzpkrdKUOkOfnUMpzYBnz")
api = tweepy.API(auth)
