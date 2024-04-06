import matplotlib.pyplot as plt

class plotClassDistribution():
    def __init__(self,data,show=False):
        self.data = data
        self.key = self.data.keys()
        self.val = self.data.values()
        self.show = show

    def plotGraph(self):
        plt.bar(list(self.key),list(self.val),width=0.25)
        if self.show == True:
            plt.show()

if __name__ == "__main__":
  ploting = plotClassDistribution({"1":5,"0":2})
  ploting.plotGraph()