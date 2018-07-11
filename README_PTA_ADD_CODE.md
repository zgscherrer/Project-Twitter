
## Contents: Outside code that was used to produce results in the Presentation

1) Zachary - code to create entire data file from Twitter using API

2) James - code to produce the live graff of a changing status of Top Ten Users using API

3) Verna - code to obtain CAP and Meter ratings from Botometer using API

## Zachary - code to create entire data file from Twitter using API


```python
import tweepy
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
# Twitter API Keys
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
app_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
app_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(app_key, app_secret)
api = tweepy.API(auth)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
```


```python
file = 'http://tweeplers.com/?cc=WORLD'
response = requests.get(file)
```


```python
txt = response.text
top_names = re.findall("@(.*)<", txt)
top_names = [x.split('<')[0] for x in top_names][:10]
sentiment = []
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
tweets = []
```


```python
top_names
```




    ['realDonaldTrump',
     'YouTube',
     'FoxNews',
     'maddow',
     'GOP',
     'CNN',
     'lopezobrador_',
     'BTS_twt',
     'FCFSeleccionCol',
     'MSNBC']




```python
for user in top_names:
    num_tweets = 1
    #for status in tweepy.Cursor(api.user_timeline, id=user).items(100):
    for status in tweepy.Cursor(api.search, q=user).items(100):
        _status = status._json
        _status["top_user"] = user
        tweets.append(_status)
```


