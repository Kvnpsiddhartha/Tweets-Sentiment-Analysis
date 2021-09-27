from tweets_senti_pkg.imports import *

 
# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    if sentiment_dict['compound'] >= 0.05 :
        return "Positive"
 
    elif sentiment_dict['compound'] <= - 0.05 :
        return "Negative"
 
    else :
        return "Neutral"
def vader_sentianalysis():
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(thisfolder, 'tweets.csv')
    df=pd.read_csv(file)
    df.columns=['Tweets']
    df['vaderanalysis']=df['Tweets'].apply(sentiment_scores)

    ptweets=df[df.vaderanalysis=='Positive']

    print("Positive tweets %:",ptweets.shape[0]/df.Tweets.shape[0])

