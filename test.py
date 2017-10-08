from pattern.web import URL, DOM, plaintext
from pattern.en import parsetree
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import time
#from ENS import textRank

#Defining blank list
thehill_list = []
cnn_list = []

url_cnn = URL('https://twitter.com/CNNPolitics')
url_hill = URL('https://twitter.com/thehill')
dom_cnn = DOM(url_cnn.download(cached=True))
dom_hill = DOM(url_hill.download(cached=True))
while True:
    for e in dom_hill('div.content'): # Top 3 reddit entries.
        #print("The Hill")
        for c in e('p.tweet-text'):
            d = plaintext(c.content)
            d = d.encode('utf-8')
            if d not in thehill_list:
                thehill_list.append(d)
            #print(d)
            #break
        break
    #print thehill_list
    strr_hill = "".join(str(x) for x in thehill_list)
    #strr = plaintext.decode_entities(strr)
    #print strr
    #strr = strr.encode('utf-8','ignore')
    #s = parsetree(strr, tokenize=True)
    #print strr
    for e in dom_cnn('div.content'): # Top 3 reddit entries.
        #print("The Hill")
        for c in e('p.tweet-text'):
            d = plaintext(c.content)
            d = d.encode('utf-8')
            if d not in cnn_list:
                cnn_list.append(d)
            #print(d)
            #break
        break
    strr_cnn = "".join(str(x) for x in cnn_list)
    main_sent = strr_cnn + " " +strr_hill
    main_sent = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', main_sent)
    stop_words = set(stopwords.words("english"))
    #stop_words_more = [":",",","``",'""']
    #stop_words = stop_words.append(stop_words,stop_words_more)
    words = word_tokenize(main_sent)
    filtered_sent = []
    for w in words:
        if w not in stop_words:
            filtered_sent.append(w)
    print filtered_sent
    time.sleep(5)
