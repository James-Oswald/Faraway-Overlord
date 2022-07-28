
import os
import re
import random
from dotenv import load_dotenv
from TwitterAPI import TwitterAPI,OAuthType

load_dotenv()
consumerKey = os.environ["consumer_key"]
consumerSecret = os.environ["consumer_secret"]
accessKey = os.environ["access_token_key"]
accessSecret = os.environ["access_token_secret"]

api = TwitterAPI(
    consumer_key=consumerKey,
    consumer_secret=consumerSecret,
    access_token_key=accessKey,
    access_token_secret=accessSecret)


images = os.listdir("images")
imageName = random.choice(images)
imageFile = open("./images/"+imageName, 'rb')
imageData = imageFile.read()
response = api.request('media/upload', None, {'media': imageData})

if response.status_code == 200:
    print("image uploaded sucessfully")
else:
    print("Failed to upload image:\n" + str(response.json()))
    exit(1)


nameParts = imageName.split("-")
if len(nameParts) == 5:
    name, season, episode, miniute, sec = nameParts
elif len(nameParts) == 6:
    name, season, episode, miniute, sec, _ = nameParts
else:
    print("Invalid file name " + imageName)
    exit(1)

mediaId = response.json()['media_id']
name = re.sub(r"(\w)([A-Z])", r"\1 \2", name)
tweetStr = f"{name} from season {season} ep {episode} at {miniute}:{sec}"


response = api.request('statuses/update', {'status': tweetStr, 'media_ids': mediaId})

if response.status_code == 200:
    print("posted tweet")
else:
    print("Failed to post tweet")
    exit(1)


