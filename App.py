import tweepy
import csv
import os
<<<<<<< HEAD
consumer_key = ''
consumer_key_secret = ''
access_token = ''
access_token_secret = ''
=======
consumer_key = 'SDffI3QFeng4u5dWG9iEKqdqD'
consumer_key_secret = 'm9hPW9TSdUX9ma6QaONN0p3hADe5KsBm1Vh9Vjoq5VXjvkHfQ6'
access_token = '1179929860480872448-XQGmTnVI1wPPC0iTtkU9ya5Awqch1K'
access_token_secret = 'OKk7YF3tx3yDuBu5U7fcGsoB3vZPG0MSXQHnjMnh5tiwn'
>>>>>>> 9d9e9b1a6e1ed6902bb98150ad3cde4a4033c7aa


auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# note your output folder here
<<<<<<< HEAD
workDir = ""
=======
workDir = "/Users/nelson/Documents/illustrations"
>>>>>>> 9d9e9b1a6e1ed6902bb98150ad3cde4a4033c7aa
# verify connectivity
try:
    api.verify_credentials()
except:
    print("Error during authentication")

def getNewestWork():
    files = [[x] for x in os.listdir(os.path.expanduser(workDir)) if ".jpg" in x]
    with open('current.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(x for x in files)

def readCsv(file):
    with open(file, 'r') as csvfile:
        content = csvfile.readlines()
        return content

def writeCurrent():
    files = [[x] for x in os.listdir(os.path.expanduser(workDir)) if ".jpg" in x]
    with open('newest.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(x for x in files)

def lookForNewest():
    return [x for x in readCsv('current.csv') if x not in readCsv('newest.csv')]

def toTweetOrNot(artOutput):
    if len(artOutput) > 0:
        for x in artOutput:
            api.media_upload(x, 'This is what I have been up to, hope you like it!')
    else:
        api.update_status("I am a bad artist who hasn't made anything new.")


def main():
    writeCurrent()
    newArt = lookForNewest()
    toTweetOrNot(newArt)
    os.rename('newest.csv','newcurrent.csv')
    os.remove('current.csv')
    os.rename('newcurrent.csv','current.csv')



<<<<<<< HEAD
=======

>>>>>>> 9d9e9b1a6e1ed6902bb98150ad3cde4a4033c7aa
if __name__ == '__main__':
    main()
