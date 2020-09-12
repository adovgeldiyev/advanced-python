DIR='/Users/14023/Anaconda3/envs/Pandas/Lib/site-packages/pandas'
import pandas as pd
import math
import statistics
from statistics import mean, median,pstdev

def sm_Mean(csv):
    dataset=pd.read_csv(DIR+'/avocado.csv',delimiter=',')
    sMean=dataset["Total Volume"].mean()
    print("The mean of Total Volume is: {}".format(round(sMean,3)))
 

def sm_Median(csv):
    dataset=pd.read_csv(DIR+'/avocado.csv',delimiter=',')
    sMedian=dataset["Total Volume"].median()
    print("The median of Total Volume is: {}".format(round(sMedian,3)))

def sm_Std(csv):
    dataset=pd.read_csv(DIR+'/avocado.csv',delimiter=',')
    pStd=statistics.pstdev(dataset["Total Volume"],dataset["Total Volume"].mean())
    print("The standard deviation of Total Volume is: {}".format(round(pStd,3)))

def hg_Mean(csv):
    dataset=pd.read_csv(DIR+'/avocado.csv',delimiter=',')
    print("Mean of the Total Volume using homegrown formula is: {}".\
        format(round(sum(dataset["Total Volume"])/len(dataset["Total Volume"]),3)))
    
def hg_Median(csv):
    dataset=pd.read_csv(DIR+'/avocado.csv',delimiter=',')
    n=len(dataset["Total Volume"])
    f=sorted(dataset["Total Volume"])
    if n%2==0:
        med1=f[n//2]
        med2=f[n//2-1]
        med=(med1+med2)/2
    else:
        med=f[n//2]
    print("Median of the Total Volume using homegrown formula is: {}".format(round(med,3)))

def hg_Std(csv):
    dataset=pd.read_csv(DIR+'/avocado.csv',delimiter=',')
    Mean=sum(dataset["Total Volume"])/len(dataset["Total Volume"])
    var=sum(pow(x-Mean,2) for x in dataset["Total Volume"])/len(dataset["Total Volume"])
    std=var**0.5
    print("Standard deviation of the Total Volume using homegrown formula is: {}".format(round(std,3)))

sm_Mean("avocado.csv")
sm_Median("avocado.csv")
sm_Std("avocado.csv")
hg_Mean("avocado.csv")
hg_Median("avocado.csv")
hg_Std("avocado.csv")