```python
def get_sentiment(tweet_text):
    results = analyzer.polarity_scores(tweet_text)
    return results

df = pd.DataFrame(tweets)
df['sentiment'] = df['text'].map(get_sentiment)
df['pos'] = df['sentiment'].map(lambda x: x.get('pos'))
df['neg'] = df['sentiment'].map(lambda x: x.get('neg'))
df['neu'] = df['sentiment'].map(lambda x: x.get('neu'))
df['comp'] = df['sentiment'].map(lambda x: x.get('compound'))
df['user_screen_name'] = df['user'].map(lambda x: x.get('screen_name'))
df['hashtags'] = df['entities'].map(lambda x: [j.get('text') for j in x.get('hashtags')])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>contributors</th>
      <th>coordinates</th>
      <th>created_at</th>
      <th>entities</th>
      <th>extended_entities</th>
      <th>favorite_count</th>
      <th>favorited</th>
      <th>geo</th>
      <th>id</th>
      <th>id_str</th>
      <th>...</th>
      <th>top_user</th>
      <th>truncated</th>
      <th>user</th>
      <th>sentiment</th>
      <th>pos</th>
      <th>neg</th>
      <th>neu</th>
      <th>comp</th>
      <th>user_screen_name</th>
      <th>hashtags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:49 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349787443838977</td>
      <td>1014349787443838977</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 757607643619799040, 'id_str': '75760764...</td>
      <td>{'neg': 0.0, 'neu': 0.866, 'pos': 0.134, 'comp...</td>
      <td>0.134</td>
      <td>0.000</td>
      <td>0.866</td>
      <td>0.5719</td>
      <td>CAEdge</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:49 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349786823053312</td>
      <td>1014349786823053312</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 75423648, 'id_str': '75423648', 'name':...</td>
      <td>{'neg': 0.0, 'neu': 0.881, 'pos': 0.119, 'comp...</td>
      <td>0.119</td>
      <td>0.000</td>
      <td>0.881</td>
      <td>0.4019</td>
      <td>tiredofgop</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:49 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349786709979141</td>
      <td>1014349786709979141</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 3010771532, 'id_str': '3010771532', 'na...</td>
      <td>{'neg': 0.209, 'neu': 0.65, 'pos': 0.141, 'com...</td>
      <td>0.141</td>
      <td>0.209</td>
      <td>0.650</td>
      <td>-0.5267</td>
      <td>acertainparty</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:49 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>{'media': [{'id': 1014309280105709568, 'id_str...</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349784931557376</td>
      <td>1014349784931557376</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 756537471723188224, 'id_str': '75653747...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>karenkauten</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349784243679234</td>
      <td>1014349784243679234</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 982623739, 'id_str': '982623739', 'name...</td>
      <td>{'neg': 0.699, 'neu': 0.301, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.699</td>
      <td>0.301</td>
      <td>-0.9690</td>
      <td>asoonerntx</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>5</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349783987699712</td>
      <td>1014349783987699712</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 214561270, 'id_str': '214561270', 'name...</td>
      <td>{'neg': 0.162, 'neu': 0.838, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.162</td>
      <td>0.838</td>
      <td>-0.4404</td>
      <td>drdavidshapiro</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [{'text': 'DeepStateCorruption', ...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349783954219008</td>
      <td>1014349783954219008</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 988205304537116672, 'id_str': '98820530...</td>
      <td>{'neg': 0.227, 'neu': 0.773, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.227</td>
      <td>0.773</td>
      <td>-0.4767</td>
      <td>BettyMc61352112</td>
      <td>[DeepStateCorruption]</td>
    </tr>
    <tr>
      <th>7</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>{'media': [{'id': 1014336600111661056, 'id_str...</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349783815745537</td>
      <td>1014349783815745537</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 2495771354, 'id_str': '2495771354', 'na...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>2back_1forth</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>8</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349783652134912</td>
      <td>1014349783652134912</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 73128187, 'id_str': '73128187', 'name':...</td>
      <td>{'neg': 0.0, 'neu': 0.621, 'pos': 0.379, 'comp...</td>
      <td>0.379</td>
      <td>0.000</td>
      <td>0.621</td>
      <td>0.6705</td>
      <td>desertlizzy</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>9</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>{'media': [{'id': 1014349774982545409, 'id_str...</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349783476162560</td>
      <td>1014349783476162560</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 819232880584863744, 'id_str': '81923288...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>SteenerBeaner</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>10</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349782385557504</td>
      <td>1014349782385557504</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 805473976277409792, 'id_str': '80547397...</td>
      <td>{'neg': 0.106, 'neu': 0.693, 'pos': 0.201, 'co...</td>
      <td>0.201</td>
      <td>0.106</td>
      <td>0.693</td>
      <td>0.3254</td>
      <td>lelliott1221</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>11</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349782150770689</td>
      <td>1014349782150770689</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 270043148, 'id_str': '270043148', 'name...</td>
      <td>{'neg': 0.103, 'neu': 0.897, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.103</td>
      <td>0.897</td>
      <td>-0.3182</td>
      <td>Jester481</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>12</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349781987201025</td>
      <td>1014349781987201025</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 1003140818436272128, 'id_str': '1003140...</td>
      <td>{'neg': 0.0, 'neu': 0.866, 'pos': 0.134, 'comp...</td>
      <td>0.134</td>
      <td>0.000</td>
      <td>0.866</td>
      <td>0.5719</td>
      <td>GroganLaney</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>13</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349781756329984</td>
      <td>1014349781756329984</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>True</td>
      <td>{'id': 934941143120322560, 'id_str': '93494114...</td>
      <td>{'neg': 0.082, 'neu': 0.823, 'pos': 0.095, 'co...</td>
      <td>0.095</td>
      <td>0.082</td>
      <td>0.823</td>
      <td>0.0644</td>
      <td>OneOf65Million</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>14</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349781123117056</td>
      <td>1014349781123117056</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 792870666626330625, 'id_str': '79287066...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>Memphisbelle51</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>15</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:48 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349780452028417</td>
      <td>1014349780452028417</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 533469077, 'id_str': '533469077', 'name...</td>
      <td>{'neg': 0.416, 'neu': 0.584, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.416</td>
      <td>0.584</td>
      <td>-0.9153</td>
      <td>ruthsatchfield</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>16</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:47 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349780321959936</td>
      <td>1014349780321959936</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 926838977168117760, 'id_str': '92683897...</td>
      <td>{'neg': 0.0, 'neu': 0.873, 'pos': 0.127, 'comp...</td>
      <td>0.127</td>
      <td>0.000</td>
      <td>0.873</td>
      <td>0.4926</td>
      <td>CoffeyCara1</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>17</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:47 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349779625799680</td>
      <td>1014349779625799680</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 736354610332344320, 'id_str': '73635461...</td>
      <td>{'neg': 0.0, 'neu': 0.672, 'pos': 0.328, 'comp...</td>
      <td>0.328</td>
      <td>0.000</td>
      <td>0.672</td>
      <td>0.8074</td>
      <td>MommaB17041818</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>18</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:47 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349779403399174</td>
      <td>1014349779403399174</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 714700202150596608, 'id_str': '71470020...</td>
      <td>{'neg': 0.106, 'neu': 0.693, 'pos': 0.201, 'co...</td>
      <td>0.201</td>
      <td>0.106</td>
      <td>0.693</td>
      <td>0.3254</td>
      <td>lala_mae46</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>19</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:47 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>{'media': [{'id': 1014349774894632960, 'id_str...</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349778979905536</td>
      <td>1014349778979905536</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 883294891404656640, 'id_str': '88329489...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>TEABONE8</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>20</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:47 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349777318838272</td>
      <td>1014349777318838272</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 4806120454, 'id_str': '4806120454', 'na...</td>
      <td>{'neg': 0.0, 'neu': 0.762, 'pos': 0.238, 'comp...</td>
      <td>0.238</td>
      <td>0.000</td>
      <td>0.762</td>
      <td>0.5216</td>
      <td>AlexMalawski</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>21</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:47 +0000 2018</td>
      <td>{'hashtags': [{'text': 'DeepState', 'indices':...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349777012740097</td>
      <td>1014349777012740097</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>True</td>
      <td>{'id': 66033904, 'id_str': '66033904', 'name':...</td>
      <td>{'neg': 0.0, 'neu': 0.867, 'pos': 0.133, 'comp...</td>
      <td>0.133</td>
      <td>0.000</td>
      <td>0.867</td>
      <td>0.3182</td>
      <td>smartvalueblog</td>
      <td>[DeepState, ShadowGovernment]</td>
    </tr>
    <tr>
      <th>22</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:47 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349776853200896</td>
      <td>1014349776853200896</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>True</td>
      <td>{'id': 806747256749584384, 'id_str': '80674725...</td>
      <td>{'neg': 0.0, 'neu': 0.835, 'pos': 0.165, 'comp...</td>
      <td>0.165</td>
      <td>0.000</td>
      <td>0.835</td>
      <td>0.4114</td>
      <td>loveanalto</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>23</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:47 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349776215773185</td>
      <td>1014349776215773185</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 3074470992, 'id_str': '3074470992', 'na...</td>
      <td>{'neg': 0.0, 'neu': 0.792, 'pos': 0.208, 'comp...</td>
      <td>0.208</td>
      <td>0.000</td>
      <td>0.792</td>
      <td>0.6124</td>
      <td>kstreet111</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>24</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:46 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349775695515648</td>
      <td>1014349775695515648</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>True</td>
      <td>{'id': 28286468, 'id_str': '28286468', 'name':...</td>
      <td>{'neg': 0.151, 'neu': 0.849, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.151</td>
      <td>0.849</td>
      <td>-0.5216</td>
      <td>TheInvisibleMo</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>25</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:46 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349775632846853</td>
      <td>1014349775632846853</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 733087664631472128, 'id_str': '73308766...</td>
      <td>{'neg': 0.0, 'neu': 0.924, 'pos': 0.076, 'comp...</td>
      <td>0.076</td>
      <td>0.000</td>
      <td>0.924</td>
      <td>0.2247</td>
      <td>jjwhite14green</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>26</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:46 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349774752018432</td>
      <td>1014349774752018432</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 1450205275, 'id_str': '1450205275', 'na...</td>
      <td>{'neg': 0.246, 'neu': 0.508, 'pos': 0.246, 'co...</td>
      <td>0.246</td>
      <td>0.246</td>
      <td>0.508</td>
      <td>0.0000</td>
      <td>jimi_the_greek</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>27</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:46 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349774269579265</td>
      <td>1014349774269579265</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 932721061053059073, 'id_str': '93272106...</td>
      <td>{'neg': 0.145, 'neu': 0.855, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.145</td>
      <td>0.855</td>
      <td>-0.2960</td>
      <td>DaveBrazo1</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>28</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:46 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349773187506176</td>
      <td>1014349773187506176</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 1295378276, 'id_str': '1295378276', 'na...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>dodiyodoe3</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>29</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:46 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349773065908224</td>
      <td>1014349773065908224</td>
      <td>...</td>
      <td>realDonaldTrump</td>
      <td>False</td>
      <td>{'id': 221501984, 'id_str': '221501984', 'name...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>hestheman1</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>970</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:17 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349650722160640</td>
      <td>1014349650722160640</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 138809251, 'id_str': '138809251', 'name...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>LoveBGees</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>971</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:17 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349650336337921</td>
      <td>1014349650336337921</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 827951465926889472, 'id_str': '82795146...</td>
      <td>{'neg': 0.069, 'neu': 0.931, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.069</td>
      <td>0.931</td>
      <td>-0.1027</td>
      <td>oldladyofCT</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>972</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:16 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349646335021056</td>
      <td>1014349646335021056</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 968390186118807553, 'id_str': '96839018...</td>
      <td>{'neg': 0.059, 'neu': 0.788, 'pos': 0.153, 'co...</td>
      <td>0.153</td>
      <td>0.059</td>
      <td>0.788</td>
      <td>0.4404</td>
      <td>StelioLardas</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>973</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:14 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349641440219136</td>
      <td>1014349641440219136</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 812293412, 'id_str': '812293412', 'name...</td>
      <td>{'neg': 0.254, 'neu': 0.746, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.254</td>
      <td>0.746</td>
      <td>-0.7003</td>
      <td>cdanettewg</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>974</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:14 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349639925895169</td>
      <td>1014349639925895169</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 822567864259510272, 'id_str': '82256786...</td>
      <td>{'neg': 0.059, 'neu': 0.788, 'pos': 0.153, 'co...</td>
      <td>0.153</td>
      <td>0.059</td>
      <td>0.788</td>
      <td>0.4404</td>
      <td>tjbogart33</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>975</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:14 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349639431139333</td>
      <td>1014349639431139333</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 261956952, 'id_str': '261956952', 'name...</td>
      <td>{'neg': 0.11, 'neu': 0.637, 'pos': 0.253, 'com...</td>
      <td>0.253</td>
      <td>0.110</td>
      <td>0.637</td>
      <td>0.5209</td>
      <td>romancntdrkside</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>976</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:13 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349634821611520</td>
      <td>1014349634821611520</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 25757068, 'id_str': '25757068', 'name':...</td>
      <td>{'neg': 0.0, 'neu': 0.706, 'pos': 0.294, 'comp...</td>
      <td>0.294</td>
      <td>0.000</td>
      <td>0.706</td>
      <td>0.7574</td>
      <td>adavis1961</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>977</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:10 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349622087749632</td>
      <td>1014349622087749632</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 269386767, 'id_str': '269386767', 'name...</td>
      <td>{'neg': 0.142, 'neu': 0.608, 'pos': 0.25, 'com...</td>
      <td>0.250</td>
      <td>0.142</td>
      <td>0.608</td>
      <td>0.3818</td>
      <td>rovirosa2003</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>978</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:10 +0000 2018</td>
      <td>{'hashtags': [{'text': 'McConnellLies', 'indic...</td>
      <td>NaN</td>
      <td>2</td>
      <td>False</td>
      <td>None</td>
      <td>1014349622049828864</td>
      <td>1014349622049828864</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>True</td>
      <td>{'id': 301795932, 'id_str': '301795932', 'name...</td>
      <td>{'neg': 0.31, 'neu': 0.69, 'pos': 0.0, 'compou...</td>
      <td>0.000</td>
      <td>0.310</td>
      <td>0.690</td>
      <td>-0.7430</td>
      <td>vwheato</td>
      <td>[McConnellLies, WeSeeYouMitch]</td>
    </tr>
    <tr>
      <th>979</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:10 +0000 2018</td>
      <td>{'hashtags': [{'text': 'MSNBC', 'indices': [0,...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349621072617472</td>
      <td>1014349621072617472</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>True</td>
      <td>{'id': 22066415, 'id_str': '22066415', 'name':...</td>
      <td>{'neg': 0.109, 'neu': 0.891, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.109</td>
      <td>0.891</td>
      <td>-0.2960</td>
      <td>StCyrlyMe2</td>
      <td>[MSNBC, CNN, Trump, SCOTUS, Republicans]</td>
    </tr>
    <tr>
      <th>980</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:09 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349619860393984</td>
      <td>1014349619860393984</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 1367537113, 'id_str': '1367537113', 'na...</td>
      <td>{'neg': 0.059, 'neu': 0.788, 'pos': 0.153, 'co...</td>
      <td>0.153</td>
      <td>0.059</td>
      <td>0.788</td>
      <td>0.4404</td>
      <td>3XYMomRNMPH</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>981</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:09 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349618698735618</td>
      <td>1014349618698735618</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 25783616, 'id_str': '25783616', 'name':...</td>
      <td>{'neg': 0.211, 'neu': 0.789, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.211</td>
      <td>0.789</td>
      <td>-0.6124</td>
      <td>Jones_112</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>982</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:09 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349617109102598</td>
      <td>1014349617109102598</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 101810576, 'id_str': '101810576', 'name...</td>
      <td>{'neg': 0.345, 'neu': 0.655, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.345</td>
      <td>0.655</td>
      <td>-0.3875</td>
      <td>jrbaltmd57</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>983</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:06 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349607814549505</td>
      <td>1014349607814549505</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 66226854, 'id_str': '66226854', 'name':...</td>
      <td>{'neg': 0.059, 'neu': 0.788, 'pos': 0.153, 'co...</td>
      <td>0.153</td>
      <td>0.059</td>
      <td>0.788</td>
      <td>0.4404</td>
      <td>javamom66</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>984</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:06 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349605797007361</td>
      <td>1014349605797007361</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 999098286203195392, 'id_str': '99909828...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>ForeverSad10</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>985</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:05 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349600025542658</td>
      <td>1014349600025542658</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 45280709, 'id_str': '45280709', 'name':...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>pbriggsiam</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>986</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:04 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349597886615553</td>
      <td>1014349597886615553</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 85219527, 'id_str': '85219527', 'name':...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>renayws</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>987</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:04 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>{'media': [{'id': 1014349589527195649, 'id_str...</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349597236346881</td>
      <td>1014349597236346881</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 4327464854, 'id_str': '4327464854', 'na...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>DosEquis2xx</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>988</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:04 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349596460552193</td>
      <td>1014349596460552193</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 4790573594, 'id_str': '4790573594', 'na...</td>
      <td>{'neg': 0.059, 'neu': 0.788, 'pos': 0.153, 'co...</td>
      <td>0.153</td>
      <td>0.059</td>
      <td>0.788</td>
      <td>0.4404</td>
      <td>ByrdHeardIt</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>989</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:03 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349592933158912</td>
      <td>1014349592933158912</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 464867026, 'id_str': '464867026', 'name...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>StephanieBraith</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>990</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:01 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349587027394560</td>
      <td>1014349587027394560</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 1956801666, 'id_str': '1956801666', 'na...</td>
      <td>{'neg': 0.254, 'neu': 0.746, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.254</td>
      <td>0.746</td>
      <td>-0.7003</td>
      <td>AntiApathy</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>991</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:01 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349585563766785</td>
      <td>1014349585563766785</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 24200853, 'id_str': '24200853', 'name':...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>MGDriscoll</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>992</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:26:00 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349580106952705</td>
      <td>1014349580106952705</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>True</td>
      <td>{'id': 93041664, 'id_str': '93041664', 'name':...</td>
      <td>{'neg': 0.236, 'neu': 0.764, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.236</td>
      <td>0.764</td>
      <td>-0.7003</td>
      <td>brucewxyz</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>993</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:25:59 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349575765872642</td>
      <td>1014349575765872642</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 819694253777518592, 'id_str': '81969425...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>AnitaJan261954</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>994</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:25:59 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349575354630147</td>
      <td>1014349575354630147</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 815407646912040960, 'id_str': '81540764...</td>
      <td>{'neg': 0.254, 'neu': 0.746, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.254</td>
      <td>0.746</td>
      <td>-0.7003</td>
      <td>AowenAnnbjorg</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>995</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:25:57 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349569797259265</td>
      <td>1014349569797259265</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 833730693930811393, 'id_str': '83373069...</td>
      <td>{'neg': 0.059, 'neu': 0.788, 'pos': 0.153, 'co...</td>
      <td>0.153</td>
      <td>0.059</td>
      <td>0.788</td>
      <td>0.4404</td>
      <td>Martamendoza718</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>996</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:25:56 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349563526774784</td>
      <td>1014349563526774784</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 4459753935, 'id_str': '4459753935', 'na...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>JohnPena03</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>997</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:25:54 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349557310939136</td>
      <td>1014349557310939136</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 36434686, 'id_str': '36434686', 'name':...</td>
      <td>{'neg': 0.0, 'neu': 0.686, 'pos': 0.314, 'comp...</td>
      <td>0.314</td>
      <td>0.000</td>
      <td>0.686</td>
      <td>0.3164</td>
      <td>PittieBoo</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>998</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:25:54 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349557193420800</td>
      <td>1014349557193420800</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 707432781492699137, 'id_str': '70743278...</td>
      <td>{'neg': 0.254, 'neu': 0.746, 'pos': 0.0, 'comp...</td>
      <td>0.000</td>
      <td>0.254</td>
      <td>0.746</td>
      <td>-0.7003</td>
      <td>SheilaDecker19</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>999</th>
      <td>None</td>
      <td>None</td>
      <td>Wed Jul 04 03:25:53 +0000 2018</td>
      <td>{'hashtags': [{'text': 'inners', 'indices': [1...</td>
      <td>NaN</td>
      <td>0</td>
      <td>False</td>
      <td>None</td>
      <td>1014349553066233856</td>
      <td>1014349553066233856</td>
      <td>...</td>
      <td>MSNBC</td>
      <td>False</td>
      <td>{'id': 268571122, 'id_str': '268571122', 'name...</td>
      <td>{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>donnamcar</td>
      <td>[inners]</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 38 columns</p>
</div>




```python
df.iloc[0].user.get('screen_name')
```




    'RFBHD52'




```python
df.to_csv("Twitter Data.csv")
```

## James - code to produce the live graff of a changing status of Top Ten Users using API

Involves 2 components:
1) animation.py  that is run in terminal at the same time as the code in 
2) The_loop.jpynb

# animation.py 
def get_labels():
    file = open('labels.txt','r').read()
    list_names = file.split('\n')
    names = []

    for name in list_names:
        name = name.strip('@')
        names.append(name)  

    return names

def animate(i):

    names= get_labels()

    pullData = open("position_1.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_1 = []
    y_position_1 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_1.append(int(x))
            y_position_1.append(int(y))
    
    
    pullData = open("position_2.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_2 = []
    y_position_2 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_2.append(int(x))
            y_position_2.append(int(y))

    pullData = open("position_3.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_3 = []
    y_position_3 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_3.append(int(x))
            y_position_3.append(int(y))

    pullData = open("position_4.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_4 = []
    y_position_4 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_4.append(int(x))
            y_position_4.append(int(y))
            
    pullData = open("position_5.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_5 = []
    y_position_5 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_5.append(int(x))
            y_position_5.append(int(y))

    ax1.clear()
    
    ax1.plot(x_position_1,y_position_1,label=names[0])
    ax1.plot(x_position_2,y_position_2,label=names[1])
    ax1.plot(x_position_3,y_position_3,label=names[2])
    ax1.plot(x_position_4,y_position_4,label=names[3])
    ax1.plot(x_position_5,y_position_5,label=names[4])
    plt.legend(bbox_to_anchor=(0.2, 1), loc=2, borderaxespad=1)
    plt.xlabel('Time in Seconds',fontsize=16)
    plt.ylabel('# of Tweet Mentions / 20k ',fontsize=16)
    plt.title('A Tale of Twitter Mentions',fontsize=20,fontweight='bold')

names=[]
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ani = animation.FuncAnimation(fig, animate,interval=1000)


plt.show()


## The_loop.ipynb 


```python
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

