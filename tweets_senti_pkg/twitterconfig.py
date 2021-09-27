import os
from tweets_senti_pkg.imports import *
def twitterconfigure():
    config = configparser.RawConfigParser()
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(thisfolder, 'twitter.txt')
    config.read(filenames = file)
    accesstoken = config.get('twitter','accesstoken') 
    accesstokensecret = config.get('twitter','accesstokensecret') 
    apikey = config.get('twitter','apikey') 
    apisecretkey = config.get('twitter','apisecretkey')
    auth = tw.OAuthHandler(apikey,apisecretkey) 
    auth.set_access_token(accesstoken,accesstokensecret) 
    api = tw.API(auth,wait_on_rate_limit=True)
    return api
