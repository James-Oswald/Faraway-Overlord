
import os
import re
import random
from dotenv import load_dotenv
from TwitterAPI import TwitterAPI,OAuthType

load_dotenv(override=True)
consumerKey = os.environ["consumer_key"]
consumerSecret = os.environ["consumer_secret"]
accessKey = os.environ["access_token_key"]
accessSecret = os.environ["access_token_secret"]

print(consumerKey)
print(consumerSecret)
print(accessKey)
print(accessSecret)


apiV1 = TwitterAPI(
    consumer_key=consumerKey,
    consumer_secret=consumerSecret,
    access_token_key=accessKey,
    access_token_secret=accessSecret,
    api_version="1.1")

apiV2 = TwitterAPI(
    consumer_key=consumerKey,
    consumer_secret=consumerSecret,
    access_token_key=accessKey,
    access_token_secret=accessSecret,
    api_version="2")


images = os.listdir("images")
imageName = random.choice(images)
imageFile = open("./images/"+imageName, 'rb')
imageData = imageFile.read()
response = apiV1.request('media/upload', None, {'media': imageData})

if response.status_code == 200:
    print("image uploaded sucessfully")
else:
    print("Failed to upload image:\n" + str(response.json()))
    exit(1)

imageName, _ = imageName.split(".") #get rid of file extension
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


response = apiV2.request('tweets', {'text': tweetStr, "media": {"media_ids": [str(mediaId)] }}, method_override="POST")

if response.status_code == 201: 
    print("posted tweet")
else:
    print(response.status_code)
    print("Failed to post tweet" + str(response.json()))
    exit(1)