```


```python
file = 'http://tweeplers.com/?cc=WORLD'

# 60 X 5minuts = 300 seconds
total_time = 21000
current_time = 20000
```


```python
while total_time>current_time:
    response = requests.get(file)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    image = soup.find_all('div',attrs={'class':'col-xs-2'})[0].a.img['src']
    names = soup.find_all('div', attrs={'class':'col-md-7'})
    tweets_per = soup.find_all('div', attrs={'class':'col-xs-2 col-md-2'})
    
    f=open("position_1.txt", "a+")
    f.write(str(current_time)+','+ tweets_per[0].text + "\n")
    f.close()
    
    f=open("position_2.txt", "a+")
    f.write(str(current_time)+','+ tweets_per[1].text + "\n")
    f.close()
    
    f=open("position_3.txt", "a+")
    f.write(str(current_time)+','+ tweets_per[2].text + "\n")
    f.close()
    
    f=open("position_4.txt", "a+")
    f.write(str(current_time)+','+ tweets_per[3].text + "\n")
    f.close()
    
    f=open("position_5.txt", "a+")
    f.write(str(current_time)+','+ tweets_per[4].text + "\n")
    f.close()
    current_time+=10
    
    open('labels.txt', 'w+')
    for i in range(10):
        f=open("labels.txt", "a+")
        f.write(names[i].text + "\n")
        f.close()
    
    time.sleep(10)
