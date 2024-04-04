import pandas as p
import numpy as n
import matplotlib.pyplot as m
import seaborn as s
data=p.read_csv("C:\Program Files\Training_Data_Google_Play_reviews_6000.csv")
data.head(50)
data.columns
data.tail(50)
data.describe()
s.scatterplot(x=data["score"],y=data["thumbsUpCount"],data=data)
m.title('Scatterplot')
m.xlabel('score')
m.ylabel('thumbsUpCount')
m.show()
s.boxplot(x='score',y='thumbsUpCount',data=data)
m.title('Boxplot')
m.xlabel('score')
m.ylabel('thumbsUpCount')
m.show()
s.histplot(data["score"],bins=30,kde=True)
m.title('Histogram')
m.xlabel('score')
m.ylabel('thumbsUpCount')
m.show()
data["score"].value_counts().plot(kind='bar')
m.title('Bardiagram')
m.xlabel('score')
m.ylabel('thumbsUpCount')
m.show()
