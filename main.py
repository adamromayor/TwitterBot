#!/usr/bin/env python
import matplotlib

import tweet
import pprint

import cloud



def main():
    pp = pprint.PrettyPrinter(indent=1)
    user = 'Perf_Prac'
    donaldTrump = 'realDonaldTrump'
    barackObama = 'BarackObama'
    joeBiden = 'JoeBiden'
    andrewYang = "AndrewYang"
    elonMusk = 'elonmusk'

    me = 'aaadaaam'
    num_tweets = 200
    min_count = 4
    # tweet.upload_wordcloud_to_twitter(barackObama, num_tweets, min_count)
    # tweet.upload_wordcloud_to_twitter(donaldTrump, num_tweets, min_count)
    # tweet.upload_wordcloud_to_twitter(joeBiden, num_tweets, min_count)
    # tweet.upload_wordcloud_to_twitter(andrewYang, num_tweets, min_count)
    tweet.upload_wordcloud_to_twitter(elonMusk, num_tweets, min_count)


    return


if __name__ == "__main__":
    main()
