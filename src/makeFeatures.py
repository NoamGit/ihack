import nltk
import numpy as np
from pytz import timezone, all_timezones


class theFeatures():

    def __init__(self, user_data = None):
        self.user_data = user_data

    def getDictVec(self, dict_list):
        text = ' '.join(self.user_data['tweets'])
        dict_feature_vec = []
        for dict in dict_list:
            np.append( dict_feature_vec, np.asarray([text.count(term) for term in dict]) )
        dict_feature_vec /= np.max(dict_feature_vec) # normalize by max
        return dict_feature_vec

    def getLocation(self):
        tz = filter(lambda x: self.user_data['time_zone'] in x, all_timezones)
        utc_offset = (timezone(tz[0]))._utcoffset.total_seconds()/(60*60)
        return utc_offset

    def getAmbigSentiment(self, list):
        super_tweets = [t for t in self.user_data['tweets'] if np.any([t.count(term) for term in list])];
    return

    def getFeatures():
    return