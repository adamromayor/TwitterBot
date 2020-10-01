#!/usr/bin/env python
import matplotlib

import tweet
import pprint
from tweet import api

import cloud


def main():
    pp = pprint.PrettyPrinter(indent=1)
    user = 'Perf_Prac'
    donaldTrump = 'realDonaldTrump'
    barackObama = 'BarackObama'
    joeBiden = 'JoeBiden'

    num_tweets = 100
    min_count = 1

    tweet.upload_wordcloud_to_twitter(barackObama, num_tweets, min_count)
    tweet.upload_wordcloud_to_twitter(donaldTrump, num_tweets, min_count)
    tweet.upload_wordcloud_to_twitter(joeBiden, num_tweets, min_count)

    return


if __name__ == "__main__":
    main()
