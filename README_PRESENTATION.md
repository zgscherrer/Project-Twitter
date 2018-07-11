
# Project Twitter Analysis

## Why Twitter?
## What's so interesting?
  
### Stats:  
 
### ____________________Worldwide, Average Monthly Users  - 330 Million             
### ____________________79% Of Users Are Outside the United States  
### ____________________67 Million Users are in the United States  
### ____________________Twitter Can Handle  18 Quatrillion Accounts  
### ____________________Twitter Is Worth 16 Billion
  
## In a world of communication, 
##            Twitter has become a significant resource for  communication.
                    
### ____________________What are the sentiments of Tweeters, and how much is real?
# 
# 
# 
# 
 

# M Y S T E R Y ___  B O T



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
# Zachary's Lapto = use this code to open CSV 
#twitter_data_csv = "/Users/ZGS/Documents/Data_Bootcamp/Project-Twitter/Resources/Twitter_Data.csv"
#df = pd.read_csv(twitter_data_csv)
#df.head()

#Verna's Laptop = use this code to open CSV file
file = 'Twitter Data.csv'
df = pd.read_csv(file)
```

Zachary's Code Starts Here


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
#avg_by_source
```


```python
sns.set_style('darkgrid', {'axes.facecolor': '.4'})
```


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
plt.title("Overall Sentiment Towards Trending Users (07/07/2018)",fontweight='bold',fontsize=20)
plt.xlabel("Trending User", fontweight='bold', fontsize=16)
plt.ylabel("Overall Polarity", fontweight='bold', fontsize=16)
plt.xticks(rotation="vertical",fontsize=16)
#plt.savefig("Overall Sentiment Trending Users.png")
print()
print()
plt.show()
print()
```

    
    



![png](output_7_1.png)


    



```python
#Plot in seaborn based on compound sentiment
ax = sns.lmplot("tweet_count", "comp", data=df, hue='top_user', fit_reg=False, size=8,aspect=1.3,
               legend_out=True)

sns.set_style('darkgrid', {'axes.facecolor': '.4'})
#plt.title("Sentiment of Trending Users (%s)" % (time.strftime("%m/%d/%Y")),fontweight='bold',fontsize=16)
plt.title("Sentiment Toward Trending Users (07/07/2018)",fontweight='bold',fontsize=20)
plt.xlabel("Total Tweets", fontweight='bold', fontsize=16)
plt.ylabel("Tweet Sentiment", fontweight='bold', fontsize=16)
#invert the x axis
plt.gcf().set_size_inches(18, 12)
plt.gca().invert_xaxis()
plt.xticks(fontsize=16)
plt.grid()
#plt.savefig("Sentiment_Analysis.png")

plt.show()
```


![png](output_8_0.png)


Mandy's Code Starts Here


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
print()

```

    



![png](output_13_1.png)



```python
cloud_trump = dfwordcloud[dfwordcloud['top_user']=='realDonaldTrump']
tweets =cloud_trump['text']
wordcloud(tweets)
```


![png](output_14_0.png)



```python
# Zachary's Laptop, use this code to open CSV
twitter_lan_csv = "/Users/ZGS/Documents/Data_Bootcamp/Project-Twitter/Resources/twitter_lan.csv"

# Verna's Laptop, use this code to open CSV
twitter_lan_csv = "twitter_lan.csv"

# All Laptops
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
#plt.title("Sentiment of Trending Users by Language (%s)" % (time.strftime("%m/%d/%Y")),fontweight ='bold',fontsize=18)
plt.title("Sentiment of Trending Users by Language (07/07/2018)",fontweight ='bold',fontsize=20)
plt.xlabel("Total Tweets", fontweight='bold', fontsize=16)
plt.ylabel("Tweet Sentiment", fontweight='bold', fontsize=16)
#invert the x axis
plt.gcf().set_size_inches(18, 12)
plt.gca().invert_xaxis()
plt.xticks(fontsize=14)
plt.grid()
#plt.savefig(“Sentiment_Analysis.png”)

plt.show()
print()
```


![png](output_16_0.png)


    



