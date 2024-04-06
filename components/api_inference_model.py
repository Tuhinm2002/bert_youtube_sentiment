from googleapiclient import discovery
from googleapiclient import errors

class apiYouTube():
  
  def __init__(self,maxRes=100):
    self.api_service_name = "youtube"
    self.api_version = "v3"
    self.DEVELOPER_KEY = "AIzaSyAzQ4ms31Ejv0KcMExwPFIAba57728eDUI" 
    self.maxRes = maxRes

  def findInputVideo(self,url):
    self.youtube = discovery.build(
    serviceName=self.api_service_name,version=self.api_version,developerKey=self.DEVELOPER_KEY
    )

    video_id = url.split("=")[1]
    # print(video_id)
    self.request = self.youtube.commentThreads().list(
    part="snippet",
    videoId = video_id,
    maxResults = self.maxRes
    )

    response = self.request.execute()

    final_output = []

    for item in response['items']:
     final_output.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])

    return final_output

if __name__ == "__main__":
  apicall = apiYouTube()
  final_output = apicall.findInputVideo("https://www.youtube.com/watch?v=QhKaZ94Z1Lg")
  print(final_output)