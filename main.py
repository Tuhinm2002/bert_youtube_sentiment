import torch
import torch.nn as nn
from transformers import DistilBertForSequenceClassification
from components import plotClassDistribution,tokenizedText,apiYouTube

bertModel = DistilBertForSequenceClassification.from_pretrained(r"models\bertModel")
# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
tokenizer = tokenizedText()

def main():
    inputs = tokenizer.generateToken("bye world")
    with torch.no_grad():
        print(bertModel(**inputs).logits)

if __name__ == "__main__":
    main()