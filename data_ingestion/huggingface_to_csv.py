import pandas as pd
from datasets import load_dataset

class HuggingfaceToCSV():
    def __init__(self):
        self.dataset = load_dataset("carblacac/twitter-sentiment-analysis",trust_remote_code=True)

        self.df_train = pd.DataFrame(self.dataset['train'],columns=['text', 'feeling'])

        self.df_test = pd.DataFrame(self.dataset['test'],columns=['text', 'feeling'])
        self.df_val = pd.DataFrame(self.dataset['validation'],columns=['text', 'feeling'])
        
    def generateDataset(self):

        self.df_train.to_csv("train.csv",index=False)
        self.df_test.to_csv("test.csv",index=False)
        self.df_val.to_csv("val.csv",index=False)

if __name__ == '__main__':
    HFCSV = HuggingfaceToCSV()
    HFCSV.generateDataset()