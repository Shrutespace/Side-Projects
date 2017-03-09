import re
import requests
#import nltk
from bs4 import BeautifulSoup

url = 'http://www.lyrics.com/eminem'
r = requests.get(url)
soup = BeautifulSoup(r.content)
gdata = soup.find_all('div',{'class':'row'})

eminemLyrics = []

for item in gdata:
    title = item.find_all('a',{'itemprop':'name'})[0].text
    lyricsdotcom = 'http://www.lyrics.com'
    for link in item('a'):
        try:
            lyriclink = lyricsdotcom+link.get('href')
            req = requests.get(lyriclink)
            lyricsoup = BeautifulSoup(req.content)
            lyricdata = lyricsoup.find_all('div',{'id':re.compile('lyric_space|lyrics')})[0].text
            eminemLyrics.append([title,lyricdata])
            print title
            print lyricdata
            print
        except:
            pass

from nltk.tokenize import word_tokenize, sent_tokenize
words = [word_tokenize(t) for t in sent_tokenize(lyric_text)]
