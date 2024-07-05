from twikit import Client
import json

client = Client('en-US')

client.load_cookies('cookies.json')

screen_name = 'example_user'
user = client.get_user_by_screen_name(screen_name)
user_id = user.id

tweets = client.get_user_tweets(user_id, 'Media', count=50)

with open('tweets.txt', 'w') as file:
    for tweet in tweets:
        file.write(tweet + '\n')
