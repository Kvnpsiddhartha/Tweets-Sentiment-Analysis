from tweets_senti_pkg.imports import *
import os
def replace(s,word):
  return s.replace(word,"")
def deEmojify(text):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.findall(emoj, text)
def cleandata():
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    file1name = os.path.join(thisfolder, 'final.csv')
    file=open(file1name,'r',encoding="utf8")
    file2name=os.path.join(thisfolder, 'tweets.csv')
    with open('tweets.csv','w',encoding="utf8") as file2 :
      csvreader = csv.reader(file)
      csvwriter = csv.writer(file2)
      for row in csvreader:
        if(isinstance(row, list)):
          txt=row[0]
        else:
          txt=row
        text=txt.replace("\n","")
        text=re.sub("\n","",text)
        ext=deEmojify(text)
        txt=re.findall('[!" "]*(@[0-9a-zA-Z]+)[!" "]*',text)
        hxt=re.findall('[!" "]*(#[0-9a-zA-Z]+)[!" "]*',text)
        rtxt=re.findall('RT\S*?[" "]:',text)
        utxt=re.findall('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)',text)
        ttxt=re.findall('https://t.co/\S*',text)
        txt=txt+hxt+ext+rtxt+ttxt+utxt;
        x=text
        for w in txt:
          x=replace(str(x),w)
          x=x.replace("RT :","")
          x=x.replace("RT","")
        x=x.replace("https://t","")
        x=x.replace("https","")
        x=x.strip(" _")
        #print(x)
        csvwriter.writerow([x])
    file.close()

