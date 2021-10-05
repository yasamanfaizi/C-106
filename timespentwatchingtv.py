import pandas as pd
import plotly.express as px

data = pd.read_csv("tv.csv")
fig = px.scatter(data, x = "Size of TV", y = "Average time")
fig.show()

corr = data.corr()
print(corr)