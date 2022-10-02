import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()
projectDir=os.path.dirname(os.path.abspath("__file__"))
dataDir=os.path.join(projectDir,'data')
fileNames = os.listdir(dataDir)
def animate(i):
    charts=[]
    plt.cla()
    for file in fileNames:
        file_path = os.path.join(dataDir, file)
        df = pd.read_csv(file_path, index_col = 0)
        plt.xticks(rotation=30)
        chart,_=plt.plot(df,label=file)
        charts.append(chart)
    plt.legend(loc='upper left',handles=charts)
    


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
#plt.gca().axes.get_xaxis().set_visible(False)
plt.show()