```python
sources =df['source'].value_counts().to_frame().reset_index()[:10]

sources['new'] = sources['index'].apply(lambda x: BeautifulSoup(x, 'lxml').get_text())

names = sources['new'].tolist()
plt.figure(1, figsize=(18, 12))
values = sources['source'].tolist()
plt.title("Total Tweets by Source Device (07/07/2018)",fontweight ='bold',fontsize=22)
plt.xlabel("Devices", fontweight='bold', fontsize=16)
plt.ylabel("Number of Tweets", fontweight='bold', fontsize=18)
plt.bar(names, values)
plt.xticks(names, names, rotation='vertical',fontweight='bold',fontsize = 18)

plt.show()
```


![png](output_17_0.png)



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
labels=['100-200','200-300','300-400','400-500','500-600','600-700','700-800','800-900',]

plt.figure(1, figsize=(18, 12))
plt.title("User Tweets Per Day Towards Top 10 Users (07/072018)",fontweight ='bold',fontsize=18)
plt.xlabel("User Bins", fontweight='bold', fontsize=16)
plt.ylabel("Total Tweets Per Day", fontweight='bold', fontsize=16)
plt.xticks(fontsize=16)
plt.bar(labels, status_count)

plt.show()
```


![png](output_18_0.png)


# James image 3
#img1 = mpimg.imread('FINAL_IMAGE.PNG')
![alt text](FINAL_IMAGE.png "Title")

Verna's Code Starts Here


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

consumer_key = "ba2r2NuTVbWXzgq6SBCoGbY8R"
consumer_secret = "bAMeX7mUj21LWX8FpEzoQ7sjacBLrTlUcu1s43aJxPXtnhKN15"
app_key = "853742326568677376-GtQ3RoG8iIxidIalAVK9n9h4XxoZizP"
app_secret = "KdSFuPtjjyTZynl4aZbdoapSr3zxXC69QSWd6J7SfJSPe"

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

# BOTOMETER: lookup 'accounts' for meter value, cap value, and name check
accounts = trump_df['user_screen_name']
#accounts

# Presentation Data file substitution for static data with added API information from Botometer
file = 'trump_df.csv'
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
#df.head(2)
```


```python
# Sort 500 tweets by Sentiment/compound - all_tweet_df, sorted from trump_df
all_tweet_df = trump_df.sort_values('comp', ascending=False)
all_tweet_df = all_tweet_df.reset_index()
#all_tweet_df.head()
subset = df.query('top_user == "realDonaldTrump"')


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
plt.savefig("PTA_Verna_fig1.png")
plt.show()
print()
#print(f"SENTIMENT RESULTS:  {pos_s} Positive   {neu_s} Neutral  {neg_s}  Negative")
```

    
    



![png](output_31_1.png)


    


# Figure 2:    Sample of 20 Most Recent Tweets, Sort by Compound Sentiment

#      With photos


```python
# OPTIONS
# Select 25 (default for graph details) most recent tweeters or change twt
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
fig, ax = plt.subplots(figsize=(25, 10))
#plt.subplot(2,1,1)

#Get Image, Size and add to plot
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
plt.title(str(twt) + " Most Recent Tweets at Trump (07/07/2018) \n Figure Size is enlarged by Botometer Meter Value \n Options:  Select # of Tweets \n", size=30,fontweight='semibold')
plt.xlabel('Sorted by Tweet Day/Time Stamp, Over Time Period  \n', size=30,fontweight='semibold')
plt.ylabel('Sentiment Value', size=30,fontweight='semibold')
plt.setp(ax.get_yticklabels(), fontsize=20, fontweight='semibold')
print()
print()
plt.savefig("PTA_Verna_fig2.png")
plt.show()
#print(f"Time Period : {trump_date1}  to  {trump_date2}")
print()
print(trump_date1)
print(trump_date2)
```

    
    



![png](output_35_1.png)


    
    0   2018-07-07 17:31:21
    Name: created_at, dtype: datetime64[ns]
    24   2018-07-07 17:31:19
    Name: created_at, dtype: datetime64[ns]


THIS GRAPH TAKES UP TO 20-30 seconds to get data to print!!  JUST WAIT when the number of TWEETERS is big

# Figure 3 :  Scatter - Most Recent 200 Tweeters - front_trump_df


