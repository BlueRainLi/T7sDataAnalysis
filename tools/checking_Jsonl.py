# -*- coding:utf-8 -*-
import jsonlines as jl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
# from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
# from statsmodels.tsa.arima_model import ARIMA
# from statsmodels.api import tsa


with jl.open("main.jsonl",mode="r") as f:
    eventId = defaultdict(list)
    for item in f:
        eventId[item["eventType"]].append(item["eventId"])
for i in range(len(eventId.keys())):
    name = list(eventId.keys())[i]
    print(name,len(eventId[name]))
print(eventId['SISTERS'])
with jl.open("vote.jsonl",mode="r") as f2:
    graph = defaultdict(list)
    ranktime = list()
    for item in f2:
        if item["eventId"] == "209":
            ranktime.append(item["RankingSpan"])
            rankinglst = item["RankingList"]
            for i in rankinglst.keys():
                graph[i].append(rankinglst[i])
ploting = []
ranktime.sort()
for item in graph:
    graph[item].sort()
    if 50 < int(item) < 3000:
        plt.plot(ranktime, graph[item])
plt.xlabel("Time")
plt.ylabel("Score")
plt.show()