```

## Verna - code to obtain CAP and Meter ratings from Botometer using API

My original jupyter notebook to produce my work for the presentation included all of these cells.  
Several of these cells not needed to run the LIVE code during the presentation were extracted for the presentation, but are included here, along with the necessary preceding cells.
The static file that this produced was used in the presentation.


```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import  OffsetImage, AnnotationBbox
import pandas as pd
import numpy as np
import time
from PIL import Image
import requests
from io import BytesIO
import tweepy
import seaborn as sns
sns.set_style()

consumer_key = "xxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
app_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
app_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(app_key, app_secret)
#api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
```


```python
# Passed in from Zachary
# Top Names are the top_users that tweet the most
top_ten_names = ['realDonaldTrump',
 'BTS_twt',
 'England',
 'FoxNews',
 'YouTube',
 'narendramodi',
 'FIFAWorldCup',
 'HarryMaguire93',
 'msdhoni',
 'SeaveyDaniel']

# Data file
file = 'Twitter Data.csv'
df = pd.read_csv(file)
```


```python
# Selected columns for new shorter df of ALL Tweets at 10 users 
df_short = df[['top_user','Unnamed: 0','comp','pos','neu','neg','text','created_at','retweeted_status','user','id','user_created_at','statuses_count','favorites_count','user_screen_name','user_name','description','profile_url']].copy()
df_short['qty'] = 1*1
df_short['cap'] = 0*0
df_short['meter'] =0*0
df_short['boto_name'] = ""

