import tweepy
import weather
from tokens import *
import pprint
import cloud

auth = tweepy.OAuthHandler(consumerAPI.apiKey, consumerAPI.apiSecret)
auth.set_access_token(accessToken.accessToken, accessToken.accessTokenSecret)
api = tweepy.API(auth)

pp = pprint.PrettyPrinter(indent=1)
# list of common words that aren't useful in analysis
common_words = ['the', 'are', 'and', 'this', 'that', 'from', 'they', 'all', 'has',
                'for', 'not', 'you', 'your', 'will', 'with', 'too', 'its', 'their',
                'who', 'have', 'been', 'like', 'but', 'how', 'why', 'can', 'was',
                'each', 'get', 'here', 'youre', 'did', 'when', 'where', 'why', 'were',
                'thats', 'what', 'way', 'heres', 'some', 'those', 'because', 'other',
                'them', 'sure', 'into', 'than', 'ive', 'had', 'let', 'after', 'our',
                'there', 'about', 'out', 'also', 'back', 'his', 'her', 'even', 'any', 
                'very', 'could', 'lot', 'them', 'would','should', 'every', 'more',
                'most', 'many', 'just','which','want', 'including', 'else', 'these',
                'wont', 'totally','knows','really','anything','everything', 'well', 'one',
                'going', 'doing','need', 'didnt', 'thing', 'make', 'cant', 'real', 'look',
                'know']


def tweet_weather_for_today():
    today_weather = weather.get_weather()
    print(today_weather)
    api.update_status(today_weather)


# returns true if character is [@, a-z, A-Z, 0-9]
def filter_word(character):
    if character == '@':
        return True
    else:
        return character.isalnum()


# takes string as input
# returns alphanumeric string 
# deletes all punctuation except for @
def strip_word(word):
    if word == '':
        return word
    alp_num = filter(filter_word, word)
    return "".join(alp_num)


# returns sorted list of words from tweets
def get_list_of_words(username, number_of_tweets):
    limit = number_of_tweets
    statuses = api.user_timeline(username, tweet_mode='extended', count=limit)

    word_list = []

    # appends words in status to word_list
    # makes all letters lowercase
    # Skips all retweets
    for index, status in zip(range(limit), statuses):
        if "RT" not in status.full_text[:2]:
            word_list.extend(status.full_text.lower().split())

    i = 0
    for word in word_list:
        if '://' in word:  # removes https://
            word_list[i] = ''
        elif '&amp' in word:
            word_list[i] = ''
        else:
            # strips word of all characters not alphanumeric
            word_list[i] = strip_word(word)
        i += 1

    # deletes all empty strings and words length 2 or shorter from list
    word_list = [x for x in word_list if (x != '' and len(x) > 2)]

    # deletes all common words
    word_list = [x for x in word_list + common_words if x not in common_words]
    word_list.sort()
    return word_list


# takes a list of words and creates a dictionary
# key is word, value is count
def word_count_dic(word_list):
    word_dic = {}

    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return word_dic


# takes word dictionary as input dic[word] = count
# prints words in descending order
def print_words_descending(word_dic, min_count=0):
    max_count = 0
    for key in word_dic:
        if word_dic[key] > max_count:
            max_count = word_dic[key]

    while (max_count > 0) and (max_count >= min_count):
        for key in word_dic:
            if word_dic[key] == max_count:
                print("\t" + str(max_count) + "\t" + key)

        max_count -= 1


# prints most tweeted words in descending order
def find_words_tweeted_most(username, limit, min_count=0):
    word_list = get_list_of_words(username, limit)
    word_counts = word_count_dic(word_list)
    print("@" + username + " has tweeted the following words: ")
    print_words_descending(word_counts, min_count)
    return word_counts


# creates a string of CSV entries
# e.g. 5,hello
# 5 is the number of times "hello" occurs
def word_counts_csv(word_dic, min_count=0):
    csv_text = ""
    max_count = 0
    for key in word_dic:
        if word_dic[key] > max_count:
            max_count = word_dic[key]

    while (max_count > 0) and (max_count >= min_count):
        for key in word_dic:
            if word_dic[key] == max_count:
                csv_text += str(word_dic[key]) + "," + key + "\n"

        max_count -= 1
    return csv_text


def find_words_tweeted_most_csv(username, limit, min_count=0):
    word_list = get_list_of_words(username, limit)
    word_counts = word_count_dic(word_list)
    csv_text = word_counts_csv(word_counts, min_count)
    return csv_text


# takes username of twitter user
# limit is the max number of tweets
# min_count is the minimum number of times the word shows up, default is 0
def create_csv_words_tweeted_most(username, limit, min_count=0):
    csv_text = find_words_tweeted_most_csv(username, limit, min_count)
    file_name = username + ".csv"
    f = open(file_name, "w+")
    f.write(csv_text)
    f.close()
    return


# Returns the word that has the highest frequency
def get_max_word(username, limit):
    word_list = get_list_of_words(username, limit)
    word_dic = word_count_dic(word_list)
    max_word = ""
    max_count = 0
    for key in word_dic:
        if word_dic[key] > max_count:
            max_count = word_dic[key]
            max_word = key

    return max_word


# Creates a wordcloud of tweets using cloud.py module
# Uploads that wordcloud to twitter, along with some text
def upload_wordcloud_to_twitter(username, limit, min_count):
    cloud.create_cloud_png(username, limit, min_count)
    file_name = "wordCloud/" + username + ".png"
    media = api.media_upload(file_name)
    hashtag = get_max_word(username, limit)

    text = "The most common words tweeted by @" + username + " in their last " + str(limit) + \
           " tweets! See anything interesting? #" + hashtag

    api.update_status(status=text, media_ids=[media.media_id])