```python
# OPTION Warning = graph size may need to be adjusted
# To change the diplayed number of tweeters, change twt = num*1

# Show all 500 and 50
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
fig, ax = plt.subplots(figsize=(80, 28))

#Get Image, Size and add to plot
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
plt.title(str(twt) +  " Most Recent Tweets at Trump over Time \n Image size is determined by Botometer Meter Value \n Options:  Select # of Tweets \n", size=60,fontweight='semibold')
plt.xlabel('\n Sorted by Time Stamp (Most Recent on left)  ', size= 60,fontweight='semibold')
plt.ylabel('Sentiment Value', size=60,fontweight='semibold')
plt.setp(ax.get_yticklabels(), fontsize=40, fontweight='semibold')
print()
print()
plt.savefig("PTA_Verna_fig3.png")
plt.show()
print(trump_date1)
print(trump_date2)
```

    
    



![png](output_39_1.png)


    0   2018-07-07 17:31:21
    Name: created_at, dtype: datetime64[ns]
    498   2018-07-07 17:30:34
    Name: created_at, dtype: datetime64[ns]


# Figure 4  :  Select cutoff=3 on the Botometer Meter from Recent 200 Tweets


```python
# OPTIONS TO RUN on Meter Value Line prints
cutoff = 3.5
twt = 200

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
# Dataframe used is 200 Most Recent Tweets 
front_trump_df = trump_df.head(twt)
# Date handling
trump_date1 = front_trump_df.created_at[0:1]
trump_date2 = front_trump_df.created_at[-1:]

# Prepare and display figure
sns.set_style("darkgrid", {"axes.facecolor": ".4"})
fig, ax = plt.subplots(figsize=(30, 12))
bots_found = []
missing_prof = []
tick = 1*1

#Get Image, Size and add to plot
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
ax.set_title(f"From {str(twt)} Most Recent Tweets at Trump \n Botometer Finding Based on a Minimum Meter value of {cut} out of 5 \n Options:  Meter Threshold, Select # of Tweets \n", size=35,fontweight='semibold')
plt.ylabel('Sentiment Value', size=30,fontweight='semibold')
plt.xlabel('\n Sorted by Date/Time Stamp \n Image size is determined by Botometer Value \n ', size= 30,fontweight='semibold')
plt.setp(ax.get_yticklabels(), fontsize=20, fontweight='semibold')
print()
print()
plt.savefig("PTA_Verna_fig4.png")
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

    Tweet likely from BOT found: SandyMa92949039        has the CAP rating of      31.93
    Tweet likely from BOT found: raoul0430        has the CAP rating of      56.51
    Tweet likely from BOT found: PhyllisCowan        has the CAP rating of      51.15
    Tweet likely from BOT found: t3D45FwOb5kRKwy        has the CAP rating of      94.47
    Tweet likely from BOT found: mcivkr        has the CAP rating of      35.29
    Tweet likely from BOT found: Kaleesa6        has the CAP rating of      56.51
    Tweet likely from BOT found: TrumpTrainMRA4        has the CAP rating of      51.15
    Tweet likely from BOT found: USAloveGOD        has the CAP rating of      53.88
    Tweet likely from BOT found: Jan2Kole        has the CAP rating of      31.93
    
    
    



![png](output_42_1.png)


    RESULTS:  There were 9 Tweets found in this range on the Botometer findings.
              Your selected threshold for including BOTS is : 3.5 or greater.
    
    0   2018-07-07 17:31:21
    Name: created_at, dtype: datetime64[ns]
    199   2018-07-07 17:31:02
    Name: created_at, dtype: datetime64[ns]


# Figure 5 : RESULTS using  CAP value - % likely a Complete Automated BOT


```python
# OPTIONS TO RUN
cutoff = 50 # Percentage
twt = 500

print_found = "yes"  # Print user & data if FOUND for graph

suppress_results = "no"  # Print results

suppress_skip = "yes"  # Supress printing of skipped records not in range

suppress_print = "yes"  # MISSING profile photos
```


```python
cut = str(cutoff)
# Dataframe used is 200 Most Recent Tweets 
front_trump_df = trump_df.head(twt)
# Date handling
trump_date1 = front_trump_df.created_at[0:1]
trump_date2 = front_trump_df.created_at[-1:]


# Prepare and display figure
sns.set_style("darkgrid", {"axes.facecolor": ".4"})
fig, ax = plt.subplots(figsize=(40, 15))

