from googleapiclient import discovery
from googleapiclient import errors

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyAzQ4ms31Ejv0KcMExwPFIAba57728eDUI"

youtube = discovery.build(
    serviceName=api_service_name,version=api_version,developerKey=DEVELOPER_KEY
)

request = youtube.commentThreads().list(
    part="snippet",
    videoId = "SIm2W9TtzR0",
    maxResults = 100
)

response = request.execute()

for item in response['items']:
  print(item['snippet']['topLevelComment']['snippet']['textDisplay'])