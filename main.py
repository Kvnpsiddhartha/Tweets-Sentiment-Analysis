#package to intall
#pip install tweepy
#pip install textblob
#pip install vaderSentiment
#pip install wordcloud
#pip install pandas
#pip install matplotlib
#pip install numpy
#pip install csv
#pip install configparser
from tweets_senti_pkg import *
def printretrived(tag):
    print("Retrieved "+tag+" tweets")


api=twitterconfigure()
print("twitter api started")
outervar=[]
tweetsearch("#incometaxportal",outervar,api)
printretrived("#incometaxportal")

tweetsearch("#incometaxnewportal",outervar,api)
printretrived("#incometaxnewportal)
              
tweetsearch('@IncomeTaxIndia  and  @Infosys',outervar,api)
printretrived('@IncomeTaxIndia  and  @Infosys')
              
tweetsearch("#NewITRPortal",outervar,api)
printretrived("#NewITRPortal")
              
tweetsearch("#newincometaxportal",outervar,api)
printretrived("#newincometaxportal")
              
tweetsearch("#ITRportal",outervar,api)
printretrived("#ITRportal")
              
tweetsearch("#InfosysFail",outervar,api)
printretrived("#InfosysFail")
              
tweetsearch("#IncomeTaxPortal",outervar,api)
printretrived("#IncomeTaxPortal")
print("cleaning")
cleandata()
print("tb senti")
textblob_sentianalysis()
print("vader senti")
vader_sentianalysis()

