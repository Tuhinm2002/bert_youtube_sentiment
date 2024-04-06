import torch
import torch.nn as nn
from transformers import DistilBertTokenizer

class tokenizedText():
    def __init__(self,tokenizer="distilbert/distilbert-base-uncased"):
        self.tokenizer = DistilBertTokenizer.from_pretrained(tokenizer)

    def generateToken(self,textData):
        data = self.tokenizer(textData,return_tensors='pt')

        return data
    
    def generateText(self,text):

      return  self.tokenizer.decode(text,skip_special_tokens=True)


if __name__ == "__main__":
  textData = tokenizedText()
  token = textData.generateToken("hello world")
  print("token : ",token)
  text = textData.generateText(token)
  print("text : ",text)