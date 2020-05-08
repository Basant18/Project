import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 
from textblob import TextBlob
import numpy as np

file=pd.read_csv(r'D:\Public_Tweets_Police.csv')
#print(file.shape)
#print(file.info())
#print(file.columns)


comment_words=" "
stopwords = set(STOPWORDS)
#print(stopwords)
for val in file.Tweet:
    
    # typecaste each val to string 
    val = str(val) 
    #clean_data(val)
    # split the value 
    #break the string by space seperator
    tokens = val.split(' ')   
    
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower()  #convert every word to lower case 
          
    for words in tokens: 
         comment_words = comment_words + words + ' '

#print(comment_words)

wordcloud = WordCloud(width = 700, height = 600, 
                background_color ='white', 
                stopwords=stopwords,
                colormap='rainbow',
                max_font_size=50, min_font_size=10).generate(comment_words)

# plot the WordCloud image                        
plt.figure(figsize = (7, 6), facecolor = None) 
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis("off")  #dont' show x and y axis 
plt.tight_layout(pad = 0) #no space   
plt.show()
sns.countplot(x='city_police',data=file)
plt.show()
#sentiment analysis
positive=0
negative=0
neutral=0
#ploting sentiment graph
for tweet in file.Tweet:
    tweet=str(tweet)
    analysis=TextBlob(tweet)
    if analysis.sentiment.polarity<0:
        negative+=1
    elif analysis.sentiment.polarity>0:
        positive+=1
    elif analysis.sentiment.polarity==0:
        neutral+=1
#print("positive=",positive)
#print("negative=",negative)
#print("neutr3al=",neutral)  
index = np.arange(1)
bar_width = 0.1
opacity = 1

plt.bar(index, positive, bar_width, alpha=opacity, color='g', edgecolor='w', label='positive')


plt.bar(index + bar_width, negative, bar_width, alpha=opacity, color='r', edgecolor='w', label='negative')


plt.bar(index + bar_width+ bar_width, neutral, bar_width, alpha=opacity, color='b', edgecolor='w', label='neutral')

plt.xticks(index+bar_width, [""],family='fantasy')
plt.xlabel('Tweets',fontweight='bold',fontsize='10')
plt.ylabel('Sentiments',fontweight='bold',fontsize='10')
plt.title('Sentiment Analysis',fontweight='bold', color = 'white', fontsize='17', horizontalalignment='center',backgroundcolor='black')
plt.legend()
plt.tight_layout()
plt.show()