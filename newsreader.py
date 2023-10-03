import requests
import json
from win32com.client import Dispatch


def speaking(speech):
    sk = Dispatch("SAPI.SpVoice")
    sk.Speak(speech)


def news():
    url = ('http://newsapi.org/v2/top-headlines?'
           'sources=google-news-in&'
           'apiKey=6d01f7f2b0744a8d82530916a387208e'
           )
    response = requests.get(url)
    text = response.text
    js = json.loads(text)
    for i in range(0, 10):
        print((js['articles'][i]['title']))
        speaking(js['articles'][i]['title'])
        # print(js)


if __name__ == "__main__":
    news()
