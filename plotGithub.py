import datetime
from random import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scraping as sc

DATE = datetime.date.today()  # YYYYMMDD
DATE = format(DATE, '%Y%m%d')


# KOTのAPI叩けたらいいな
df = sc.getGithub()

    
def plotBizTime(df):
    print(df)
    sns.set_palette("husl", 9)
    sns.lineplot(data=df)
    plt.show()
    

plotBizTime(df)
