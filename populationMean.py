import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
pop_mean=statistics.mean(data)
std_dev=statistics.stdev(data)
print("Population Mean",pop_mean)
print("Standard Deviation",std_dev)

def randomMeanSet(counter):
    data_set=[]

    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    
    mean=statistics.mean(data_set)
    return mean

def show_fig(mean_list):
    df=mean_list
    MEAN=statistics.mean(mean_list)
    print("Mean",MEAN)
    StdDEV=statistics.stdev(mean_list)
    print("Standard Deviation",StdDEV)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[MEAN,MEAN],y=[0,1],mode="lines",name="mean"))
    fig.show()

mean_list=[]

for i in range(0,1000):
    set_of_means=randomMeanSet(100)
    mean_list.append(set_of_means)

show_fig(mean_list)


std_deviation=statistics.stdev(mean_list)
first_std_dev_start,first_std_dev_end=pop_mean-std_deviation,pop_mean+std_deviation
second_std_dev_start,second_std_dev_end=pop_mean-(std_deviation*2),pop_mean+(std_deviation*2)
third_std_dev_start,third_std_dev_end=pop_mean-(std_deviation*3),pop_mean+(std_deviation*3)

fig=ff.create_distplot([mean_list],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[pop_mean,pop_mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.17],mode="lines",name="First Standard Deviation"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.17],mode="lines",name="First Standard Deviation"))
fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.17],mode="lines",name="Second Standard Deviation"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.17],mode="lines",name="Second Standard Deviation"))
fig.show()