from tweets_senti_pkg.imports import *
def writecsv(filename,res,mode):
  thisfolder = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(thisfolder, filename)
  #f=open(filename+".txt",mode)
  rows=[[i] for i in res]    
  # writing to csv file 
  filename = filename+".csv"
  with open(filename, mode) as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile)                  
    # writing the data rows 
    csvwriter.writerows(rows)

def tweetsearch(searchword,outervar,api):
  tweets = tw.Cursor(api.search,q = searchword, lang ='en').items(1000)
  t=[[tweet.id,tweet.text]for tweet in tweets]
  res=[]
  for item in t:
    status = api.get_status(item[0], tweet_mode = "extended")
    full_text = status.full_text
    res.append(full_text)
  #print(len(res))
  outervar.append(res)
  #writecsv(searchword,res,'w')
  writecsv("final",res,'a')
  return res
