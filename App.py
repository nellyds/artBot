import tweepy
import csv
import os
consumer_key = ''
consumer_key_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# note your output folder here
workDir = ""
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



if __name__ == '__main__':
    main()
