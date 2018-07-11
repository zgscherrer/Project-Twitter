

```python
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import time
from datetime import datetime
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from dateutil import parser

from PIL import Image
from io import BytesIO
sns.set_style()
from matplotlib.offsetbox import  OffsetImage, AnnotationBbox
```


```python
twitter_data_csv = "/Users/ZGS/Documents/Data_Bootcamp/Project-Twitter/Resources/Twitter_Data.csv"
df = pd.read_csv(twitter_data_csv)
df.head()
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
      <th>Unnamed: 0</th>
      <th>contributors</th>
      <th>coordinates</th>
      <th>created_at</th>
      <th>entities</th>
      <th>extended_entities</th>
      <th>favorite_count</th>
      <th>favorited</th>
      <th>geo</th>
      <th>id</th>
      <th>...</th>
      <th>statuses_count</th>
      <th>user_created_at</th>
      <th>verified</th>
      <th>user_name</th>
      <th>description</th>
      <th>followers_count</th>
      <th>listed</th>
      <th>favorites_count</th>
      <th>notifications</th>
      <th>following</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:21 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>47785.0</td>
      <td>Fri Apr 17 15:45:33 +0000 2009</td>
      <td>False</td>
      <td>frances renfer 1959</td>
      <td>I am a retired middle school art teacher - Tau...</td>
      <td>350.0</td>
      <td>NaN</td>
      <td>15153.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>2680.0</td>
      <td>Fri Dec 01 15:53:47 +0000 2017</td>
      <td>False</td>
      <td>wicked smaht patriot</td>
      <td>Quietly watching. Sending love .++++++++</td>
      <td>539.0</td>
      <td>NaN</td>
      <td>17028.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>8921.0</td>
      <td>Mon Apr 23 21:54:10 +0000 2018</td>
      <td>False</td>
      <td>Never Dem Again</td>
      <td>#Trump2020...#KAG...#NoTrollZone #blocked...Ob...</td>
      <td>1802.0</td>
      <td>NaN</td>
      <td>4787.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>804.0</td>
      <td>Wed Feb 25 17:47:05 +0000 2015</td>
      <td>False</td>
      <td>Sam Tennant</td>
      <td>así es la vida—UNC ‘22</td>
      <td>327.0</td>
      <td>NaN</td>
      <td>14826.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>111944.0</td>
      <td>Mon Oct 17 20:17:41 +0000 2016</td>
      <td>False</td>
      <td>and justice for all</td>
      <td>Pillar of Patience, G-MA, Forever Yankee Fan, ...</td>
      <td>677.0</td>
      <td>NaN</td>
      <td>121203.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 54 columns</p>
</div>




```python
top_names = ['realDonaldTrump',
 'BTS_twt',
 'England',
 'FoxNews',
 'YouTube',
 'narendramodi',
 'FIFAWorldCup',
 'HarryMaguire93',
 'msdhoni',
 'SeaveyDaniel']
```


```python
avg_by_source=df.groupby("top_user")["comp"].mean()
avg_by_source
```




    top_user
    BTS_twt            0.141166
    England            0.259368
    FIFAWorldCup       0.206215
    FoxNews           -0.069758
    HarryMaguire93     0.150803
    SeaveyDaniel       0.302205
    YouTube            0.060363
    msdhoni            0.603918
    narendramodi       0.081166
    realDonaldTrump   -0.074072
    Name: comp, dtype: float64




```python
x_axis = np.arange(len(avg_by_source))
xlabels = avg_by_source.index
count = 0
for sentiment in avg_by_source:
    plt.text(count, sentiment+.01, str(round(sentiment,2)))
    count = count + 1

plt.bar(x_axis, avg_by_source,
        tick_label = xlabels,
        align='center',
        color = ['lightskyblue', 'green', 'red', 'blue', 'yellow', 'purple','brown','orange','gray','aqua'])
plt.gcf().set_size_inches(18, 12)
plt.grid()
plt.axhline(0, color='k')
plt.title("Overall Sentiment of Trending Users (%s)" % (time.strftime("%m/%d/%Y")),fontweight='bold',fontsize=20)
plt.xlabel("Trending User", fontweight='bold', fontsize=16)
plt.ylabel("Overall Polarity", fontweight='bold', fontsize=16)
plt.xticks(rotation='vertical', fontsize = 16)
plt.savefig("Overall Sentiment Trending Users.png")
plt.show()
```


![png](output_4_0.png)



```python
#Plot in seaborn based on compound sentiment
ax = sns.lmplot("tweet_count", "comp", data=df, hue='top_user', fit_reg=False, size=8,aspect=1.3,
               legend_out=True)

sns.set_style('darkgrid', {'axes.facecolor': '.4'})
plt.title("Sentiment of Trending Users (%s)" % (time.strftime("%m/%d/%Y")),fontweight='bold',fontsize=20)
plt.xlabel("Total Tweets", fontweight='bold', fontsize=16)
plt.ylabel("Tweet Sentiment", fontweight='bold', fontsize=16)
#invert the x axis
plt.gcf().set_size_inches(18, 12)
plt.gca().invert_xaxis()
plt.xticks(fontsize =14)
plt.grid()
plt.savefig("Sentiment_Analysis.png")

