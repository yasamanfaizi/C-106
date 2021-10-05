import pandas as pd
import plotly.express as px

data = pd.read_csv("coffee.csv")
fig = px.scatter(data, x = "Coffee in ml", y = "sleep in hours" )
fig.show()
corr = data.corr()
print(corr)