missing_prof = []
bots_found = []
tick = 1*1
donothing = ""

#Get Image, Size and add to plot
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
                print(f"Tweet likely from BOT.    CAP Rating: {rating}    Handle: {row['user_screen_name']}")
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
plt.title(str(twt) +  f" Most Recent Tweets at Trump \n Using CAP Value {cutoff}% from Botometer \n Options:  Meter Threshold, Select # of Tweets \n", size=50,fontweight='semibold')
plt.xlabel('\n Image size is determined by Meter Value', size= 50,fontweight='semibold')
plt.ylabel('Sentiment Value', size=50,fontweight='semibold')
plt.setp(ax.get_yticklabels(), fontsize=20)
plt.savefig("PTA_Verna_fig5.png")
plt.show()
if suppress_results == "no":
    print(f'RESULTS:  There were {len(bots_found)} Tweets found in this range on the Botometer findings.')
else:
    donothing = ""
print(f"          Your selected threshold for including BOTS is : {cutoff}% or greater.") 
print()
print(trump_date1)
print(trump_date2)
```

    Tweet likely from BOT.    CAP Rating: 56.51    Handle: raoul0430
    Tweet likely from BOT.    CAP Rating: 51.15    Handle: PhyllisCowan
    Tweet likely from BOT.    CAP Rating: 94.47    Handle: t3D45FwOb5kRKwy
    Tweet likely from BOT.    CAP Rating: 56.51    Handle: Kaleesa6
    Tweet likely from BOT.    CAP Rating: 51.15    Handle: TrumpTrainMRA4
    Tweet likely from BOT.    CAP Rating: 53.88    Handle: USAloveGOD
    Tweet likely from BOT.    CAP Rating: 84.69    Handle: CERAP_Paris
    Tweet likely from BOT.    CAP Rating: 56.51    Handle: Luisraos
    Tweet likely from BOT.    CAP Rating: 59.07    Handle: menares1945
    Tweet likely from BOT.    CAP Rating: 51.15    Handle: superyayadize
    Tweet likely from BOT.    CAP Rating: 53.88    Handle: MusingCat2014
    Tweet likely from BOT.    CAP Rating: 53.88    Handle: USAloveGOD
    Tweet likely from BOT.    CAP Rating: 69.13    Handle: mandymendez90
    



![png](output_45_1.png)


    RESULTS:  There were 13 Tweets found in this range on the Botometer findings.
              Your selected threshold for including BOTS is : 50% or greater.
    
    0   2018-07-07 17:31:21
    Name: created_at, dtype: datetime64[ns]
    498   2018-07-07 17:30:34
    Name: created_at, dtype: datetime64[ns]


# Select record number to reveal actual images of user



```python
answer_this = input("Enter the record number that you would like to see more data of: ")



```


```python
# Spoof
img1 = mpimg.imread('Jeff.png')
img2 = mpimg.imread('Kellen.png')
img4 = mpimg.imread('myDial.png')
img3 = mpimg.imread('Eric.png')

fig,axes = plt.subplots(nrows = 2, ncols = 2, figsize=(10,10))
#plt.imshow(img)
axes[0,0].imshow(img1)
axes[0,1].imshow(img2)
axes[1,0].imshow(img3)
axes[1,1].imshow(img4)
axes[0,0].xaxis.set_label_text("EXTEME BOT aka JEFF",fontsize=20)
axes[0,0].yaxis.set_label_text("EXTREMELY HIGH: TWEETS PER HOUR", fontsize=12 )
axes[0,1].xaxis.set_label_text("KELLEN aka BOT",fontsize=20)
axes[0,1].yaxis.set_label_text("KNOWN ACCOMPLICE TO JEFF", fontsize=12)
axes[1,0].xaxis.set_label_text("ERIC aka BOT",fontsize=20)
axes[1,0].yaxis.set_label_text("KNOWN ACCOMPLICE TO JEFF", fontsize=12)
axes[1,1].xaxis.set_label_text("EXTREMELY HIGH BOT VALUE",fontsize=20)
#axes[1,1].yaxis.set_label_text("EXTREMELY HIGH , fontsize=12)
```




    Text(0.5,0,'EXTREMELY HIGH BOT VALUE')




![png](output_48_1.png)

