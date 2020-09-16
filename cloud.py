import numpy as np
import pandas as pd
import tweet
from os import path
from PIL import Image

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


def create_cloud_png(username, limit, min_count):
    word_list = tweet.get_list_of_words(username, limit)

    text = tweet.word_count_dic(word_list)

    # deletes all words that have frequency less than the min
    for key in list(text):
        if text[key] < min_count:
            text.pop(key)

    wordcloud = WordCloud(background_color="white", max_words=500, mode="RGBA").generate_from_frequencies(text)

    file_name = "wordCloud/" + username + ".png"
    wordcloud.to_file(file_name)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

   # plt.savefig(file_name)
    print("Word Cloud created successfully for " + username)



