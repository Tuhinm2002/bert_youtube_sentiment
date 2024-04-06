import pandas as pd
import numpy  as np
import string
import re

class DatasetPreprocess():
    def __init__(self):
        self.trainData = pd.read_csv("train.csv")
        self.testData = pd.read_csv("test.csv")
        self.valData = pd.read_csv("val.csv")

    def removePunctuations(self,textData):
        for char in string.punctuation:
            textData = textData.replace(char,'')
        return textData

    def removeURL(self,textData):
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        urls = url_pattern.findall(textData)

        for url in urls:
            textData = textData.replace(url, "")

        return textData

    def removeHTMLTag(self,textData):
        pattern = re.compile("<.*?>")
        return pattern.sub(r'',textData)

    def preprocessTrainData(self):

      self.trainData['text'] = self.trainData['text'].apply(self.removeHTMLTag)
      self.trainData['text'] = self.trainData['text'].apply(self.removeURL)
      self.trainData['text'] = self.trainData['text'].apply(self.removePunctuations)

      self.trainData.to_csv("train.csv",index=False)


    def preprocessTestData(self):

      self.testData['text'] = self.testData['text'].apply(self.removeHTMLTag)
      self.testData['text'] = self.testData['text'].apply(self.removeURL)
      self.testData['text'] = self.testData['text'].apply(self.removePunctuations)

      self.testData.to_csv("test.csv",index=False)



    def preprocessValData(self):

      self.valData['text'] = self.valData['text'].apply(self.removeHTMLTag)
      self.valData['text'] = self.valData['text'].apply(self.removeURL)
      self.valData['text'] = self.valData['text'].apply(self.removePunctuations)

      self.valData.to_csv("val.csv",index=False)



if __name__ == "__main__":

    dataPreprocess = DatasetPreprocess()
    dataPreprocess.preprocessTrainData()
    dataPreprocess.preprocessTestData()
    dataPreprocess.preprocessValData()
