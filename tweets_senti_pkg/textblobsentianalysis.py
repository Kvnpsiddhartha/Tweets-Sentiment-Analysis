from tweets_senti_pkg.imports import *
def getSubjectivity(text):
  return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
  return TextBlob(text).sentiment.polarity
def textblob_sentianalysis():
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(thisfolder, 'tweets.csv')
    df=pd.read_csv(file)
    df.columns=['Tweets']
    df['subjectivity']=df['Tweets'].apply(getSubjectivity)
    df['polarity']=df['Tweets'].apply(getPolarity)

    words=' '.join([tweet for tweet in df['Tweets']])

    wordcloud = WordCloud(width=600,height=300,max_font_size=119,random_state=12).generate(words)

    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.show()

    def getAnalysis(score):
      if score<0:
        return 'Negative'
      elif score==0:
        return 'Neutral'
      else:
        return 'Positive'

    df['analysis']=df['polarity'].apply(getAnalysis)

    ptweets=df[df.analysis=='Positive']
    print("Positive tweets %:",ptweets.shape[0]/df.Tweets.shape[0])
