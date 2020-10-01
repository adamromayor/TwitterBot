# TwitterBot

This program analyzes the most recent tweets from any public twitter user.

It will look at the most recent x number of tweets and create a word cloud out of the
most frequent number of words. This program will upload this word cloud to twitter
using the account @Perf_Prac

tweet.py:
  > Contains the functions that are used to analyze tweets
  > Uses twitter API to grab recent n tweets from any public user
  > Analyzes tweets to create a dictionary of words and frequencies
  > Generates a wordcloud of frequent words and posts the word cloud to twitter
  > Wordlouc is generated using cloud.py module
  
cloud.py:
  > Contains the functions used to generate a word cloud and save it into the
  > wordCloud folder as a .png file
 
weather.py
  > Contains functions to tweet the current weather.