#df_short.head()
```


```python
# Pull TRUMP RECORDS
trump_df = df_short.query('top_user == "realDonaldTrump"')
#trump_df.head()
```


```python
# BOTOMETER: lookup 'accounts' for meter value, cap value, and name check
accounts = trump_df['user_screen_name']
#accounts
```


```python
# BLOCKED OUT for PRESENTATION - 
# Retrieve 'BOT' RATINGS from the BOTOMETER WEBSITE 
# RECORD RETRIEVAL is about 1 RECORD per 4 SECONDS, and THERE is a USER LIMIT PER DAY
import botometer
# Authorizations:
mashape_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
twitter_app_auth = {
    'consumer_key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'consumer_secret': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'access_token': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'access_token_secret': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)
# Variables and get Botometer information
boto_name = []
caps = []
meter_score = []
count = 1*1
NaN = "NaN"
for screen_name, result in bom.check_accounts_in(accounts):
    try:
        print(count)
        print(screen_name)
        scrn_name = result['user']['screen_name'] # used for double checking
        boto_name.append(scrn_name)
        cap = result['cap']['english'] # Overall score %
        caps.append(cap)
        meter = result['display_scores']['english']
        meter_score.append(meter)
        count += 1
        print(caps)
        print(boto_name)
        print(meter_score)
        print("__________________________")
     
    except:
        print(count)
        count += 1
        print("Skipping due to error")
        boto_name.append(NaN)
        caps.append(NaN)
        meter_score.append(NaN)
        print("__________________________")
```


```python
# Hard code backup: cap values for presentation
# caps = [0.0020801266669107617, 0.31925820414416145, 0.07583235670880943, 0.0014828129117616376, 0.014543680863094452, 0.0022344951904619756, 0.0034565375041747688, 0.021603216955146855, 0.032183220269696264, 0.06706338835674493, 0.0012183789109573519, 0.028225552221050176, 0.007724054879521963, 0.07583235670880943, 0.00682617488477388, 0.0038317559975942547, 0.2564674002687074, 0.0060434470460022415, 0.011259346570646776, 0.00682617488477388, 0.004268306222830912, 0.014543680863094452, 0.15990913252190533, 0.08590409243653727, 0.0060434470460022415, 0.009922300094567935, 0.0012616932230026553, 0.22851217352302083, 0.0024124820419756166, 0.008750694009244317, 0.0038317559975942547, 0.002856940094612955, 0.0019457839054003979, 0.007724054879521963, 0.00682617488477388, 0.008750694009244317, 0.008750694009244317, 0.007724054879521963, 0.05272348371475359, 0.0026183131920431966, 0.5650534221025286, 0.02470203924309943, 0.032183220269696264, 0.008750694009244317, 0.004268306222830912, 0.14157391067567082, 0.5114515477139734, 0.004268306222830912, 0.0018284205282117316, 0.003134129284123964, 0.22851217352302083, 0.0016347149115980926, 0.008750694009244317, 0.05942480200270631, 0.0020801266669107617, 0.012788431177246198, 0.09741389119048932, 0.0013611897321404152, 0.007724054879521963, 0.0024124820419756166, 0.15990913252190533, 0.0016347149115980926, 0.00682617488477388, 0.007724054879521963, 0.046773782504080826, 0.04142512584947667, 0.0060434470460022415, 0.18036203754175442, 0.9446742630045359, 0.012788431177246198, 0.2564674002687074, 0.004268306222830912, 0.014543680863094452, 0.22851217352302083, 0.06706338835674493, 0.004775575529426348, 0.0024124820419756166, 0.0024124820419756166, 0.003134129284123964, 0.3528904417922491, 0.011259346570646776, 0.007724054879521963, 0.004775575529426348, 0.003134129284123964, 0.0038317559975942547, 0.05942480200270631, 0.0022344951904619756, 0.0024124820419756166, 0.31925820414416145, 0.004775575529426348, 0.0038317559975942547, 0.0038317559975942547, 0.0020801266669107617, 0.0013611897321404152, 0.018904416758651326, 0.0022344951904619756, 0.005363701003450149, 0.15990913252190533, 0.0020801266669107617, 0.021603216955146855, 0.5650534221025286, 0.0016347149115980926, 0.003134129284123964, 0.016566752245969804, 0.004268306222830912, 0.5114515477139734, 0.0060434470460022415, 0.11046376827194711, 0.03657805288858329, 0.0014187924969112314, 0.028225552221050176, 0.012788431177246198, 0.0024124820419756166, 0.0020801266669107617, 0.0024124820419756166, 0.00682617488477388, 0.0012183789109573519, 0.0015543510151536995, 0.28686866458066024, 0.02470203924309943, 0.004775575529426348, 0.002856940094612955, 0.12514574764971045, 0.004268306222830912, 0.004775575529426348, 0.00682617488477388, 0.011259346570646776, 0.021603216955146855, 0.003134129284123964, 0.05942480200270631, 0.14157391067567082, 0.18036203754175442, 0.0020801266669107617, 0.0019457839054003979, 0.5387761106184944, 0.14157391067567082, 0.011259346570646776, 0.0024124820419756166, 0.0060434470460022415, 0.0038317559975942547, 0.004268306222830912, 0.014543680863094452, 0.0020801266669107617, 0.003134129284123964, 0.03657805288858329, 0.05942480200270631, 0.04142512584947667, 0.004268306222830912, 0.046773782504080826, 0.20316525868115767, 0.004775575529426348, 0.018904416758651326, 0.004268306222830912, 0.28686866458066024, 0.0013611897321404152, 0.018904416758651326, 0.04142512584947667, 0.008750694009244317, 0.02470203924309943, 0.0022344951904619756, 0.31925820414416145, 0.07583235670880943, 0.012788431177246198, 0.0013611897321404152, 0.0015543510151536995, 0.011259346570646776, 0.0016347149115980926, 0.0034565375041747688, 0.06706338835674493, 0.002856940094612955, 0.007724054879521963, 0.016566752245969804, 0.0014828129117616376, 0.021603216955146855, 0.0019457839054003979, 0.14157391067567082, 0.0018284205282117316, 0.2564674002687074, 0.0038317559975942547, 0.05272348371475359, 0.0012616932230026553, 0.0038317559975942547, 0.003134129284123964, 0.0026183131920431966, 0.002856940094612955, 0.0019457839054003979, 0.014543680863094452, 0.028225552221050176, 0.0022344951904619756, 0.0014828129117616376, 'NaN', 0.008750694009244317, 0.0034565375041747688, 0.003134129284123964, 0.08590409243653727, 0.001309081196579327, 0.09741389119048932, 0.0013611897321404152, 0.003134129284123964, 0.04142512584947667, 0.003134129284123964, 0.003134129284123964, 0.003134129284123964, 0.0016347149115980926, 0.0034565375041747688, 0.0060434470460022415, 0.014543680863094452, 0.0015543510151536995, 0.0020801266669107617, 0.001725457650971877, 0.032183220269696264, 0.001725457650971877, 0.05942480200270631, 0.002856940094612955, 0.0019457839054003979, 0.05272348371475359, 0.0038317559975942547, 0.011259346570646776, 0.002856940094612955, 0.007724054879521963, 0.31925820414416145, 0.012788431177246198, 0.0019457839054003979, 0.0038317559975942547, 0.0038317559975942547, 0.001725457650971877, 0.14157391067567082, 0.011259346570646776, 0.008750694009244317, 0.04142512584947667, 0.012788431177246198, 0.007724054879521963, 0.005363701003450149, 0.021603216955146855, 0.004775575529426348, 0.0026183131920431966, 0.014543680863094452, 0.014543680863094452, 0.0026183131920431966, 0.028225552221050176, 0.0019457839054003979, 0.005363701003450149, 0.008750694009244317, 0.012788431177246198, 0.018904416758651326, 0.22851217352302083, 0.021603216955146855, 0.0038317559975942547, 0.12514574764971045, 0.007724054879521963, 0.009922300094567935, 0.0020801266669107617, 0.003134129284123964, 0.003134129284123964, 0.032183220269696264, 0.0034565375041747688, 0.011259346570646776, 0.20316525868115767, 0.0014187924969112314, 0.0011785984309163565, 0.0024124820419756166, 0.014543680863094452, 0.0038317559975942547, 0.0060434470460022415, 0.001725457650971877, 0.014543680863094452, 0.04142512584947667, 0.007724054879521963, 0.05272348371475359, 0.011259346570646776, 0.0012183789109573519, 0.12514574764971045, 0.0038317559975942547, 0.016566752245969804, 0.012788431177246198, 0.0060434470460022415, 0.3868425932473016, 0.007724054879521963, 0.014543680863094452, 0.0022344951904619756, 0.0014828129117616376, 0.04142512584947667, 0.08590409243653727, 0.0038317559975942547, 0.014543680863094452, 0.02470203924309943, 0.0026183131920431966, 0.002856940094612955, 0.0060434470460022415, 0.046773782504080826, 0.0060434470460022415, 0.12514574764971045, 0.09741389119048932, 0.04142512584947667, 0.8469348665516686, 0.002856940094612955, 0.018904416758651326, 0.0013611897321404152, 0.2564674002687074, 0.0022344951904619756, 0.005363701003450149, 0.0019457839054003979, 0.009922300094567935, 0.0020801266669107617, 0.005363701003450149, 0.001725457650971877, 0.007724054879521963, 0.0038317559975942547, 0.011259346570646776, 0.002856940094612955, 0.11046376827194711, 0.0022344951904619756, 0.20316525868115767, 0.005363701003450149, 0.011259346570646776, 0.002856940094612955, 0.032183220269696264, 0.0038317559975942547, 0.001309081196579327, 0.007724054879521963, 0.003134129284123964, 0.0060434470460022415, 0.003134129284123964, 0.002856940094612955, 0.005363701003450149, 0.004775575529426348, 0.0038317559975942547, 0.0014828129117616376, 0.0015543510151536995, 0.0038317559975942547, 0.011259346570646776, 0.0020801266669107617, 0.005363701003450149, 0.5650534221025286, 0.005363701003450149, 0.014543680863094452, 0.0034565375041747688, 0.0016347149115980926, 0.00682617488477388, 0.001725457650971877, 0.011259346570646776, 0.0022344951904619756, 0.011259346570646776, 0.0060434470460022415, 0.0022344951904619756, 0.06706338835674493, 0.31925820414416145, 0.002856940094612955, 0.28686866458066024, 0.003134129284123964, 0.0022344951904619756, 0.012788431177246198, 0.15990913252190533, 0.009922300094567935, 0.004268306222830912, 0.001725457650971877, 0.014543680863094452, 0.016566752245969804, 0.012788431177246198, 0.0019457839054003979, 0.0022344951904619756, 0.021603216955146855, 0.04142512584947667, 0.03657805288858329, 0.03657805288858329, 0.004268306222830912, 0.14157391067567082, 0.009922300094567935, 0.00682617488477388, 0.0034565375041747688, 0.04142512584947667, 0.046773782504080826, 0.004775575529426348, 0.0014828129117616376, 0.001725457650971877, 0.18036203754175442, 0.14157391067567082, 0.007724054879521963, 0.003134129284123964, 0.05942480200270631, 0.0013611897321404152, 0.0024124820419756166, 0.0034565375041747688, 0.001725457650971877, 0.0016347149115980926, 0.11046376827194711, 0.05272348371475359, 0.001725457650971877, 0.0019457839054003979, 0.0018284205282117316, 0.5906777151076118, 0.0016347149115980926, 0.48270052072345504, 0.00682617488477388, 0.20316525868115767, 0.012788431177246198, 0.0024124820419756166, 0.09741389119048932, 0.012788431177246198, 0.06706338835674493, 0.003134129284123964, 0.016566752245969804, 0.016566752245969804, 0.0034565375041747688, 0.028225552221050176, 0.06706338835674493, 0.5114515477139734, 0.0014828129117616376, 0.004775575529426348, 0.0015543510151536995, 0.00682617488477388, 0.011259346570646776, 0.009922300094567935, 0.02470203924309943, 0.0038317559975942547, 0.005363701003450149, 0.014543680863094452, 0.009922300094567935, 0.0038317559975942547, 0.016566752245969804, 0.0022344951904619756, 0.00682617488477388, 0.07583235670880943, 0.012788431177246198, 0.42020504633925215, 0.0019457839054003979, 0.003134129284123964, 0.009922300094567935, 0.09741389119048932, 0.0034565375041747688, 0.0014828129117616376, 0.04142512584947667, 0.0014187924969112314, 0.0016347149115980926, 0.005363701003450149, 0.009922300094567935, 0.001309081196579327, 0.0022344951904619756, 0.0018284205282117316, 0.012788431177246198, 0.0024124820419756166, 0.05272348371475359, 0.004775575529426348, 0.046773782504080826, 0.046773782504080826, 0.007724054879521963, 0.0024124820419756166, 0.04142512584947667, 0.0060434470460022415, 0.012788431177246198, 0.0038317559975942547, 0.0022344951904619756, 0.016566752245969804, 0.004268306222830912, 0.018904416758651326, 0.008750694009244317, 0.003134129284123964, 0.0014828129117616376, 0.0034565375041747688, 0.004775575529426348, 0.002856940094612955, 0.0038317559975942547, 0.0038317559975942547, 0.0012183789109573519, 0.45227900229523627, 0.0026183131920431966, 0.0060434470460022415, 0.05272348371475359, 0.11046376827194711, 0.0024124820419756166, 0.032183220269696264, 0.004268306222830912, 0.0060434470460022415, 0.5387761106184944, 0.02470203924309943, 0.03657805288858329, 0.03657805288858329, 0.0014187924969112314, 0.5387761106184944, 0.0022344951904619756, 0.0013611897321404152, 0.011259346570646776, 0.001309081196579327, 0.009922300094567935, 0.0024124820419756166, 0.02470203924309943, 0.0034565375041747688, 0.0060434470460022415, 0.0016347149115980926, 0.02470203924309943, 0.003134129284123964, 0.18036203754175442, 0.14157391067567082, 0.001725457650971877, 0.0022344951904619756, 0.0015543510151536995, 0.0019457839054003979, 0.6913231693056707, 0.0026183131920431966, 0.004268306222830912]
 trump_df['cap'] = caps
```


```python
# Hard code backup: meter_score for presenation
# meter_score = [0.3, 3.5, 2.3, 0.2, 1.1, 0.3, 0.5, 1.3, 1.6, 2.2, 0.1, 1.5, 0.8, 2.3, 0.7, 0.5, 3.3, 0.7, 1.0, 0.7, 0.5, 1.1, 3.0, 2.4, 0.7, 0.9, 0.1, 3.3, 0.3, 0.8, 0.5, 0.4, 0.3, 0.8, 0.7, 0.8, 0.8, 0.8, 2.0, 0.4, 4.1, 1.4, 1.6, 0.8, 0.5, 2.8, 4.0, 0.5, 0.2, 0.4, 3.3, 0.2, 0.8, 2.1, 0.3, 1.0, 2.5, 0.2, 0.8, 0.3, 3.0, 0.2, 0.7, 0.8, 1.9, 1.8, 0.7, 3.1, 4.8, 1.0, 3.3, 0.5, 1.1, 3.3, 2.2, 0.6, 0.3, 0.3, 0.4, 3.6, 1.0, 0.8, 0.6, 0.4, 0.5, 2.1, 0.3, 0.3, 3.5, 0.6, 0.5, 0.5, 0.3, 0.2, 1.3, 0.3, 0.6, 3.0, 0.3, 1.3, 4.1, 0.2, 0.4, 1.2, 0.5, 4.0, 0.7, 2.6, 1.7, 0.2, 1.5, 1.0, 0.3, 0.3, 0.3, 0.7, 0.1, 0.2, 3.4, 1.4, 0.6, 0.4, 2.7, 0.5, 0.6, 0.7, 1.0, 1.3, 0.4, 2.1, 2.8, 3.1, 0.3, 0.3, 4.1, 2.8, 1.0, 0.3, 0.7, 0.5, 0.5, 1.1, 0.3, 0.4, 1.7, 2.1, 1.8, 0.5, 1.9, 3.2, 0.6, 1.3, 0.5, 3.4, 0.2, 1.3, 1.8, 0.8, 1.4, 0.3, 3.5, 2.3, 1.0, 0.2, 0.2, 1.0, 0.2, 0.5, 2.2, 0.4, 0.8, 1.2, 0.2, 1.3, 0.3, 2.8, 0.2, 3.3, 0.5, 2.0, 0.1, 0.5, 0.4, 0.4, 0.4, 0.3, 1.1, 1.5, 0.3, 0.2, 'NaN', 0.8, 0.5, 0.4, 2.4, 0.1, 2.5, 0.2, 0.4, 1.8, 0.4, 0.4, 0.4, 0.2, 0.5, 0.7, 1.1, 0.2, 0.3, 0.2, 1.6, 0.2, 2.1, 0.4, 0.3, 2.0, 0.5, 1.0, 0.4, 0.8, 3.5, 1.0, 0.3, 0.5, 0.5, 0.2, 2.8, 1.0, 0.8, 1.8, 1.0, 0.8, 0.6, 1.3, 0.6, 0.4, 1.1, 1.1, 0.4, 1.5, 0.3, 0.6, 0.8, 1.0, 1.3, 3.3, 1.3, 0.5, 2.7, 0.8, 0.9, 0.3, 0.4, 0.4, 1.6, 0.5, 1.0, 3.2, 0.2, 0.1, 0.3, 1.1, 0.5, 0.7, 0.2, 1.1, 1.8, 0.8, 2.0, 1.0, 0.1, 2.7, 0.5, 1.2, 1.0, 0.7, 3.7, 0.8, 1.1, 0.3, 0.2, 1.8, 2.4, 0.5, 1.1, 1.4, 0.4, 0.4, 0.7, 1.9, 0.7, 2.7, 2.5, 1.8, 4.6, 0.4, 1.3, 0.2, 3.3, 0.3, 0.6, 0.3, 0.9, 0.3, 0.6, 0.2, 0.8, 0.5, 1.0, 0.4, 2.6, 0.3, 3.2, 0.6, 1.0, 0.4, 1.6, 0.5, 0.1, 0.8, 0.4, 0.7, 0.4, 0.4, 0.6, 0.6, 0.5, 0.2, 0.2, 0.5, 1.0, 0.3, 0.6, 4.1, 0.6, 1.1, 0.5, 0.2, 0.7, 0.2, 1.0, 0.3, 1.0, 0.7, 0.3, 2.2, 3.5, 0.4, 3.4, 0.4, 0.3, 1.0, 3.0, 0.9, 0.5, 0.2, 1.1, 1.2, 1.0, 0.3, 0.3, 1.3, 1.8, 1.7, 1.7, 0.5, 2.8, 0.9, 0.7, 0.5, 1.8, 1.9, 0.6, 0.2, 0.2, 3.1, 2.8, 0.8, 0.4, 2.1, 0.2, 0.3, 0.5, 0.2, 0.2, 2.6, 2.0, 0.2, 0.3, 0.2, 4.2, 0.2, 3.9, 0.7, 3.2, 1.0, 0.3, 2.5, 1.0, 2.2, 0.4, 1.2, 1.2, 0.5, 1.5, 2.2, 4.0, 0.2, 0.6, 0.2, 0.7, 1.0, 0.9, 1.4, 0.5, 0.6, 1.1, 0.9, 0.5, 1.2, 0.3, 0.7, 2.3, 1.0, 3.8, 0.3, 0.4, 0.9, 2.5, 0.5, 0.2, 1.8, 0.2, 0.2, 0.6, 0.9, 0.1, 0.3, 0.2, 1.0, 0.3, 2.0, 0.6, 1.9, 1.9, 0.8, 0.3, 1.8, 0.7, 1.0, 0.5, 0.3, 1.2, 0.5, 1.3, 0.8, 0.4, 0.2, 0.5, 0.6, 0.4, 0.5, 0.5, 0.1, 3.9, 0.4, 0.7, 2.0, 2.6, 0.3, 1.6, 0.5, 0.7, 4.1, 1.4, 1.7, 1.7, 0.2, 4.1, 0.3, 0.2, 1.0, 0.1, 0.9, 0.3, 1.4, 0.5, 0.7, 0.2, 1.4, 0.4, 3.1, 2.8, 0.2, 0.3, 0.2, 0.3, 4.4, 0.4, 0.5]
trump_df['meter'] = meter_score
```


```python
# Hard code backup: boto_name for presentation
# boto_name = ['frenfer123', 'SandyMa92949039', 'Neverdemagain2', 'sam_tennant12', 'PaysonMelissa', 'mrrin213', 'bearharrumph', 'AnnetteMaillet3', 'mgtythor', 'AlexWal1980', '_Ericccccc', 'Bluesman57', 'ladamsrib', 'JodyC27', 'THATjonballard', 'lturner3108', 'LaredoAL', 'fancyfrog1337', 'GreatThee', 'izunoeigorou', 'jusfow', 'spandabelike', 'BencomoGail', 'oneHigginsDavid', 'squashzilla', 'kneesee79', 'Studio9Glen', 'DontMockMyTypos', 'kastlbend', 'myhappylife2020', 'Stupidosaur', 'DavidHumanzee', 'ktpasa', 'Rebashoenfelt1', 'valkyrie_hanna', 'theresa_brown50', 'Trupik127', 'dellacurran1', 'freddiechurro13', 'Smartiecats', 'raoul0430', 'jitendersoni133', 'kimmy52216977', 'raylene_resists', 'thomashourigan1', 'IAMParatiSi', 'PhyllisCowan', 'sunbeltengines', 'UnerasedUniv6', 'schachin', 'rav1960', 'RedVinesRedWine', 'dmacdonald1966', '5b20be6386164f8', 'GDawgForever', 'jjfaux82', 'scholt7', 'philtheswo', 'proudveteran63', 'wilburmeinen', 'Jaypeah', 'NishaNishimoto', 'Spiritof1773', 'cheetofacts', 'nygye', 'CharMac50', 'RojelioD', 'MCarolaNunez', 't3D45FwOb5kRKwy', 'mzzgotti1', 'DontMockMyTypos', 'bjdrues', 'Hereand66987608', 'VijayAr21020032', 'JamesABryant8', 'annmlee1', 'GillMark1709', 'JohnWayneLegend', 'GeenaJagger', 'mcivkr', 'JimmyStreich', 'nowaygirltv', 'Angelrubyring', 'joecarruba', 'ANN13951880', 'SJMoore64', 'Cunneenmachine', 'amuzme420', 'AnnaApp91838450', 'hobitcumasi', 'nicosat', 'BeulahTamborel1', 'FriendsofUKIPLl', 'Notorious_ZEB', 'ByroadsChelsie', 'buffalo_girl', 'kafd214', 'BencomoGail', 'sheadyacres', 'LANURSE1', 'Kaleesa6', 'laura_garvock', 'palomacreative', 'dmduffy6666', 'SammieGirlRSD', 'TrumpTrainMRA4', 'judemgreen', '72washington', 'richrake', 'lindyk20', 'hayne7', 'chilepeppermama', 'lorenzoVon38', 'debjensen360', 'tootame', 'spennington33', 'TexasPharmD', 'JordanGranados', '32jim2', 'crzymom110', 'DrMcKuKu', 'h2oswmn', 'Hitofan', 'yiayia62847', 'tcjepson', 'sperrin20', 'lizbethklein', 'Haytham_MG', 'RandyBMan', 'rhonda_harbison', 'cAlabaZa04901Je', 'sharonjlake', 'tomchappell', 'VioletAndSilver', 'USAloveGOD', 'RonCunningham', 'lovetreeskk', 'LDBPNV', 'BradParker_', 'booksbygin50', 'Sheamous89', 'divot1040', 'Its_All_Taken', 'jerimickelberry', 'EliseGr02404357', '5b20be6386164f8', 'D_Mass', 'spetersaz', 'mlogeman', 'LeeCapobianco1', 'JamesAr19476462', 'batliner_julia', 'rocktalkbox', 'JamesWa55188246', 'CPTDisgruntled', 'lunargranny', 'xbz2017', 'Happy01686651', 'PNewmanBennett', 'jeff14mail', 'Jan2Kole', 'chipolitics', 'Robbyusee', 'Reneeb4327', 'ckcrider', 'robert_sicario', 'Birdboy1981', 'prairie0597', 'Kupi_Zak', 'lttlgreenish', 'TerraGravity', 'Photog_NateHart', 'yungefdabean', 'Dangermmm', 'Taffy_Tart', 'duckman511', 'jeancunningham2', 'niksnook57', 'TiffanieMarcum', 'AileenMoffatt', 'Barbara_AOK', 'SexBanJohn', 'PSP7530', 'wtryonjr', 'OSGdirector', 'mamacross03', 'RobertWorthley', 'retvantq1', 'KellyKnor', 'SanduzzoPSL', 'NaN', 'Del56', 'AprilGreen93', 'billhenwood', 'DJBurn77', 'Coverciae_731', 'midwestcher', 'angelauk1900', 'DebraFletcher17', 'xbz2017', 'emilialuxa', 'BlueLn91', 'Grace4NY', 'Raqib_Ali_', 'DSoonerborn', 'AZHotTopics', 'LBarto_1952', 'Borgy_1978', 'Goofydad', 'bebemariiee', 'jojokejohn', 'NIAbbot', 'IcyBrown3', 'shara76', 'BarryOCommunist', 'sherluck_h', 'SpudLovr', 'Squiddlle', 'justwongirl', 'pamo6107', 'LeighAnnStewar8', 'Halabutt1', 'welldoneAI', 'grayjonv', 'ZagCsik', 'kalia273', 'Donna53217165', 'perrypines', 'PuniTenshu', 'xbz2017', 'LMagurck', 'GLSCHWALL', 'friest_len', 'scarlett_0hara', 'SharonCoryell3', 'NoToTheRight', 'patty_hawthorne', 'EmeldaA4', 'Pete4709', 'PickleJar10', 'SusiBV', 'dnj732', 'Citlaivi', 'mayrasons2', 'michaelsaint13', 'Patriot_Mom_17', 'MarletJones', 'meherrn', 'PradRachael', 'Kali_Wolf_888', 'Melissa53611', 'QeyeTDogbytes', 'Max96244404', 'KipHarris11', 'PatriotSally', 'TJFrazier006', 'Roger68376925', 'Winshield20', 'Kimma_S', 'idoseerussia', 'RetireNluvIT', 'LBarto_1952', 'Wilson1Theresa', 'VisibleSocSci', 'Oooooo_Donna', 'PlattWannabe', 'CarmineZozzora', 'pamo6107', 'MartinPujdak', 'NMartel54', 'darwinwoodka', 'sapayne8', 'Uniteusall12', 'Photog_NateHart', 'NottaTrolla', 'GadflyQuebec', 'di_plora', 'jimmythegote', 'Idryvfast', 'tr_williams', 'corinna_1981', 'xbz2017', 'DJBurn77', 'ANN13951880', 'JanetLe29397084', 'PNewmanBennett', 'coolncalm3', 'inertaliens', 'MountainRancher', 'lindseyforeal', 'RohanPinto', 'patsy_lee_green', 'scholt7', 'thegeekdudez', 'CERAP_Paris', 'Cynical_turd', 'andrefisher5931', 'MatthewK33', 'RebeccaSprunger', 'JosephRZarba', 'bonafideartist', 'Biggccman', 'Pell48', 'USHwy34', 'PamelaStovall6', 'DonnaCo4567890', 'pamo6107', 'PlinkinPatriot', 'ShenoahAlways', 'shottydread22', 'conservmia', 'rockinrobintwts', 'LeeCapobianco1', 'TerminalCreache', 'CozmoLizard', 'Mikeymgm1701', 'smc752', 'rcrlc8721', 'grrrr72', 'luisyahdiel3', 'resist_detroit1', 'RoscoeSauza', 'joecarruba', 'Tina51105580', 'LoveForAll24', 'irispraytan', 'GolasKathleen', 'fas1242', 'tweetflex', 'KarlSwain10', 'usageb170', 'mwh52', 'johndowe49', 'Luisraos', 'annetonie', 'EmeldaA4', 'loria_dawson', 'lonjets', 'sperrin20', 'Eloriel', 'alainmarle', 'classynogin', 'perrypines', 'LisaLew64739529', 'mutex7', 'thetheresac', 'di_plora', 'JJH789', 'VasilyAbogado', 'ERGA497511', 'eraofmoon', 'LMagurck', 'ravena68', 'leecobbonbass', 'JaksMimi', 'CPaRhon', 'StephenPetters6', 'Riponite', 'Star8400CPD', 'mellian1', 'mellymagscopy17', 'VoteTrumpPence7', 'kaseyredus', 'peanuts152', 'Stephen25719292', 'CarolFischbach1', 'NanaDavis_46', 'tomrichardson1', 'Serena_Jor', 'jasmine62246739', 'EddieDonovan', 'CarelockTim', 'kimcook49790981', 'ajfleming81', 'WellsIAm', 'littletujunga1', 'saurabhprasad', 'pamo6107', 'Retired_Now', 'Murphy931339211', 'VCurrentAffairs', 'PortableRockArt', 'save_democracy', 'mr_dsantos', 'vcntekbs', 'TPCLJ', 'Truth2Dj', 'alexroupakia', 'MarcusLDoss', 'beegSF', 'menares1945', 'mdsnkm', 'HerbertLubitz', 'Refracting', 'odecanha', 'JonieJesus1st', 'margo94', 'manzanares_ron', 'EmeldaA4', 'FlyFishingChef', 'mik84256067', 'jamielynn_xx', 'DavidRuch2', 'MsCjay', 'RomneyJudith', 'BigFish3000', 'superyayadize', 'Thee_Johnny', 'bakerbyaccident', 'Pattysanchez95', 'BBallBitchin', 'Gmanc95Castillo', 'BarbaraDadam', 'TigressLilly1', 'not6016', 'inspectorplanet', 'BryanSnow3', 'PatrioticKK', 'TeamB21919030', 'jacquesmanya', 'jnotestein', 'JanetPageHill', '034Davidhv1', 'MinaSuki143', 'Rambling_Lady', 'JanetF862258', 'mtlaurelbarb', 'bugg_ray', 'KimRoberts316', 'SOCJUSTICEDEATH', 'yungefdabean', 'InforAlemany', 'csatennis', 'jameslatoff', '21sunshine64', 'StubobNumbersAR', 'beharu', 'katemccloudsays', 'EddieH63', 'CareyJo95846484', 'TheSpeaker2012', 'SmokeyMtnStrong', 'hobitcumasi', 'TJSeraphim', 'it_middle', 'pamo6107', 'chocolatMILF', 'sccrgirl1718', 'squashzilla', 'RealBuzMartin', 'curmudgeon_girl', 'chandlertroyd', 'dekelley14', 'ForeverTepsMom', 'ChristinaZacker', 'dmacdonald1966', 'Jmacliberty', 'bbuddhas', 'MalcolmFarley', 'BaileyBono', 'joejacksonlive', 'whogotlaptop', 'ANN13951880', 'Nimasema', 'b918fvc', 'JamesRusselforc', 'OurbabyMinx', 'spanglesvi', 'scholt7', 'chelhidden', 'CarolineGasper1', 'texor2012', 'keyzpleez', 'MusingCat2014', 'scarlett_0hara', 'cheezwitham', 'farr_mimi', 'wandaransom', 'USAloveGOD', 'Unexpectedactiv', 'HeelStCloud', 'lynecarr', 'BBunjaporte_15', 'MAGAToday1', 'Rewind_Design', 'slaten_lora', 'Reader_14001', 'Lise_Borsum', 'RevDavidPSmith', 'WI4Palin', 'dansturn_views', 'timmy_rev', 'BerriePelser', 'DiXiEjO68', 'donaldrickert', 'StephanieSidley', 'RHeightsFinest', 'mandymendez90', 'Dougy_Hamilton', 'spetersaz']
trump_df['boto_name'] = boto_name
```


```python
#For PRESENTATION, read in prepared csv file in lines below (each record in the botometer takes 4 seconds to process)
trump_df.to_csv('trump_df.csv')

# NOTE:  if this file fails, the data is already created and hardcoded as backup, and will run

# Presentation Data file substitution for static data with added API information from Botometer
#file = 'trump_df.csv'
#trump_df = pd.read_csv(file)
#trump_df = pd.read_csv(file, parse_dates=['created_at'])
#trump_df.shape
```


```python
# For PRESENTATION, remove bad data (already accounted for in regular coding)
trump_df.dropna(subset=['meter','cap','boto_name'], inplace=True)
trump_df = trump_df.reset_index()
# trump_df.shape
```

## Code to produce the arched meter in the Spoof 

### This code was found on a search and I adapted it to produce the figure for the spoof.


```python
import matplotlib.pyplot as plt
from matplotlib import cm, gridspec
import numpy as np
import math
#import seaborn as sns
#sns.set_style()
from PIL import Image
from mpl_toolkits.axes_grid1 import make_axes_locatable
 
# set your color array and name of figure here:
dial_colors = np.linspace(0,1,1000) # using linspace here as an example
figname = 'myDial'
#sns.set_style(‘darkgrid’, {‘axes.facecolor’: ‘.4’}) 

meter = 4.5
factored = meter*200
arrow_index = factored
 
# create labels at desired locations
# note that the pie plot ploots from right to left
labels = [' ']*len(dial_colors)*2
labels[25] = '5'
labels[250] = '3.75'
labels[500] = '2.5'
labels[750] = '1.25'
labels[975] = '0'
 
# function plotting a colored dial
def dial(color_array, arrow_index, labels, ax):
    # Create bins to plot (equally sized)
    size_of_groups=np.ones(len(color_array)*2)
 
    # Create a pieplot, half white, half colored by your color array
    white_half = np.ones(len(color_array))*.5
    color_half = color_array
    color_pallet = np.concatenate([color_half, white_half])
 
    cs=cm.RdYlBu(color_pallet)
    pie_wedge_collection = ax.pie(size_of_groups, colors=cs, labels=labels)
 
    i=0
    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor(cm.RdYlBu(color_pallet[i]))
        i=i+1
 
    # create a white circle to make the pie chart a dial
    my_circle=plt.Circle( (0,0), 0.3, color='white')
    ax.add_artist(my_circle)
 
    # create the arrow, pointing at specified index
    arrow_angle = (arrow_index/float(len(color_array)))*3.14159
    arrow_x = 0.2*math.cos(arrow_angle)
    arrow_y = 0.2*math.sin(arrow_angle)
    ax.arrow(0,0,-arrow_x,arrow_y, width=.02, head_width=.07, \
        head_length=.1, fc='k', ec='k')
 
# create figure and specify figure name
fig, ax = plt.subplots()
 
# make dial plot and save figure
dial(dial_colors, arrow_index, labels, ax)
ax.set_aspect('equal')


plt.savefig(figname + '.png') 
 
# create a figure for the colorbar (crop so only colorbar is saved)
#fig, ax2 = plt.subplots()
cmap = cm.ScalarMappable(cmap='RdYlBu')
cmap.set_array([min(dial_colors), max(dial_colors)])

plt.savefig('cbar.png')
cbar = Image.open('cbar.png')

c_width, c_height = cbar.size
cbar = cbar.crop((0, .8*c_height, c_width, c_height)).save('cbar.png')
 
# open figure and crop bottom half
im = Image.open(figname + '.png')
width, height = im.size
 
# crop bottom half of figure
im = im.crop((0, 0, width+c_width, int(height/2.0))).save(figname + '.png')


```


```python
im = Image.open(figname +'.png')
print(figname)
im

```

    myDial





![png](output_31_1.png)


