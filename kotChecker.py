import datetime
from random import random
import jpholiday
import calendar
import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns

DATE = datetime.date.today()  # YYYYMMDD
DATE = format(DATE, '%Y%m%d')


def isBizDay(DATE):
    Date = datetime.date(int(DATE[0:4]), int(DATE[4:6]), int(DATE[6:8]))
    if Date.weekday() >= 5 or jpholiday.is_holiday(Date):
        return 0
    else:
        return 1
    
    
def totoalBizDay(DATE):
    EndDay = calendar.monthrange(int(DATE[0:4]), int(DATE[4:6]))[1]
    countBizDays = 0
    for day in [x for x in range(1, EndDay + 1)]:
        date = format(datetime.date(int(DATE[0:4]), int(DATE[4:6]), day), '%Y%m%d')
        countBizDays += isBizDay(date)
    return countBizDays


def totalBizTime(bizDays):
    minimumTime = bizDays * 8
    maximumTime = minimumTime + 40
    gorinjuTime = minimumTime + 75
    return (minimumTime, maximumTime, gorinjuTime)


# KOTのAPI叩けたらいいな
def getBizTimes():
    # sample data
    date = [format(datetime.date(int(DATE[0:4]), int(DATE[4:6]), x), '%Y%m%d') for x in range(1, totoalBizDay(DATE) + 1)]
    hours = [random.randint(7, 10) for x in range(1, totoalBizDay(DATE) + 1)]
    df = pd.DataFrame({'date': date, 'hours': hours})
    print(df.cumsum())
    return df.cumsum()
    
    
def plotBizTime(df, workDays, minimumTime, maximumTime, gorinjuTime):
    print(df)
    sns.set_palette("husl", 9)
    sns.lineplot(data=df)
    plt.ylim(0, gorinjuTime + 10)
    plt.xlim(1, 1 + workDays)
    plt.hlines(minimumTime, 1, 31, 'g', linestyles='dashed')
    plt.hlines(maximumTime, 1, 31, 'b', linestyles='dashed')
    plt.hlines(gorinjuTime, 1, 31, 'r', linestyles='dashed')
    plt.plot(len(df) - 1, df.iloc[-1]['hours'], marker='o', markersize=10)
    print(len(df) - 1, df.iloc[-1]['hours'])
    
    for x in range(1, len(df)):
        plt.hlines(df.iloc[x]['hours'], 0, x, "m", linestyle=":", alpha=0.2, color="black")
        plt.vlines(x, 0, df.iloc[x]['hours'], "m", linestyle=":", alpha=0.2, color="black")
    plt.show()
    

plotBizTime(getBizTimes(), totoalBizDay(DATE), *totalBizTime(totoalBizDay(DATE)))