plt.show()
```


![png](output_5_0.png)



```python
dfwordcloud = df.copy()
#dfwordcloud.drop(dfwordcloud.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,]], axis=1, inplace=True)
dfwordcloud.drop(dfwordcloud.index[3337], inplace=True)
```


```python
dfwordcloud
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
      <th>Unnamed: 0</th>
      <th>contributors</th>
      <th>coordinates</th>
      <th>created_at</th>
      <th>entities</th>
      <th>extended_entities</th>
      <th>favorite_count</th>
      <th>favorited</th>
      <th>geo</th>
      <th>id</th>
      <th>...</th>
      <th>statuses_count</th>
      <th>user_created_at</th>
      <th>verified</th>
      <th>user_name</th>
      <th>description</th>
      <th>followers_count</th>
      <th>listed</th>
      <th>favorites_count</th>
      <th>notifications</th>
      <th>following</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:21 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>47785.0</td>
      <td>Fri Apr 17 15:45:33 +0000 2009</td>
      <td>False</td>
      <td>frances renfer 1959</td>
      <td>I am a retired middle school art teacher - Tau...</td>
      <td>350.0</td>
      <td>NaN</td>
      <td>15153.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>2680.0</td>
      <td>Fri Dec 01 15:53:47 +0000 2017</td>
      <td>False</td>
      <td>wicked smaht patriot</td>
      <td>Quietly watching. Sending love .++++++++</td>
      <td>539.0</td>
      <td>NaN</td>
      <td>17028.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>8921.0</td>
      <td>Mon Apr 23 21:54:10 +0000 2018</td>
      <td>False</td>
      <td>Never Dem Again</td>
      <td>#Trump2020...#KAG...#NoTrollZone #blocked...Ob...</td>
      <td>1802.0</td>
      <td>NaN</td>
      <td>4787.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>804.0</td>
      <td>Wed Feb 25 17:47:05 +0000 2015</td>
      <td>False</td>
      <td>Sam Tennant</td>
      <td>así es la vida—UNC ‘22</td>
      <td>327.0</td>
      <td>NaN</td>
      <td>14826.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>111944.0</td>
      <td>Mon Oct 17 20:17:41 +0000 2016</td>
      <td>False</td>
      <td>and justice for all</td>
      <td>Pillar of Patience, G-MA, Forever Yankee Fan, ...</td>
      <td>677.0</td>
      <td>NaN</td>
      <td>121203.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>33048.0</td>
      <td>Thu Feb 02 01:44:18 +0000 2017</td>
      <td>False</td>
      <td>Mrrin213N'Jadaka</td>
      <td>Leftist toy collector. Texas chick. Mike Patto...</td>
      <td>429.0</td>
      <td>NaN</td>
      <td>109165.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>8808.0</td>
      <td>Fri Nov 04 20:32:54 +0000 2011</td>
      <td>False</td>
      <td>bearharrumph 🏳️‍🌈😈</td>
      <td>If you can’t Carpe Deim, try to Carpe Testicul...</td>
      <td>4951.0</td>
      <td>NaN</td>
      <td>9228.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>20555.0</td>
      <td>Sun Apr 01 11:02:28 +0000 2018</td>
      <td>False</td>
      <td>Annette Maillet</td>
      <td>NaN</td>
      <td>393.0</td>
      <td>NaN</td>
      <td>20684.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [{'text': 'ICE', 'indices': [117,...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>52965.0</td>
      <td>Sun Apr 05 16:35:08 +0000 2009</td>
      <td>False</td>
      <td>Darlene M Morris</td>
      <td>A mature matron on the outside but still a wil...</td>
      <td>4951.0</td>
      <td>NaN</td>
      <td>132080.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>54032.0</td>
      <td>Mon Jun 04 13:37:13 +0000 2018</td>
      <td>False</td>
      <td>Alex Walker</td>
      <td>NaN</td>
      <td>655.0</td>
      <td>NaN</td>
      <td>1469.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>65538.0</td>
      <td>Mon Sep 16 02:15:39 +0000 2013</td>
      <td>False</td>
      <td>Eric</td>
      <td>🇲🇽</td>
      <td>566.0</td>
      <td>NaN</td>
      <td>20362.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>72590.0</td>
      <td>Mon Feb 23 17:03:50 +0000 2009</td>
      <td>False</td>
      <td>District 1</td>
      <td>The left's over reach has shown their true col...</td>
      <td>14940.0</td>
      <td>NaN</td>
      <td>4779.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>5525.0</td>
      <td>Fri Jan 20 22:09:41 +0000 2017</td>
      <td>False</td>
      <td>LaMomma</td>
      <td>Medical, Educator, Political blogger Activist ...</td>
      <td>527.0</td>
      <td>NaN</td>
      <td>7282.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>4076.0</td>
      <td>Fri May 19 01:23:04 +0000 2017</td>
      <td>False</td>
      <td>Jody Currie</td>
      <td>I'm a HVAC Service tech. God fearing American ...</td>
      <td>339.0</td>
      <td>NaN</td>
      <td>5929.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>9344.0</td>
      <td>Fri Feb 20 13:53:02 +0000 2009</td>
      <td>False</td>
      <td>Jon Ballard 🤦🏻‍♂️</td>
      <td>Radio Guy. Baseball Fan. Bacon Aficionado. Dri...</td>
      <td>540.0</td>
      <td>NaN</td>
      <td>3834.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:20 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>27703.0</td>
      <td>Mon Jun 05 04:56:43 +0000 2017</td>
      <td>False</td>
      <td>💙Lauri Turner✊🏼✊🏽✊🏾</td>
      <td>NaN</td>
      <td>175.0</td>
      <td>NaN</td>
      <td>33721.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>2746.0</td>
      <td>Wed May 20 11:50:47 +0000 2009</td>
      <td>False</td>
      <td>JDGirl</td>
      <td>Privacy zealot, freedom lover, independent thi...</td>
      <td>759.0</td>
      <td>NaN</td>
      <td>928.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>2273.0</td>
      <td>Mon Apr 20 19:40:48 +0000 2009</td>
      <td>False</td>
      <td>We need a hero🌊</td>
      <td>Not my president, in a mixed marriage, I am D ...</td>
      <td>2269.0</td>
      <td>NaN</td>
      <td>24379.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>34425.0</td>
      <td>Thu Jan 10 20:51:21 +0000 2013</td>
      <td>False</td>
      <td>AlfredTheGreat</td>
      <td>Alfred the Great - my 34th Great Grandfather! ...</td>
      <td>3392.0</td>
      <td>NaN</td>
      <td>3308.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [{'text': 'トランプ大統領', 'indices': [...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>286424.0</td>
      <td>Thu Aug 27 18:18:36 +0000 2009</td>
      <td>False</td>
      <td>伊豆の栄五郎</td>
      <td>69歳、趣味（ゴルフ、競馬、toto、FX,）、CFP,起きて半畳、寝て１畳、天下とっても２...</td>
      <td>1596.0</td>
      <td>NaN</td>
      <td>24916.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>20</th>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>12845.0</td>
      <td>Fri Mar 01 21:04:49 +0000 2013</td>
      <td>False</td>
      <td>Justin Fowler🇺🇸</td>
      <td>not a Russian bot</td>
      <td>276.0</td>
      <td>NaN</td>
      <td>12233.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>18157.0</td>
      <td>Sun Apr 23 06:12:27 +0000 2017</td>
      <td>False</td>
      <td>DinjinSamadhi</td>
      <td>I study and practice psychoanalysis and religi...</td>
      <td>77.0</td>
      <td>NaN</td>
      <td>13921.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>22</th>
      <td>22</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>8712.0</td>
      <td>Sun Apr 08 18:44:13 +0000 2018</td>
      <td>False</td>
      <td>Gail Bencomo</td>
      <td>always believed in helping others that’s why I...</td>
      <td>216.0</td>
      <td>NaN</td>
      <td>10917.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>23</th>
      <td>23</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>2061.0</td>
      <td>Mon Feb 20 01:23:08 +0000 2012</td>
      <td>False</td>
      <td>David Higgins</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>45.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>24</th>
      <td>24</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>2351.0</td>
      <td>Tue Jan 06 00:15:27 +0000 2009</td>
      <td>False</td>
      <td>squashzilla</td>
      <td>You're only as smart as other people think you...</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>20.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>61284.0</td>
      <td>Tue Mar 03 08:59:11 +0000 2009</td>
      <td>False</td>
      <td>🐞🦅🌦Denise 🐱🌲❄</td>
      <td>G-mom, mom, wife. Animal lover, music enthusia...</td>
      <td>1293.0</td>
      <td>NaN</td>
      <td>116570.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>26</th>
      <td>26</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [{'text': 'DanRyanShutDown', 'ind...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>8785.0</td>
      <td>Wed Jun 08 04:21:49 +0000 2011</td>
      <td>False</td>
      <td>Studio9</td>
      <td>Destiny only takes you half way. From there, y...</td>
      <td>1068.0</td>
      <td>NaN</td>
      <td>23704.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>47762.0</td>
      <td>Thu Jul 18 03:17:56 +0000 2013</td>
      <td>False</td>
      <td>Kimberly❤'s America</td>
      <td>#MAGA 🇺🇸 #LivePD ❤ #Mountaineers 👉 I 💞 GOD, JE...</td>
      <td>19838.0</td>
      <td>NaN</td>
      <td>126567.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>28</th>
      <td>28</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>17830.0</td>
      <td>Thu Jun 30 19:35:50 +0000 2011</td>
      <td>False</td>
      <td>Joanna</td>
      <td>Toronto Blue Jays, Raptors, Maple Leafs &amp; TFC ...</td>
      <td>178.0</td>
      <td>NaN</td>
      <td>13980.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>29</th>
      <td>29</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:31:19 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015649e+18</td>
      <td>...</td>
      <td>44313.0</td>
      <td>Sat Jun 10 15:56:34 +0000 2017</td>
      <td>False</td>
      <td>Lisa</td>
      <td>God, Family, Country, Military Mom, ALL lives ...</td>
      <td>865.0</td>
      <td>NaN</td>
      <td>39292.0</td>
      <td>False</td>
      <td>False</td>
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
      <th>4971</th>
      <td>4970</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:59 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>15613.0</td>
      <td>Thu Apr 07 03:56:15 +0000 2016</td>
      <td>False</td>
      <td>lexi • why don’t we TALK</td>
      <td>wdw. 💡| @truTVjokers ✨.</td>
      <td>640.0</td>
      <td>NaN</td>
      <td>29162.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4972</th>
      <td>4971</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:59 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>{'media': [{'id': 1015646052714668033, 'id_str...</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>4844.0</td>
      <td>Sat Jun 10 19:31:16 +0000 2017</td>
      <td>False</td>
      <td>ryn 🎮</td>
      <td>NaN</td>
      <td>421.0</td>
      <td>NaN</td>
      <td>13145.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4973</th>
      <td>4972</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:58 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>31.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>5926.0</td>
      <td>Tue Jul 21 11:27:39 +0000 2009</td>
      <td>False</td>
      <td>Kristin</td>
      <td>Inspiring young minds &amp; MAMA to these beauties...</td>
      <td>48576.0</td>
      <td>NaN</td>
      <td>8458.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4974</th>
      <td>4973</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:57 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>{'media': [{'id': 1015646052714668033, 'id_str...</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>2494.0</td>
      <td>Sun Jun 28 04:12:30 +0000 2015</td>
      <td>False</td>
      <td>Jazmine • 328 days</td>
      <td>I’m a crazy 14 y/o girl who loves to listen to...</td>
      <td>315.0</td>
      <td>NaN</td>
      <td>32237.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4975</th>
      <td>4974</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:55 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>11163.0</td>
      <td>Tue Oct 18 19:50:42 +0000 2016</td>
      <td>False</td>
      <td>‏  ًa</td>
      <td>⠀⠀⠀⠀⠀⠀𝘫𝘶𝘴𝘵 𝘴𝘰𝘶𝘯𝘥𝘴 𝘰𝘧 𝘴𝘪𝘭𝘦𝘯𝘤𝘦. @maraisless</td>
      <td>2380.0</td>
      <td>NaN</td>
      <td>128893.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4976</th>
      <td>4975</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:55 +0000 2018</td>
      <td>{'hashtags': [{'text': 'talkmusicvideo', 'indi...</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>9316.0</td>
      <td>Wed Feb 07 16:26:46 +0000 2018</td>
      <td>False</td>
      <td>MADI HAS SO MUCH RESPECT FOR DANIEL/29</td>
      <td>Madi not Maddie. I love singing,boxing,God,and...</td>
      <td>1229.0</td>
      <td>NaN</td>
      <td>25247.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4977</th>
      <td>4976</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:53 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>2800.0</td>
      <td>Sat Mar 21 12:52:07 +0000 2015</td>
      <td>False</td>
      <td>ika loves daniel</td>
      <td>17 // love Shawn Mendes and Why Don't We so mu...</td>
      <td>74.0</td>
      <td>NaN</td>
      <td>7536.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4978</th>
      <td>4977</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:52 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>9428.0</td>
      <td>Wed Nov 16 23:04:54 +0000 2016</td>
      <td>False</td>
      <td>𝚐𝚞𝚒𝚍𝚊</td>
      <td>𝙸𝚏 𝚠𝚎 𝚌𝚘𝚞𝚕𝚍 𝚜𝚙𝚎𝚊𝚔 𝚕𝚒𝚔𝚎 𝚠𝚎’𝚛𝚎 𝚝𝚛𝚢𝚒𝚗𝚐 𝚝𝚘 🌙</td>
      <td>138.0</td>
      <td>NaN</td>
      <td>85638.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4979</th>
      <td>4978</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:49 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>11416.0</td>
      <td>Sat Sep 27 16:04:46 +0000 2014</td>
      <td>False</td>
      <td>ZΛNNYΞLL</td>
      <td>19 || I’m with the boyband ||</td>
      <td>998.0</td>
      <td>NaN</td>
      <td>18901.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4980</th>
      <td>4979</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:46 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>22975.0</td>
      <td>Sat Jun 22 01:13:47 +0000 2013</td>
      <td>False</td>
      <td>Maddy•WHY DONT WE</td>
      <td>I tried to follow Daniel Seavey’s girlfriend b...</td>
      <td>1065.0</td>
      <td>NaN</td>
      <td>39521.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4981</th>
      <td>4980</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:46 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>{'media': [{'id': 1015650085496147970, 'id_str...</td>
      <td>7.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>7721.0</td>
      <td>Thu Jan 19 01:36:08 +0000 2017</td>
      <td>False</td>
      <td>cel 💘 || 22</td>
      <td>wow i have no ideas for a bio we stan that</td>
      <td>531.0</td>
      <td>NaN</td>
      <td>10455.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4982</th>
      <td>4981</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:43 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>3969.0</td>
      <td>Fri Dec 29 23:05:27 +0000 2017</td>
      <td>False</td>
      <td>Briana</td>
      <td>7-24-17 &amp; 3/8/18 &amp; 6-30-18❤️ EBEN Liked 3/8/18...</td>
      <td>517.0</td>
      <td>NaN</td>
      <td>5060.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4983</th>
      <td>4982</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:42 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>1154.0</td>
      <td>Wed Jun 20 18:19:18 +0000 2018</td>
      <td>False</td>
      <td>MIMI</td>
      <td>“Life moves pretty fast. If you don’t stop and...</td>
      <td>35.0</td>
      <td>NaN</td>
      <td>129.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4984</th>
      <td>4983</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:40 +0000 2018</td>
      <td>{'hashtags': [{'text': 'WDWTALK', 'indices': [...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>234.0</td>
      <td>Fri Sep 11 16:20:25 +0000 2015</td>
      <td>False</td>
      <td>mewmemem</td>
      <td>NaN</td>
      <td>16.0</td>
      <td>NaN</td>
      <td>351.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4985</th>
      <td>4984</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:39 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>211562.0</td>
      <td>Sat Sep 01 11:56:15 +0000 2012</td>
      <td>False</td>
      <td>`Cherry🥀</td>
      <td>I'm Cherry| IG:c.cherryy_| MFU19 HIM | 1998 | ...</td>
      <td>1771.0</td>
      <td>NaN</td>
      <td>2232.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4986</th>
      <td>4985</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:38 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>{'media': [{'id': 1015647642099937280, 'id_str...</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>3536.0</td>
      <td>Mon Nov 03 22:26:43 +0000 2014</td>
      <td>False</td>
      <td>Kathryn-Grace Stacio</td>
      <td>“hi, i’d like to order one zach herron and one...</td>
      <td>102.0</td>
      <td>NaN</td>
      <td>291.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4987</th>
      <td>4986</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:37 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>12115.0</td>
      <td>Mon Sep 07 07:05:54 +0000 2015</td>
      <td>False</td>
      <td>Emily 🧡 54 Days</td>
      <td>16 • Elder Gertrude OG • 🇦🇺🇲🇰 • trust in god a...</td>
      <td>597.0</td>
      <td>NaN</td>
      <td>36727.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4988</th>
      <td>4987</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:35 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>2243.0</td>
      <td>Sat May 30 14:11:40 +0000 2015</td>
      <td>False</td>
      <td>taylor | TALK</td>
      <td>Words turn to riddles, we make it worse</td>
      <td>226.0</td>
      <td>NaN</td>
      <td>13731.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4989</th>
      <td>4988</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:35 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>1328.0</td>
      <td>Sat Dec 20 19:55:26 +0000 2014</td>
      <td>False</td>
      <td>🌸H~E~N~Y🌷</td>
      <td>💙🏖🌷🇨🇴”don’t think we’ll ever get better,”💙🏖🌷🇨🇴</td>
      <td>192.0</td>
      <td>NaN</td>
      <td>5360.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4990</th>
      <td>4989</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:34 +0000 2018</td>
      <td>{'hashtags': [{'text': 'WDWTALK', 'indices': [...</td>
      <td>{'media': [{'id': 1015650020677148672, 'id_str...</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>45.0</td>
      <td>Sat Jun 09 08:58:30 +0000 2018</td>
      <td>False</td>
      <td>Rylee</td>
      <td>i don’t even care if you’re gonna be the death...</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>494.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4991</th>
      <td>4990</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:32 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>25870.0</td>
      <td>Sun Mar 09 07:35:41 +0000 2014</td>
      <td>False</td>
      <td>Avery is proud of wdw💘</td>
      <td>you so cute girl, yeah you is a blessing🙏;\n\n...</td>
      <td>3080.0</td>
      <td>NaN</td>
      <td>58668.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4992</th>
      <td>4991</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:31 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>{'media': [{'id': 1015649966633545729, 'id_str...</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>1599.0</td>
      <td>Sat Sep 19 14:25:09 +0000 2015</td>
      <td>False</td>
      <td>Karley</td>
      <td>Hi I miss @seaveydaniel and all of @whydontwem...</td>
      <td>125.0</td>
      <td>NaN</td>
      <td>3379.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4993</th>
      <td>4992</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:31 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>{'media': [{'id': 1015646052714668033, 'id_str...</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>1868.0</td>
      <td>Sun Apr 15 23:50:22 +0000 2018</td>
      <td>False</td>
      <td>hannah 🏴󠁧󠁢󠁥󠁮󠁧󠁿 | 107 days xx</td>
      <td>we go, breaking up like cell phones | @snoozin...</td>
      <td>199.0</td>
      <td>NaN</td>
      <td>3618.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4994</th>
      <td>4993</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:31 +0000 2018</td>
      <td>{'hashtags': [{'text': 'WDWTALK', 'indices': [...</td>
      <td>{'media': [{'id': 1015650022078083072, 'id_str...</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>2389.0</td>
      <td>Sat Dec 02 16:18:03 +0000 2017</td>
      <td>False</td>
      <td>Ririka :)🇯🇵</td>
      <td>16/WhyDon'tWe/JonahMarais</td>
      <td>233.0</td>
      <td>NaN</td>
      <td>2442.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4995</th>
      <td>4994</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:31 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>312.0</td>
      <td>Fri Sep 30 22:22:35 +0000 2016</td>
      <td>False</td>
      <td>Lisa💛✨// 29 dayss</td>
      <td>i like @whydontwemusic &amp; @alissaviolet</td>
      <td>70.0</td>
      <td>NaN</td>
      <td>387.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4996</th>
      <td>4995</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:30 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>957.0</td>
      <td>Wed Dec 21 06:47:01 +0000 2016</td>
      <td>False</td>
      <td>sHOOKED 🌈✨</td>
      <td>why dont we &amp; basic relatable things.</td>
      <td>51.0</td>
      <td>NaN</td>
      <td>1050.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4997</th>
      <td>4996</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:27 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>88.0</td>
      <td>Sun Dec 27 22:49:14 +0000 2015</td>
      <td>False</td>
      <td>Kelsey ✨</td>
      <td>I’m that bad reputation in your neighborhood;)</td>
      <td>64.0</td>
      <td>NaN</td>
      <td>172.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4998</th>
      <td>4997</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:26 +0000 2018</td>
      <td>{'hashtags': [{'text': 'TALKVIDEO', 'indices':...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>4414.0</td>
      <td>Sun Sep 04 18:00:31 +0000 2016</td>
      <td>False</td>
      <td>Lucy —109 🇬🇧</td>
      <td>r5er, potterhead, limelight, chickee, ping pon...</td>
      <td>310.0</td>
      <td>NaN</td>
      <td>13231.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4999</th>
      <td>4998</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:25 +0000 2018</td>
      <td>{'hashtags': [], 'symbols': [], 'user_mentions...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>13464.0</td>
      <td>Sat Apr 23 08:16:39 +0000 2016</td>
      <td>False</td>
      <td>𝓢𝓲𝓸𝓫𝓱𝓪𝓷</td>
      <td>Daniel 💘💖💗💓💞</td>
      <td>305.0</td>
      <td>NaN</td>
      <td>12196.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5000</th>
      <td>4999</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sat Jul 07 17:33:25 +0000 2018</td>
      <td>{'hashtags': [{'text': 'talkvideo', 'indices':...</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.015650e+18</td>
      <td>...</td>
      <td>2040.0</td>
      <td>Sun Feb 04 20:41:55 +0000 2018</td>
      <td>False</td>
      <td>Roxana</td>
      <td>I Stan @whydontwemusic,@shawnmendes, and etc #wdw</td>
      <td>64.0</td>
      <td>NaN</td>
      <td>2782.0</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>5000 rows × 54 columns</p>
</div>




```python
dfwordcloud['text']= dfwordcloud['text'].str.replace("https", "")
dfwordcloud['text']= dfwordcloud['text'].str.replace("rt", "")
dfwordcloud['text'] = dfwordcloud['text'].apply(lambda x: re.sub('[!@#$:).;,?&]', '', x.lower()))
dfwordcloud['text'] = dfwordcloud['text'].apply(lambda x: re.sub('  ', ' ', x))
tweets =dfwordcloud['text']
```


```python
def wordcloud (tweets):
   stopwords = list(set(STOPWORDS))
 
   stopwords.extend(top_names)
   stopwords.extend(["tco","guv52ytcuf",'rt'])
   wordcloud = WordCloud(background_color="grey",stopwords=stopwords,random_state = 2016).generate(" ".join([i for i in tweets]))
   plt.figure( figsize=(20,10), facecolor='k')
   plt.imshow(wordcloud)
   plt.axis("off")
   plt.title("Trending topics")
   #print(stopwords)
wordcloud(tweets)
```


![png](output_9_0.png)



```python
cloud_trump = dfwordcloud[dfwordcloud['top_user']=='realDonaldTrump']
tweets =cloud_trump['text']
wordcloud(tweets)
```


![png](output_10_0.png)



```python
twitter_lan_csv = "/Users/ZGS/Documents/Data_Bootcamp/Project-Twitter/Resources/twitter_lan.csv"
dflang = pd.read_csv(twitter_lan_csv)
dflang.head()
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
      <th>Unnamed: 0</th>
      <th>lang</th>
      <th>Group_lan</th>
      <th>top_user</th>
      <th>pos</th>
      <th>neg</th>
      <th>neu</th>
      <th>comp</th>
      <th>user_screen_name</th>
      <th>tweet_count</th>
      <th>language</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>en</td>
      <td>English</td>
      <td>realDonaldTrump</td>
      <td>0.309</td>
      <td>0.000</td>
      <td>0.691</td>
      <td>0.7712</td>
      <td>frenfer123</td>
      <td>1</td>
      <td>en</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>en</td>
      <td>English</td>
      <td>realDonaldTrump</td>
      <td>0.083</td>
      <td>0.182</td>
      <td>0.735</td>
      <td>-0.3975</td>
      <td>SandyMa92949039</td>
      <td>2</td>
      <td>en</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>en</td>
      <td>English</td>
      <td>realDonaldTrump</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0000</td>
      <td>Neverdemagain2</td>
      <td>3</td>
      <td>en</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>en</td>
      <td>English</td>
      <td>realDonaldTrump</td>
      <td>0.000</td>
      <td>0.087</td>
      <td>0.913</td>
      <td>-0.2500</td>
      <td>sam_tennant12</td>
      <td>4</td>
      <td>en</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>en</td>
      <td>English</td>
      <td>realDonaldTrump</td>
      <td>0.000</td>
      <td>0.117</td>
      <td>0.883</td>
      <td>-0.3384</td>
      <td>PaysonMelissa</td>
      <td>5</td>
      <td>en</td>
    </tr>
  </tbody>
</table>
</div>




```python
ax = sns.lmplot('tweet_count', 'comp', data=dflang, hue='Group_lan', fit_reg=False, size=8,aspect=1.3,
             legend_out=True)

sns.set_style('darkgrid', {'axes.facecolor': '.4'})
plt.title("Sentiment of Trending Users by Language (%s)" % (time.strftime("%m/%d/%Y")),fontweight ='bold',fontsize=20)
plt.xlabel("Total Tweets", fontweight='bold', fontsize=16)
plt.ylabel("Tweet Sentiment", fontweight='bold', fontsize=16)
#invert the x axis
plt.gcf().set_size_inches(18, 12)
plt.xticks(fontsize=14)
plt.gca().invert_xaxis()
plt.grid()
#plt.savefig(“Sentiment_Analysis.png”)

plt.show()
```


![png](output_12_0.png)



```python
sources =df['source'].value_counts().to_frame().reset_index()[:10]

sources['new'] = sources['index'].apply(lambda x: BeautifulSoup(x, 'lxml').get_text())

names = sources['new'].tolist()
plt.figure(1, figsize=(18, 12))
values = sources['source'].tolist()
plt.title("Amount of Tweets by Source (%s)" % (time.strftime("%m/%d/%Y")),fontweight ='bold',fontsize=22)
plt.xlabel("Total Tweets", fontweight='bold', fontsize=16)
plt.ylabel("Number of Tweets", fontweight='bold', fontsize=16)
plt.bar(names, values)
plt.xticks(names, names, rotation='vertical', fontsize = 14)

plt.show()
```


![png](output_13_0.png)



```python
new_df=df.groupby('user_screen_name').head()

df=new_df.sort_values('statuses_count', ascending=False)[:4899].reset_index()

df_date = df['user_screen_name'].to_frame(name='screen_name')

df_date['tweet_date'] = df['created_at'].apply(lambda x: parser.parse(x))

df_date['user_created']=df['user_created_at'].apply(lambda x: parser.parse(x))

df_date['time_delta']=df_date['tweet_date'] - df_date['user_created']

df_date['days'] = df_date['time_delta'].map(lambda x: x.days)

df_date['status_count'] = df['statuses_count']

df_date['tweets_per_day'] = df_date['status_count']/df_date['days']

labels = [100,200,300,400,500,600,700,800,900]

per_day =df_date.groupby(pd.cut(df_date['tweets_per_day'], bins = labels))['status_count'].count().to_frame().reset_index()

per_day

status_count = per_day['status_count'].tolist()
labels = per_day['tweets_per_day'].tolist()

status_count
labels=['100,200','200-300','300-400','400-500','500-600','600-700','700-800','800-900',]

plt.figure(1, figsize=(18, 12))
plt.title("User Tweets Per Day (%s)" % (time.strftime("%m/%d/%Y")),fontweight ='bold',fontsize=20)
plt.xlabel("User", fontweight='bold', fontsize=16)
plt.ylabel("Total Tweets Groups", fontweight='bold', fontsize=16)
plt.xticks(fontsize = 14)
plt.bar(labels, status_count)

plt.show()
```


![png](output_14_0.png)



```python
# Selected columns for new shorter df of ALL Tweets at 10 users 
df_short = df[['top_user','Unnamed: 0','comp','text','created_at','retweeted_status','user','id','user_created_at','statuses_count','favorites_count','user_screen_name','user_name','description','profile_url']].copy()
df_short['qty'] = 1*1
df_short['cap'] = 0*0
df_short['meter'] =0*0
df_short['boto_name'] = ""
df_short.head()
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
      <th>top_user</th>
      <th>Unnamed: 0</th>
      <th>comp</th>
      <th>text</th>
      <th>created_at</th>
      <th>retweeted_status</th>
      <th>user</th>
      <th>id</th>
      <th>user_created_at</th>
      <th>statuses_count</th>
      <th>favorites_count</th>
      <th>user_screen_name</th>
      <th>user_name</th>
      <th>description</th>
      <th>profile_url</th>
      <th>qty</th>
      <th>cap</th>
      <th>meter</th>
      <th>boto_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>realDonaldTrump</td>
      <td>210</td>
      <td>0.0000</td>
      <td>RT @mr_funsun: 💚#LOVEvolution 💚\n🐼#SkinTintIrr...</td>
      <td>Sat Jul 07 17:31:01 +0000 2018</td>
      <td>{'created_at': 'Sun Jun 04 15:51:01 +0000 2017...</td>
      <td>{'id': 90804267, 'id_str': '90804267', 'name':...</td>
      <td>1.015649e+18</td>
      <td>Wed Nov 18 04:52:45 +0000 2009</td>
      <td>1266433.0</td>
      <td>419252.0</td>
      <td>jojokejohn</td>
      <td>john lovethemtoyz</td>
      <td>For you-enjoy- toys&amp;collectibles-https://t.co/...</td>
      <td>http://pbs.twimg.com/profile_images/7374999810...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>England</td>
      <td>1353</td>
      <td>0.5106</td>
      <td>England thump New Zealand in first ODI: Half-c...</td>
      <td>Sat Jul 07 17:31:23 +0000 2018</td>
      <td>NaN</td>
      <td>{'id': 3049283884, 'id_str': '3049283884', 'na...</td>
      <td>1.015649e+18</td>
      <td>Sat Feb 21 09:54:50 +0000 2015</td>
      <td>696856.0</td>
      <td>61.0</td>
      <td>sportingnewsww</td>
      <td>sporting news</td>
      <td>Sporting news is here to bring you all the lat...</td>
      <td>http://pbs.twimg.com/profile_images/5690915961...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>FoxNews</td>
      <td>1696</td>
      <td>-0.4215</td>
      <td>Dr. Marc Siegel: The opioid crisis has a solut...</td>
      <td>Sat Jul 07 17:30:57 +0000 2018</td>
      <td>NaN</td>
      <td>{'id': 2735511486, 'id_str': '2735511486', 'na...</td>
      <td>1.015649e+18</td>
      <td>Fri Aug 15 20:59:39 +0000 2014</td>
      <td>627843.0</td>
      <td>22017.0</td>
      <td>JoeFreedomLove</td>
      <td>Joe FreedomLover🇺🇸</td>
      <td>Trump/PenceUSA 1st; #MAGA; Defeat ISIS; Stop S...</td>
      <td>http://pbs.twimg.com/profile_images/5004120552...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>FoxNews</td>
      <td>1852</td>
      <td>0.0000</td>
      <td>North Korea says denuclearization talks with P...</td>
      <td>Sat Jul 07 17:30:17 +0000 2018</td>
      <td>NaN</td>
      <td>{'id': 2735511486, 'id_str': '2735511486', 'na...</td>
      <td>1.015649e+18</td>
      <td>Fri Aug 15 20:59:39 +0000 2014</td>
      <td>627843.0</td>
      <td>22017.0</td>
      <td>JoeFreedomLove</td>
      <td>Joe FreedomLover🇺🇸</td>
      <td>Trump/PenceUSA 1st; #MAGA; Defeat ISIS; Stop S...</td>
      <td>http://pbs.twimg.com/profile_images/5004120552...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>FoxNews</td>
      <td>1800</td>
      <td>-0.5267</td>
      <td>The other North Korea threat -- that almost ne...</td>
      <td>Sat Jul 07 17:30:30 +0000 2018</td>
      <td>NaN</td>
      <td>{'id': 2735511486, 'id_str': '2735511486', 'na...</td>
      <td>1.015649e+18</td>
      <td>Fri Aug 15 20:59:39 +0000 2014</td>
      <td>627843.0</td>
      <td>22017.0</td>
      <td>JoeFreedomLove</td>
      <td>Joe FreedomLover🇺🇸</td>
      <td>Trump/PenceUSA 1st; #MAGA; Defeat ISIS; Stop S...</td>
      <td>http://pbs.twimg.com/profile_images/5004120552...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python
# Pull TRUMP RECORDS
trump_df = df_short.query('top_user == "realDonaldTrump"')
trump_df.head()
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
      <th>top_user</th>
      <th>Unnamed: 0</th>
      <th>comp</th>
      <th>text</th>
      <th>created_at</th>
      <th>retweeted_status</th>
      <th>user</th>
      <th>id</th>
      <th>user_created_at</th>
      <th>statuses_count</th>
      <th>favorites_count</th>
      <th>user_screen_name</th>
      <th>user_name</th>
      <th>description</th>
      <th>profile_url</th>
      <th>qty</th>
      <th>cap</th>
      <th>meter</th>
      <th>boto_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>realDonaldTrump</td>
      <td>210</td>
      <td>0.0000</td>
      <td>RT @mr_funsun: 💚#LOVEvolution 💚\n🐼#SkinTintIrr...</td>
      <td>Sat Jul 07 17:31:01 +0000 2018</td>
      <td>{'created_at': 'Sun Jun 04 15:51:01 +0000 2017...</td>
      <td>{'id': 90804267, 'id_str': '90804267', 'name':...</td>
      <td>1.015649e+18</td>
      <td>Wed Nov 18 04:52:45 +0000 2009</td>
      <td>1266433.0</td>
      <td>419252.0</td>
      <td>jojokejohn</td>
      <td>john lovethemtoyz</td>
      <td>For you-enjoy- toys&amp;collectibles-https://t.co/...</td>
      <td>http://pbs.twimg.com/profile_images/7374999810...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <th>16</th>
      <td>realDonaldTrump</td>
      <td>30</td>
      <td>0.0000</td>
      <td>@blondenfun1 @RoyalFamily @realDonaldTrump Ano...</td>
      <td>Sat Jul 07 17:31:18 +0000 2018</td>
      <td>NaN</td>
      <td>{'id': 307807275, 'id_str': '307807275', 'name...</td>
      <td>1.015649e+18</td>
      <td>Mon May 30 09:55:28 +0000 2011</td>
      <td>467299.0</td>
      <td>1241.0</td>
      <td>Stupidosaur</td>
      <td>#DestroyTheAadhaar #BanDigitalElections #Defea...</td>
      <td>Engineer who takes pics,makes cartoons,talks o...</td>
      <td>http://pbs.twimg.com/profile_images/6227271500...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <th>17</th>
      <td>realDonaldTrump</td>
      <td>475</td>
      <td>0.3818</td>
      <td>RT @LawWorksAction: "When @realDonaldTrump tal...</td>
      <td>Sat Jul 07 17:30:36 +0000 2018</td>
      <td>{'created_at': 'Sat Jul 07 14:13:07 +0000 2018...</td>
      <td>{'id': 1049560369, 'id_str': '1049560369', 'na...</td>
      <td>1.015649e+18</td>
      <td>Mon Dec 31 05:14:32 +0000 2012</td>
      <td>464731.0</td>
      <td>448244.0</td>
      <td>cheezwitham</td>
      <td>lisa witham</td>
      <td>NaN</td>
      <td>http://pbs.twimg.com/profile_images/3044794822...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <th>19</th>
      <td>realDonaldTrump</td>
      <td>266</td>
      <td>-0.4019</td>
      <td>How ironic that the neocon and Republican esta...</td>
      <td>Sat Jul 07 17:30:55 +0000 2018</td>
      <td>NaN</td>
      <td>{'id': 2167674121, 'id_str': '2167674121', 'na...</td>
      <td>1.015649e+18</td>
      <td>Fri Nov 01 03:24:23 +0000 2013</td>
      <td>427421.0</td>
      <td>417880.0</td>
      <td>CarmineZozzora</td>
      <td>JointheNRA NOW! 🇺🇸</td>
      <td>America is worth saving. #MakeAmericaGreatAgai...</td>
      <td>http://pbs.twimg.com/profile_images/9863455225...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <th>22</th>
      <td>realDonaldTrump</td>
      <td>105</td>
      <td>0.0000</td>
      <td>RT @ArizonaKayte: MUST READ THREAD!!!\n\n@Tuck...</td>
      <td>Sat Jul 07 17:31:11 +0000 2018</td>
      <td>{'created_at': 'Sat Jul 07 17:24:29 +0000 2018...</td>
      <td>{'id': 4739845481, 'id_str': '4739845481', 'na...</td>
      <td>1.015649e+18</td>
      <td>Fri Jan 08 01:27:41 +0000 2016</td>
      <td>425996.0</td>
      <td>400807.0</td>
      <td>TrumpTrainMRA4</td>
      <td>Michael💛 🌾🌺🥂HappySaturday🥂🌺🌾</td>
      <td>SavedbyGrace Pilot AeroDesgr @NASA 34Yrs Vet N...</td>
      <td>http://pbs.twimg.com/profile_images/1014877760...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python
# BOTOMETER: lookup 'accounts' for meter value, cap value, and name check
accounts = trump_df['user_screen_name']
#accounts
```


```python
## BLOCKED OUT for PRESENTATION
## Retrieve 'BOT' RATINGS from the BOTOMETER WEBSITE 
## RECORD RETRIEVAL is about 1 RECORD per 4 SECONDS, and THERE is a USER LIMIT PER DAY
#import botometer
## Authorizations:
#mashape_key = "AtjAtA78ADmsh6je89knkhTcaXitp17qeVBjsnUbRue0y6tuI0"
#twitter_app_auth = {
#     'consumer_key': 'ba2r2NuTVbWXzgq6SBCoGbY8R',
#     'consumer_secret': 'bAMeX7mUj21LWX8FpEzoQ7sjacBLrTlUcu1s43aJxPXtnhKN15',
#     'access_token': '853742326568677376-GtQ3RoG8iIxidIalAVK9n9h4XxoZizP',
#     'access_token_secret': 'KdSFuPtjjyTZynl4aZbdoapSr3zxXC69QSWd6J7SfJSPe',
#   }
# bom = botometer.Botometer(wait_on_ratelimit=True,
#                           mashape_key=mashape_key,
#                           **twitter_app_auth)
## Variables and get Botometer information
# boto_name = []
# caps = []
# meter_score = []
# count = 1*1
# NaN = "NaN"
# for screen_name, result in bom.check_accounts_in(accounts):
#     try:
#         print(count)
#         print(screen_name)
#         scrn_name = result['user']['screen_name'] # used for double checking
#         boto_name.append(scrn_name)
#         cap = result['cap']['english'] # Overall score %
#         caps.append(cap)
#         meter = result['display_scores']['english']
#         meter_score.append(meter)
#         count += 1
#         print(caps)
#         print(boto_name)
#         print(meter_score)
#         print("__________________________")
#      
#     except:
#         print(count)
#         count += 1
#         print("Skipping due to error")
#         boto_name.append(NaN)
#         caps.append(NaN)
#         meter_score.append(NaN)
#         print("__________________________")
```


```python
#Hard code backup: cap values for presentation
caps = [0.0020801266669107617, 0.31925820414416145, 0.07583235670880943, 0.0014828129117616376, 0.014543680863094452, 0.0022344951904619756, 0.0034565375041747688, 0.021603216955146855, 0.032183220269696264, 0.06706338835674493, 0.0012183789109573519, 0.028225552221050176, 0.007724054879521963, 0.07583235670880943, 0.00682617488477388, 0.0038317559975942547, 0.2564674002687074, 0.0060434470460022415, 0.011259346570646776, 0.00682617488477388, 0.004268306222830912, 0.014543680863094452, 0.15990913252190533, 0.08590409243653727, 0.0060434470460022415, 0.009922300094567935, 0.0012616932230026553, 0.22851217352302083, 0.0024124820419756166, 0.008750694009244317, 0.0038317559975942547, 0.002856940094612955, 0.0019457839054003979, 0.007724054879521963, 0.00682617488477388, 0.008750694009244317, 0.008750694009244317, 0.007724054879521963, 0.05272348371475359, 0.0026183131920431966, 0.5650534221025286, 0.02470203924309943, 0.032183220269696264, 0.008750694009244317, 0.004268306222830912, 0.14157391067567082, 0.5114515477139734, 0.004268306222830912, 0.0018284205282117316, 0.003134129284123964, 0.22851217352302083, 0.0016347149115980926, 0.008750694009244317, 0.05942480200270631, 0.0020801266669107617, 0.012788431177246198, 0.09741389119048932, 0.0013611897321404152, 0.007724054879521963, 0.0024124820419756166, 0.15990913252190533, 0.0016347149115980926, 0.00682617488477388, 0.007724054879521963, 0.046773782504080826, 0.04142512584947667, 0.0060434470460022415, 0.18036203754175442, 0.9446742630045359, 0.012788431177246198, 0.2564674002687074, 0.004268306222830912, 0.014543680863094452, 0.22851217352302083, 0.06706338835674493, 0.004775575529426348, 0.0024124820419756166, 0.0024124820419756166, 0.003134129284123964, 0.3528904417922491, 0.011259346570646776, 0.007724054879521963, 0.004775575529426348, 0.003134129284123964, 0.0038317559975942547, 0.05942480200270631, 0.0022344951904619756, 0.0024124820419756166, 0.31925820414416145, 0.004775575529426348, 0.0038317559975942547, 0.0038317559975942547, 0.0020801266669107617, 0.0013611897321404152, 0.018904416758651326, 0.0022344951904619756, 0.005363701003450149, 0.15990913252190533, 0.0020801266669107617, 0.021603216955146855, 0.5650534221025286, 0.0016347149115980926, 0.003134129284123964, 0.016566752245969804, 0.004268306222830912, 0.5114515477139734, 0.0060434470460022415, 0.11046376827194711, 0.03657805288858329, 0.0014187924969112314, 0.028225552221050176, 0.012788431177246198, 0.0024124820419756166, 0.0020801266669107617, 0.0024124820419756166, 0.00682617488477388, 0.0012183789109573519, 0.0015543510151536995, 0.28686866458066024, 0.02470203924309943, 0.004775575529426348, 0.002856940094612955, 0.12514574764971045, 0.004268306222830912, 0.004775575529426348, 0.00682617488477388, 0.011259346570646776, 0.021603216955146855, 0.003134129284123964, 0.05942480200270631, 0.14157391067567082, 0.18036203754175442, 0.0020801266669107617, 0.0019457839054003979, 0.5387761106184944, 0.14157391067567082, 0.011259346570646776, 0.0024124820419756166, 0.0060434470460022415, 0.0038317559975942547, 0.004268306222830912, 0.014543680863094452, 0.0020801266669107617, 0.003134129284123964, 0.03657805288858329, 0.05942480200270631, 0.04142512584947667, 0.004268306222830912, 0.046773782504080826, 0.20316525868115767, 0.004775575529426348, 0.018904416758651326, 0.004268306222830912, 0.28686866458066024, 0.0013611897321404152, 0.018904416758651326, 0.04142512584947667, 0.008750694009244317, 0.02470203924309943, 0.0022344951904619756, 0.31925820414416145, 0.07583235670880943, 0.012788431177246198, 0.0013611897321404152, 0.0015543510151536995, 0.011259346570646776, 0.0016347149115980926, 0.0034565375041747688, 0.06706338835674493, 0.002856940094612955, 0.007724054879521963, 0.016566752245969804, 0.0014828129117616376, 0.021603216955146855, 0.0019457839054003979, 0.14157391067567082, 0.0018284205282117316, 0.2564674002687074, 0.0038317559975942547, 0.05272348371475359, 0.0012616932230026553, 0.0038317559975942547, 0.003134129284123964, 0.0026183131920431966, 0.002856940094612955, 0.0019457839054003979, 0.014543680863094452, 0.028225552221050176, 0.0022344951904619756, 0.0014828129117616376, 'NaN', 0.008750694009244317, 0.0034565375041747688, 0.003134129284123964, 0.08590409243653727, 0.001309081196579327, 0.09741389119048932, 0.0013611897321404152, 0.003134129284123964, 0.04142512584947667, 0.003134129284123964, 0.003134129284123964, 0.003134129284123964, 0.0016347149115980926, 0.0034565375041747688, 0.0060434470460022415, 0.014543680863094452, 0.0015543510151536995, 0.0020801266669107617, 0.001725457650971877, 0.032183220269696264, 0.001725457650971877, 0.05942480200270631, 0.002856940094612955, 0.0019457839054003979, 0.05272348371475359, 0.0038317559975942547, 0.011259346570646776, 0.002856940094612955, 0.007724054879521963, 0.31925820414416145, 0.012788431177246198, 0.0019457839054003979, 0.0038317559975942547, 0.0038317559975942547, 0.001725457650971877, 0.14157391067567082, 0.011259346570646776, 0.008750694009244317, 0.04142512584947667, 0.012788431177246198, 0.007724054879521963, 0.005363701003450149, 0.021603216955146855, 0.004775575529426348, 0.0026183131920431966, 0.014543680863094452, 0.014543680863094452, 0.0026183131920431966, 0.028225552221050176, 0.0019457839054003979, 0.005363701003450149, 0.008750694009244317, 0.012788431177246198, 0.018904416758651326, 0.22851217352302083, 0.021603216955146855, 0.0038317559975942547, 0.12514574764971045, 0.007724054879521963, 0.009922300094567935, 0.0020801266669107617, 0.003134129284123964, 0.003134129284123964, 0.032183220269696264, 0.0034565375041747688, 0.011259346570646776, 0.20316525868115767, 0.0014187924969112314, 0.0011785984309163565, 0.0024124820419756166, 0.014543680863094452, 0.0038317559975942547, 0.0060434470460022415, 0.001725457650971877, 0.014543680863094452, 0.04142512584947667, 0.007724054879521963, 0.05272348371475359, 0.011259346570646776, 0.0012183789109573519, 0.12514574764971045, 0.0038317559975942547, 0.016566752245969804, 0.012788431177246198, 0.0060434470460022415, 0.3868425932473016, 0.007724054879521963, 0.014543680863094452, 0.0022344951904619756, 0.0014828129117616376, 0.04142512584947667, 0.08590409243653727, 0.0038317559975942547, 0.014543680863094452, 0.02470203924309943, 0.0026183131920431966, 0.002856940094612955, 0.0060434470460022415, 0.046773782504080826, 0.0060434470460022415, 0.12514574764971045, 0.09741389119048932, 0.04142512584947667, 0.8469348665516686, 0.002856940094612955, 0.018904416758651326, 0.0013611897321404152, 0.2564674002687074, 0.0022344951904619756, 0.005363701003450149, 0.0019457839054003979, 0.009922300094567935, 0.0020801266669107617, 0.005363701003450149, 0.001725457650971877, 0.007724054879521963, 0.0038317559975942547, 0.011259346570646776, 0.002856940094612955, 0.11046376827194711, 0.0022344951904619756, 0.20316525868115767, 0.005363701003450149, 0.011259346570646776, 0.002856940094612955, 0.032183220269696264, 0.0038317559975942547, 0.001309081196579327, 0.007724054879521963, 0.003134129284123964, 0.0060434470460022415, 0.003134129284123964, 0.002856940094612955, 0.005363701003450149, 0.004775575529426348, 0.0038317559975942547, 0.0014828129117616376, 0.0015543510151536995, 0.0038317559975942547, 0.011259346570646776, 0.0020801266669107617, 0.005363701003450149, 0.5650534221025286, 0.005363701003450149, 0.014543680863094452, 0.0034565375041747688, 0.0016347149115980926, 0.00682617488477388, 0.001725457650971877, 0.011259346570646776, 0.0022344951904619756, 0.011259346570646776, 0.0060434470460022415, 0.0022344951904619756, 0.06706338835674493, 0.31925820414416145, 0.002856940094612955, 0.28686866458066024, 0.003134129284123964, 0.0022344951904619756, 0.012788431177246198, 0.15990913252190533, 0.009922300094567935, 0.004268306222830912, 0.001725457650971877, 0.014543680863094452, 0.016566752245969804, 0.012788431177246198, 0.0019457839054003979, 0.0022344951904619756, 0.021603216955146855, 0.04142512584947667, 0.03657805288858329, 0.03657805288858329, 0.004268306222830912, 0.14157391067567082, 0.009922300094567935, 0.00682617488477388, 0.0034565375041747688, 0.04142512584947667, 0.046773782504080826, 0.004775575529426348, 0.0014828129117616376, 0.001725457650971877, 0.18036203754175442, 0.14157391067567082, 0.007724054879521963, 0.003134129284123964, 0.05942480200270631, 0.0013611897321404152, 0.0024124820419756166, 0.0034565375041747688, 0.001725457650971877, 0.0016347149115980926, 0.11046376827194711, 0.05272348371475359, 0.001725457650971877, 0.0019457839054003979, 0.0018284205282117316, 0.5906777151076118, 0.0016347149115980926, 0.48270052072345504, 0.00682617488477388, 0.20316525868115767, 0.012788431177246198, 0.0024124820419756166, 0.09741389119048932, 0.012788431177246198, 0.06706338835674493, 0.003134129284123964, 0.016566752245969804, 0.016566752245969804, 0.0034565375041747688, 0.028225552221050176, 0.06706338835674493, 0.5114515477139734, 0.0014828129117616376, 0.004775575529426348, 0.0015543510151536995, 0.00682617488477388, 0.011259346570646776, 0.009922300094567935, 0.02470203924309943, 0.0038317559975942547, 0.005363701003450149, 0.014543680863094452, 0.009922300094567935, 0.0038317559975942547, 0.016566752245969804, 0.0022344951904619756, 0.00682617488477388, 0.07583235670880943, 0.012788431177246198, 0.42020504633925215, 0.0019457839054003979, 0.003134129284123964, 0.009922300094567935, 0.09741389119048932, 0.0034565375041747688, 0.0014828129117616376, 0.04142512584947667, 0.0014187924969112314, 0.0016347149115980926, 0.005363701003450149, 0.009922300094567935, 0.001309081196579327, 0.0022344951904619756, 0.0018284205282117316, 0.012788431177246198, 0.0024124820419756166, 0.05272348371475359, 0.004775575529426348, 0.046773782504080826, 0.046773782504080826, 0.007724054879521963, 0.0024124820419756166, 0.04142512584947667, 0.0060434470460022415, 0.012788431177246198, 0.0038317559975942547, 0.0022344951904619756, 0.016566752245969804, 0.004268306222830912, 0.018904416758651326, 0.008750694009244317, 0.003134129284123964, 0.0014828129117616376, 0.0034565375041747688, 0.004775575529426348, 0.002856940094612955, 0.0038317559975942547, 0.0038317559975942547, 0.0012183789109573519, 0.45227900229523627, 0.0026183131920431966, 0.0060434470460022415, 0.05272348371475359, 0.11046376827194711, 0.0024124820419756166, 0.032183220269696264, 0.004268306222830912, 0.0060434470460022415, 0.5387761106184944, 0.02470203924309943, 0.03657805288858329, 0.03657805288858329, 0.0014187924969112314, 0.5387761106184944, 0.0022344951904619756, 0.0013611897321404152, 0.011259346570646776, 0.001309081196579327, 0.009922300094567935, 0.0024124820419756166, 0.02470203924309943, 0.0034565375041747688, 0.0060434470460022415, 0.0016347149115980926, 0.02470203924309943, 0.003134129284123964, 0.18036203754175442, 0.14157391067567082, 0.001725457650971877, 0.0022344951904619756, 0.0015543510151536995, 0.0019457839054003979, 0.6913231693056707, 0.0026183131920431966, 0.004268306222830912]
trump_df['cap'] = caps
#print(caps)
```

    /anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until



```python
#Hard code backup: meter_score for presenation
meter_score = [0.3, 3.5, 2.3, 0.2, 1.1, 0.3, 0.5, 1.3, 1.6, 2.2, 0.1, 1.5, 0.8, 2.3, 0.7, 0.5, 3.3, 0.7, 1.0, 0.7, 0.5, 1.1, 3.0, 2.4, 0.7, 0.9, 0.1, 3.3, 0.3, 0.8, 0.5, 0.4, 0.3, 0.8, 0.7, 0.8, 0.8, 0.8, 2.0, 0.4, 4.1, 1.4, 1.6, 0.8, 0.5, 2.8, 4.0, 0.5, 0.2, 0.4, 3.3, 0.2, 0.8, 2.1, 0.3, 1.0, 2.5, 0.2, 0.8, 0.3, 3.0, 0.2, 0.7, 0.8, 1.9, 1.8, 0.7, 3.1, 4.8, 1.0, 3.3, 0.5, 1.1, 3.3, 2.2, 0.6, 0.3, 0.3, 0.4, 3.6, 1.0, 0.8, 0.6, 0.4, 0.5, 2.1, 0.3, 0.3, 3.5, 0.6, 0.5, 0.5, 0.3, 0.2, 1.3, 0.3, 0.6, 3.0, 0.3, 1.3, 4.1, 0.2, 0.4, 1.2, 0.5, 4.0, 0.7, 2.6, 1.7, 0.2, 1.5, 1.0, 0.3, 0.3, 0.3, 0.7, 0.1, 0.2, 3.4, 1.4, 0.6, 0.4, 2.7, 0.5, 0.6, 0.7, 1.0, 1.3, 0.4, 2.1, 2.8, 3.1, 0.3, 0.3, 4.1, 2.8, 1.0, 0.3, 0.7, 0.5, 0.5, 1.1, 0.3, 0.4, 1.7, 2.1, 1.8, 0.5, 1.9, 3.2, 0.6, 1.3, 0.5, 3.4, 0.2, 1.3, 1.8, 0.8, 1.4, 0.3, 3.5, 2.3, 1.0, 0.2, 0.2, 1.0, 0.2, 0.5, 2.2, 0.4, 0.8, 1.2, 0.2, 1.3, 0.3, 2.8, 0.2, 3.3, 0.5, 2.0, 0.1, 0.5, 0.4, 0.4, 0.4, 0.3, 1.1, 1.5, 0.3, 0.2, 'NaN', 0.8, 0.5, 0.4, 2.4, 0.1, 2.5, 0.2, 0.4, 1.8, 0.4, 0.4, 0.4, 0.2, 0.5, 0.7, 1.1, 0.2, 0.3, 0.2, 1.6, 0.2, 2.1, 0.4, 0.3, 2.0, 0.5, 1.0, 0.4, 0.8, 3.5, 1.0, 0.3, 0.5, 0.5, 0.2, 2.8, 1.0, 0.8, 1.8, 1.0, 0.8, 0.6, 1.3, 0.6, 0.4, 1.1, 1.1, 0.4, 1.5, 0.3, 0.6, 0.8, 1.0, 1.3, 3.3, 1.3, 0.5, 2.7, 0.8, 0.9, 0.3, 0.4, 0.4, 1.6, 0.5, 1.0, 3.2, 0.2, 0.1, 0.3, 1.1, 0.5, 0.7, 0.2, 1.1, 1.8, 0.8, 2.0, 1.0, 0.1, 2.7, 0.5, 1.2, 1.0, 0.7, 3.7, 0.8, 1.1, 0.3, 0.2, 1.8, 2.4, 0.5, 1.1, 1.4, 0.4, 0.4, 0.7, 1.9, 0.7, 2.7, 2.5, 1.8, 4.6, 0.4, 1.3, 0.2, 3.3, 0.3, 0.6, 0.3, 0.9, 0.3, 0.6, 0.2, 0.8, 0.5, 1.0, 0.4, 2.6, 0.3, 3.2, 0.6, 1.0, 0.4, 1.6, 0.5, 0.1, 0.8, 0.4, 0.7, 0.4, 0.4, 0.6, 0.6, 0.5, 0.2, 0.2, 0.5, 1.0, 0.3, 0.6, 4.1, 0.6, 1.1, 0.5, 0.2, 0.7, 0.2, 1.0, 0.3, 1.0, 0.7, 0.3, 2.2, 3.5, 0.4, 3.4, 0.4, 0.3, 1.0, 3.0, 0.9, 0.5, 0.2, 1.1, 1.2, 1.0, 0.3, 0.3, 1.3, 1.8, 1.7, 1.7, 0.5, 2.8, 0.9, 0.7, 0.5, 1.8, 1.9, 0.6, 0.2, 0.2, 3.1, 2.8, 0.8, 0.4, 2.1, 0.2, 0.3, 0.5, 0.2, 0.2, 2.6, 2.0, 0.2, 0.3, 0.2, 4.2, 0.2, 3.9, 0.7, 3.2, 1.0, 0.3, 2.5, 1.0, 2.2, 0.4, 1.2, 1.2, 0.5, 1.5, 2.2, 4.0, 0.2, 0.6, 0.2, 0.7, 1.0, 0.9, 1.4, 0.5, 0.6, 1.1, 0.9, 0.5, 1.2, 0.3, 0.7, 2.3, 1.0, 3.8, 0.3, 0.4, 0.9, 2.5, 0.5, 0.2, 1.8, 0.2, 0.2, 0.6, 0.9, 0.1, 0.3, 0.2, 1.0, 0.3, 2.0, 0.6, 1.9, 1.9, 0.8, 0.3, 1.8, 0.7, 1.0, 0.5, 0.3, 1.2, 0.5, 1.3, 0.8, 0.4, 0.2, 0.5, 0.6, 0.4, 0.5, 0.5, 0.1, 3.9, 0.4, 0.7, 2.0, 2.6, 0.3, 1.6, 0.5, 0.7, 4.1, 1.4, 1.7, 1.7, 0.2, 4.1, 0.3, 0.2, 1.0, 0.1, 0.9, 0.3, 1.4, 0.5, 0.7, 0.2, 1.4, 0.4, 3.1, 2.8, 0.2, 0.3, 0.2, 0.3, 4.4, 0.4, 0.5]
trump_df['meter'] = meter_score
#print(meter_score)
```

    /anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until



```python
#Hard code backup: boto_name for presentation
boto_name = ['frenfer123', 'SandyMa92949039', 'Neverdemagain2', 'sam_tennant12', 'PaysonMelissa', 'mrrin213', 'bearharrumph', 'AnnetteMaillet3', 'mgtythor', 'AlexWal1980', '_Ericccccc', 'Bluesman57', 'ladamsrib', 'JodyC27', 'THATjonballard', 'lturner3108', 'LaredoAL', 'fancyfrog1337', 'GreatThee', 'izunoeigorou', 'jusfow', 'spandabelike', 'BencomoGail', 'oneHigginsDavid', 'squashzilla', 'kneesee79', 'Studio9Glen', 'DontMockMyTypos', 'kastlbend', 'myhappylife2020', 'Stupidosaur', 'DavidHumanzee', 'ktpasa', 'Rebashoenfelt1', 'valkyrie_hanna', 'theresa_brown50', 'Trupik127', 'dellacurran1', 'freddiechurro13', 'Smartiecats', 'raoul0430', 'jitendersoni133', 'kimmy52216977', 'raylene_resists', 'thomashourigan1', 'IAMParatiSi', 'PhyllisCowan', 'sunbeltengines', 'UnerasedUniv6', 'schachin', 'rav1960', 'RedVinesRedWine', 'dmacdonald1966', '5b20be6386164f8', 'GDawgForever', 'jjfaux82', 'scholt7', 'philtheswo', 'proudveteran63', 'wilburmeinen', 'Jaypeah', 'NishaNishimoto', 'Spiritof1773', 'cheetofacts', 'nygye', 'CharMac50', 'RojelioD', 'MCarolaNunez', 't3D45FwOb5kRKwy', 'mzzgotti1', 'DontMockMyTypos', 'bjdrues', 'Hereand66987608', 'VijayAr21020032', 'JamesABryant8', 'annmlee1', 'GillMark1709', 'JohnWayneLegend', 'GeenaJagger', 'mcivkr', 'JimmyStreich', 'nowaygirltv', 'Angelrubyring', 'joecarruba', 'ANN13951880', 'SJMoore64', 'Cunneenmachine', 'amuzme420', 'AnnaApp91838450', 'hobitcumasi', 'nicosat', 'BeulahTamborel1', 'FriendsofUKIPLl', 'Notorious_ZEB', 'ByroadsChelsie', 'buffalo_girl', 'kafd214', 'BencomoGail', 'sheadyacres', 'LANURSE1', 'Kaleesa6', 'laura_garvock', 'palomacreative', 'dmduffy6666', 'SammieGirlRSD', 'TrumpTrainMRA4', 'judemgreen', '72washington', 'richrake', 'lindyk20', 'hayne7', 'chilepeppermama', 'lorenzoVon38', 'debjensen360', 'tootame', 'spennington33', 'TexasPharmD', 'JordanGranados', '32jim2', 'crzymom110', 'DrMcKuKu', 'h2oswmn', 'Hitofan', 'yiayia62847', 'tcjepson', 'sperrin20', 'lizbethklein', 'Haytham_MG', 'RandyBMan', 'rhonda_harbison', 'cAlabaZa04901Je', 'sharonjlake', 'tomchappell', 'VioletAndSilver', 'USAloveGOD', 'RonCunningham', 'lovetreeskk', 'LDBPNV', 'BradParker_', 'booksbygin50', 'Sheamous89', 'divot1040', 'Its_All_Taken', 'jerimickelberry', 'EliseGr02404357', '5b20be6386164f8', 'D_Mass', 'spetersaz', 'mlogeman', 'LeeCapobianco1', 'JamesAr19476462', 'batliner_julia', 'rocktalkbox', 'JamesWa55188246', 'CPTDisgruntled', 'lunargranny', 'xbz2017', 'Happy01686651', 'PNewmanBennett', 'jeff14mail', 'Jan2Kole', 'chipolitics', 'Robbyusee', 'Reneeb4327', 'ckcrider', 'robert_sicario', 'Birdboy1981', 'prairie0597', 'Kupi_Zak', 'lttlgreenish', 'TerraGravity', 'Photog_NateHart', 'yungefdabean', 'Dangermmm', 'Taffy_Tart', 'duckman511', 'jeancunningham2', 'niksnook57', 'TiffanieMarcum', 'AileenMoffatt', 'Barbara_AOK', 'SexBanJohn', 'PSP7530', 'wtryonjr', 'OSGdirector', 'mamacross03', 'RobertWorthley', 'retvantq1', 'KellyKnor', 'SanduzzoPSL', 'NaN', 'Del56', 'AprilGreen93', 'billhenwood', 'DJBurn77', 'Coverciae_731', 'midwestcher', 'angelauk1900', 'DebraFletcher17', 'xbz2017', 'emilialuxa', 'BlueLn91', 'Grace4NY', 'Raqib_Ali_', 'DSoonerborn', 'AZHotTopics', 'LBarto_1952', 'Borgy_1978', 'Goofydad', 'bebemariiee', 'jojokejohn', 'NIAbbot', 'IcyBrown3', 'shara76', 'BarryOCommunist', 'sherluck_h', 'SpudLovr', 'Squiddlle', 'justwongirl', 'pamo6107', 'LeighAnnStewar8', 'Halabutt1', 'welldoneAI', 'grayjonv', 'ZagCsik', 'kalia273', 'Donna53217165', 'perrypines', 'PuniTenshu', 'xbz2017', 'LMagurck', 'GLSCHWALL', 'friest_len', 'scarlett_0hara', 'SharonCoryell3', 'NoToTheRight', 'patty_hawthorne', 'EmeldaA4', 'Pete4709', 'PickleJar10', 'SusiBV', 'dnj732', 'Citlaivi', 'mayrasons2', 'michaelsaint13', 'Patriot_Mom_17', 'MarletJones', 'meherrn', 'PradRachael', 'Kali_Wolf_888', 'Melissa53611', 'QeyeTDogbytes', 'Max96244404', 'KipHarris11', 'PatriotSally', 'TJFrazier006', 'Roger68376925', 'Winshield20', 'Kimma_S', 'idoseerussia', 'RetireNluvIT', 'LBarto_1952', 'Wilson1Theresa', 'VisibleSocSci', 'Oooooo_Donna', 'PlattWannabe', 'CarmineZozzora', 'pamo6107', 'MartinPujdak', 'NMartel54', 'darwinwoodka', 'sapayne8', 'Uniteusall12', 'Photog_NateHart', 'NottaTrolla', 'GadflyQuebec', 'di_plora', 'jimmythegote', 'Idryvfast', 'tr_williams', 'corinna_1981', 'xbz2017', 'DJBurn77', 'ANN13951880', 'JanetLe29397084', 'PNewmanBennett', 'coolncalm3', 'inertaliens', 'MountainRancher', 'lindseyforeal', 'RohanPinto', 'patsy_lee_green', 'scholt7', 'thegeekdudez', 'CERAP_Paris', 'Cynical_turd', 'andrefisher5931', 'MatthewK33', 'RebeccaSprunger', 'JosephRZarba', 'bonafideartist', 'Biggccman', 'Pell48', 'USHwy34', 'PamelaStovall6', 'DonnaCo4567890', 'pamo6107', 'PlinkinPatriot', 'ShenoahAlways', 'shottydread22', 'conservmia', 'rockinrobintwts', 'LeeCapobianco1', 'TerminalCreache', 'CozmoLizard', 'Mikeymgm1701', 'smc752', 'rcrlc8721', 'grrrr72', 'luisyahdiel3', 'resist_detroit1', 'RoscoeSauza', 'joecarruba', 'Tina51105580', 'LoveForAll24', 'irispraytan', 'GolasKathleen', 'fas1242', 'tweetflex', 'KarlSwain10', 'usageb170', 'mwh52', 'johndowe49', 'Luisraos', 'annetonie', 'EmeldaA4', 'loria_dawson', 'lonjets', 'sperrin20', 'Eloriel', 'alainmarle', 'classynogin', 'perrypines', 'LisaLew64739529', 'mutex7', 'thetheresac', 'di_plora', 'JJH789', 'VasilyAbogado', 'ERGA497511', 'eraofmoon', 'LMagurck', 'ravena68', 'leecobbonbass', 'JaksMimi', 'CPaRhon', 'StephenPetters6', 'Riponite', 'Star8400CPD', 'mellian1', 'mellymagscopy17', 'VoteTrumpPence7', 'kaseyredus', 'peanuts152', 'Stephen25719292', 'CarolFischbach1', 'NanaDavis_46', 'tomrichardson1', 'Serena_Jor', 'jasmine62246739', 'EddieDonovan', 'CarelockTim', 'kimcook49790981', 'ajfleming81', 'WellsIAm', 'littletujunga1', 'saurabhprasad', 'pamo6107', 'Retired_Now', 'Murphy931339211', 'VCurrentAffairs', 'PortableRockArt', 'save_democracy', 'mr_dsantos', 'vcntekbs', 'TPCLJ', 'Truth2Dj', 'alexroupakia', 'MarcusLDoss', 'beegSF', 'menares1945', 'mdsnkm', 'HerbertLubitz', 'Refracting', 'odecanha', 'JonieJesus1st', 'margo94', 'manzanares_ron', 'EmeldaA4', 'FlyFishingChef', 'mik84256067', 'jamielynn_xx', 'DavidRuch2', 'MsCjay', 'RomneyJudith', 'BigFish3000', 'superyayadize', 'Thee_Johnny', 'bakerbyaccident', 'Pattysanchez95', 'BBallBitchin', 'Gmanc95Castillo', 'BarbaraDadam', 'TigressLilly1', 'not6016', 'inspectorplanet', 'BryanSnow3', 'PatrioticKK', 'TeamB21919030', 'jacquesmanya', 'jnotestein', 'JanetPageHill', '034Davidhv1', 'MinaSuki143', 'Rambling_Lady', 'JanetF862258', 'mtlaurelbarb', 'bugg_ray', 'KimRoberts316', 'SOCJUSTICEDEATH', 'yungefdabean', 'InforAlemany', 'csatennis', 'jameslatoff', '21sunshine64', 'StubobNumbersAR', 'beharu', 'katemccloudsays', 'EddieH63', 'CareyJo95846484', 'TheSpeaker2012', 'SmokeyMtnStrong', 'hobitcumasi', 'TJSeraphim', 'it_middle', 'pamo6107', 'chocolatMILF', 'sccrgirl1718', 'squashzilla', 'RealBuzMartin', 'curmudgeon_girl', 'chandlertroyd', 'dekelley14', 'ForeverTepsMom', 'ChristinaZacker', 'dmacdonald1966', 'Jmacliberty', 'bbuddhas', 'MalcolmFarley', 'BaileyBono', 'joejacksonlive', 'whogotlaptop', 'ANN13951880', 'Nimasema', 'b918fvc', 'JamesRusselforc', 'OurbabyMinx', 'spanglesvi', 'scholt7', 'chelhidden', 'CarolineGasper1', 'texor2012', 'keyzpleez', 'MusingCat2014', 'scarlett_0hara', 'cheezwitham', 'farr_mimi', 'wandaransom', 'USAloveGOD', 'Unexpectedactiv', 'HeelStCloud', 'lynecarr', 'BBunjaporte_15', 'MAGAToday1', 'Rewind_Design', 'slaten_lora', 'Reader_14001', 'Lise_Borsum', 'RevDavidPSmith', 'WI4Palin', 'dansturn_views', 'timmy_rev', 'BerriePelser', 'DiXiEjO68', 'donaldrickert', 'StephanieSidley', 'RHeightsFinest', 'mandymendez90', 'Dougy_Hamilton', 'spetersaz']
trump_df['boto_name'] = boto_name
#print(boto_name)
```

    /anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until



```python
#For PRESENTATION, read in prepared csv file  (each record in the botometer takes 4 seconds to process)
#trump_df.to_csv('trump_df.csv')

# NOTE:  if this file fails, the data is already created and hardcoded as backup, and will run
#twitter_data_csv = "/Users/ZGS/Documents/Data_Bootcamp/Project-Twitter/Resources/Twitter_Data.csv"
df = pd.read_csv(twitter_data_csv)
# Presentation Data file
file = "/Users/ZGS/Documents/Data_Bootcamp/Project-Twitter/Resources/trump_df.csv"
#trump_df = pd.read_csv(file)
trump_df = pd.read_csv(file, parse_dates=['created_at'])
#trump_df.shape
```


```python
# For PRESENTATION, remove bad data (already accounted for in regular coding)
trump_df.dropna(subset=['meter','cap','boto_name'], inplace=True)
trump_df = trump_df.reset_index()
# trump_df.shape
```

# Figure 1:   500 Tweets over Time Period -  Sorted by Compound Sentiment 

# Line Graph

No coded options to select.


```python
# Sort 500 tweets by Sentiment/compound - all_tweet_df, sorted from trump_df
all_tweet_df = trump_df.sort_values('comp', ascending=False)
all_tweet_df = all_tweet_df.reset_index()
#all_tweet_df.head()
```


```python
# Date Handling from  dataframe of all 500 - date/time order
trump_date1 = trump_df.created_at[0:1]
trump_date2 = trump_df.created_at[-1:]

#Works on dataframe all_tweet_df for plot, but uses trump_df for header data range
# Prepare and Display figure
sns.set_style("darkgrid", {"axes.facecolor": ".4"})
fig, ax = plt.subplots(figsize=(20, 10))
#plt.subplot(2,1,1)
x_axis = np.arange(len(all_tweet_df))
tick_locations = [value+1 for value in x_axis]
ax.set_ylim(-1.18, 1.18)
plt.axhline(linewidth=4, color='w')
y_axis = all_tweet_df['comp']
plt.plot(x_axis,y_axis, linewidth=12, color='r')
plt.title("500 Most Recent Tweets at Trump (07/07/2018) ", size=30,fontweight='semibold')
plt.xlabel('Sorted by Sentiment Value, Over Time Period :  17:30:34 - 17:31:21 \n 48 seconds', size=22,fontweight='semibold')
plt.ylabel('Sentiment Value', size=22,fontweight='semibold')
plt.setp(ax.get_yticklabels(), size=22,fontweight='semibold')
print()
print()
plt.show()
print()
print()
```

    
    



![png](output_28_1.png)


    
    


# Figure 2:    Sample of 20 Most Recent Tweets, Sort by Compound Sentiment

#      With photos


```python
# OPTIONS
# Select 20 (default for graph details) most recent tweeters or change twt
twt = 25
```


```python
# Selected data from main trump_df
fig2_df = trump_df.head(twt)
#Date Handling before sort
trump_date1 = fig2_df.created_at[0:1]
trump_date2 = fig2_df.created_at[-1:]
# Sort by comp
fig2_df = fig2_df.sort_values(by="comp", ascending=False)
fig2_df = fig2_df.reset_index()
# I'LL BE SHOWING TWO PLOTS, ONE OVER THE OTHER TO SHOW ONE WITH 'BOTS' AND ONE WITHOUT 'BOTS'
donothing = ""
sns.set_style("darkgrid", {"axes.facecolor": ".4"})
fig, ax = plt.subplots(figsize=(30, 10))
#plt.subplot(2,1,1)

for index, row in fig2_df.iterrows():
    try:
        url_item =row['profile_url']
        response = requests.get(url_item)
        img_url = Image.open(BytesIO(response.content))
        zoom = row['meter'] *1
        imagebox = OffsetImage(img_url, zoom=zoom)
        y = row['comp']
        xy = [index+1,y]
        ab = AnnotationBbox(imagebox, xy,                    
                        xycoords='data',
                        frameon=True,
                        pad=0.6    
                        )                               
        ax.add_artist(ab)       
    except:
        print()
        print()
        print(f"Missing: {url_item}")
        # Replace this code with default photo

x_axis = np.arange(len(fig2_df)+1)
tick_locations = [value+1 for value in x_axis]
plt.xticks(tick_locations,fig2_df['user_screen_name'],rotation='vertical',size=20,fontweight='semibold')
ax.set_ylim(-1.18, 1.18)
plt.axhline(linewidth=4, color='w')
plt.title(str(twt) + " Most Recent Tweets at Trump (07/07/2018) \n Figure Size is enlarged by Botometer Meter Value \n", size=30,fontweight='semibold')
plt.xlabel('Sorted by Tweet Day/Time Stamp, Over Time Period  \n', size=30,fontweight='semibold')
plt.ylabel('Sentiment Value', size=30,fontweight='semibold')
plt.setp(ax.get_yticklabels(), fontsize=20, fontweight='semibold')
print()
print()
plt.show()
#print(f"Time Period : {trump_date1}  to  {trump_date2}")
print()
print(trump_date1)
print(trump_date2)
```

    
    
    Missing: http://pbs.twimg.com/profile_images/872617255900594176/b_woIjzV_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/965569925573152768/4MwCUDfo_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/1013105116822503424/d8XWqZ0w_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/1013737333378699264/5Ax1kQLh_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/2635226138/867ea2ca617e8c5d7a18c2a1c25b479f_normal.jpeg
    
    
    Missing: http://pbs.twimg.com/profile_images/2890266838/4c91b22c7c6d936c04482e1321901380_normal.jpeg
    
    
    Missing: http://pbs.twimg.com/profile_images/1010350814102253568/bwTz9ttu_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/997619076196429825/qL18NKhY_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/992176176662708229/NCh0_r5c_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/986800221664563201/peBpszr8_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/1003643392079876096/imleDDTq_normal.jpg
    
    
    Missing: http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png
    
    
    Missing: http://pbs.twimg.com/profile_images/991010823383339008/MSxjz-O4_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/978305331460702209/Q8JXaLSh_normal.jpg
    
    
    Missing: http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png
    
    
    Missing: http://pbs.twimg.com/profile_images/973505557481930752/PF98sk-7_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/950743415884365830/YecGhnnT_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/1006252790711242754/kS2410oO_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/824316505215139841/C2MPgHKf_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/978837699787403264/rnAXW5od_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/980484390164844544/ZU39Wy_K_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/1007767700452491264/UaZm-wKI_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/865382636700794881/H3oRuUae_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/856032890181648384/gMKH7hOf_normal.jpg
    
    
    Missing: http://pbs.twimg.com/profile_images/3578214293/045bae48b5ad68b9eb1748583beda40e_normal.jpeg
    
    



![png](output_32_1.png)


    
    0   2018-07-07 17:31:21
    Name: created_at, dtype: datetime64[ns]
    24   2018-07-07 17:31:19
    Name: created_at, dtype: datetime64[ns]


THIS GRAPH TAKES UP TO 20-30 seconds to get data to print!!  JUST WAIT when the number of TWEETERS is big

# Figure 3 :  Most Recent 200 Tweeters - front_trump_df


```python
# OPTION Warning = graph size may need to be adjusted
# To change the diplayed number of tweeters, change twt = num*1
twt = 500
```


```python
# Dataframe used is 200 Most Recent Tweets 
front_trump_df = trump_df.head(twt)
# Date handling
trump_date1 = front_trump_df.created_at[0:1]
trump_date2 = front_trump_df.created_at[-1:]

# Preapare and display figure
sns.set_style("darkgrid", {"axes.facecolor": ".4"})
fig, ax = plt.subplots(figsize=(60, 28))

for index, row in front_trump_df.iterrows():
    try:
        url_item =row['profile_url']       
        response = requests.get(url_item)
        img_url = Image.open(BytesIO(response.content))
        zoom = row['meter'] *.9
        imagebox = OffsetImage(img_url, zoom=zoom)
        y = row['comp']        
        xy = [index+1,y]
        ab = AnnotationBbox(imagebox, xy,                    
                        xycoords='data',
                        frameon=True,
                        pad=0.5
                        )                               
        ax.add_artist(ab)       
    except:
        donothing = ""
       
x_axis = np.arange(len(front_trump_df)+1)
tick_locations = [value+1 for value in x_axis]
plt.xticks(tick_locations,front_trump_df['user_screen_name'],rotation='vertical',size=20,fontweight='semibold')
ax.set_ylim(-1.18, 1.18)
plt.axhline(linewidth=2, color='r')
plt.title(str(twt) +  " Most Recent Tweets at Trump over Time \n Image size is determined by Botometer Meter Value \n", size=60,fontweight='semibold')
plt.xlabel('\n Sorted by Time Stamp (Most recent on left)  ', size= 60,fontweight='semibold')
plt.ylabel('Sentiment Value', size=60,fontweight='semibold')
plt.setp(ax.get_yticklabels(), fontsize=40, fontweight='semibold')
print()
print()
plt.show()
print(trump_date1)
print(trump_date2)
```

    
    



![png](output_36_1.png)


    0   2018-07-07 17:31:21
    Name: created_at, dtype: datetime64[ns]
    498   2018-07-07 17:30:34
    Name: created_at, dtype: datetime64[ns]


# Figure 4  :  Select cutoff=3 on the Botometer Meter from Recent 200 Tweets


```python
# OPTIONS TO RUN
cutoff = 4

cut = str(cutoff)
# Missing profile photos
suppress_print = "yes"
# Print user & data if found for graph
print_found = "yes"
# Supress printing of skipped records not in range
suppress_skip = "yes"
# Print results
suppress_results = "no"
```


```python
# Date handling - uses front_trump_df
trump_date1 = front_trump_df.created_at[0:1]
trump_date2 = front_trump_df.created_at[-1:]

# Prepare and display figure
sns.set_style("darkgrid", {"axes.facecolor": ".4"})
fig, ax = plt.subplots(figsize=(30, 12))
bots_found = []
missing_prof = []
tick = 1*1
#plot photos as found from requirements
for index, row in front_trump_df.iterrows():
    if row['meter'] >= cutoff:
        try:
            url_item =row['profile_url']
            response = requests.get(url_item)
            img_url = Image.open(BytesIO(response.content))
            zoom = row['meter'] *.9
            imagebox = OffsetImage(img_url, zoom=zoom)
            y = row['comp']
            xy = [tick,y]
            ab = AnnotationBbox(imagebox, xy,                    
                            xycoords='data',
                            frameon=True,
                            pad=0.5
                            )                               
            ax.add_artist(ab)
            bots_found.append(row['user_screen_name'])            
            tick += 1
            if print_found == "yes":
                rating = "{0:.2f}".format(row['cap']*100)
                print(f"Tweet likely from BOT found: {row['user_screen_name']}        has the CAP rating of      {rating}")
            else:
                donothing = ""
        except:
            if suppress_print == "no":
                print(f"Missing: {row['profile_url']}")
            else:
                missing_prof.append(row['user_screen_name'])   
    else:
        if suppress_skip == "no":
            print(f"Skipping meter values of Tweet Users less than {cutoff}:  " ,float(row['cap']*100)," ", row['user_screen_name'])
        else:
            donothing = ""
print()            
x_axis = np.arange(len(bots_found)+1)
tick_locations = [value+1 for value in x_axis]
plt.xticks(tick_locations,bots_found,rotation='vertical',size=20,fontweight='semibold')
ax.set_ylim(-1.18, 1.18)
plt.axhline(linewidth=2, color='r')
ax.set_title(f"From {str(twt)} Most Recent Tweets at Trump \n Botometer finding based on a minimum Meter value of {cut} out of 5", size=35,fontweight='semibold')
plt.ylabel('Sentiment Value', size=30,fontweight='semibold')
plt.xlabel('\n Sorted by Date/Time Stamp \n Image size is determined by Botometer Value ', size= 30,fontweight='semibold')
plt.setp(ax.get_yticklabels(), fontsize=20, fontweight='semibold')
print()
print()
plt.show()
if suppress_results == "no":
    print(f'RESULTS:  There were {len(bots_found)} Tweets found in this range on the Botometer findings.')
else:
    donothing = ""
print(f"          Your selected threshold for including BOTS is : {cutoff} or greater.")
print()
print(trump_date1)
print(trump_date2)
```

# Figure 5 : RESULTS using  CAP value - % likely a Complete Automated BOT


```python
# OPTIONS TO RUN
cutoff = 51

suppress_print = "yes"
print_found = "yes"
suppress_skip = "yes"
suppress_results = "no"
```


```python
# Date handling - uses front_trump_df
trump_date1 = front_trump_df.created_at[0:1]
trump_date2 = front_trump_df.created_at[-1:]

# Prepare and display figure
sns.set_style("darkgrid", {"axes.facecolor": ".4"})
fig, ax = plt.subplots(figsize=(40, 15))

missing_prof = []
bots_found = []
tick = 1*1
donothing = ""
#plot photos as found from requirements
for index, row in front_trump_df.iterrows():
    if row['cap']*100 >= cutoff:
        try:
            url_item =row['profile_url']
            response = requests.get(url_item)
            img_url = Image.open(BytesIO(response.content))
            zoom = row['meter'] *.9
            imagebox = OffsetImage(img_url, zoom=zoom)
            y = row['comp']
            xy = [tick,y]
            ab = AnnotationBbox(imagebox, xy,                    
                            xycoords='data',
                            frameon=True,
                            pad=0.5
                            )                               
            ax.add_artist(ab)
            bots_found.append(row['user_screen_name'])
            tick += 1
            if print_found == "yes":
                rating = "{0:.2f}".format(row['cap']*100)
                print(f"Tweet likely from BOT found: {row['user_screen_name']}        has the CAP rating of      {rating}")
            else:
                donothing = ""                             
        except:
            if suppress_print == "no":
                print(f"Missing: {row['profile_url']}")
            else:
                missing_prof.append(row['user_screen_name'])
    else:
        if suppress_skip == "no":
            print(f"Skipping meter values of Tweet Users less than {cutoff}:  " ,float(row['cap']*100)," ", row['user_screen_name'])
        else:
            donothing = ""
print()       
x_axis = np.arange(len(bots_found)+1)
tick_locations = [value+1 for value in x_axis]
plt.xticks(tick_locations,bots_found,rotation='vertical',size=30,fontweight='semibold')
ax.set_ylim(-1.18, 1.18)
plt.axhline(linewidth=2, color='r')
plt.title(str(twt) +  f" Most Recent Tweets at Trump \n Using CAP Value {cutoff}% from Botometer \n", size=50,fontweight='semibold')
plt.xlabel('\n Image size is determined by Meter Value', size= 50,fontweight='semibold')
plt.ylabel('Sentiment Value', size=50,fontweight='semibold')
plt.setp(ax.get_yticklabels(), fontsize=20)
plt.show()
if suppress_results == "no":
    print(f'RESULTS:  There were {len(bots_found)} Tweets found in this range on the Botometer findings.')
else:
    donothing = ""
print(f"          Your selected threshold for including BOTS is : {cutoff} or greater.")  
```


## Observations
* The Vader Sentiment tool compound sentiment number can be misleading when looking at the average of compound values. When combining the average compound score with a scatter plot view of the sentiment, it is much easier to deduce the overall distribution of tweet sentiment.
* Though many fluctuations occur, the top ten trending accounts overall attract a positive sentiment at any given time, readily outpacing negative sentiment.
* Wordcloud
    * Word cloud is a graphical representation of frequently used words within text. The height (size) of each word in this picture is an indication of frequency of occurrence of the word in the entire text. 
    * Word cloud can be a used as tool to help analyze unstructured data. To be able to count the frequency of data STOPWORDS is required to eliminate commonly occurring words.
* Data cleanup (removing characters, HTTPS, RT’s) is required to see word clouds that are of value. Word cloud analysis to some extent is less precise for text with 240 characters or less.
* Language
    * There are some common challenges of sentiment analysis such as emoji analysis, word order, spelling and certain words that may have a different or opposite meaning in certain situations. After observation is was clear that the sentiment analyzer is not accurate for multi-language text. No values recorded for Russian as an example. English text (without multi language) appeared to be more accurate.
