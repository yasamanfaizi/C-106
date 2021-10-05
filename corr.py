import pandas as pd
import plotly.express as px

data = pd.read_csv("sales.csv")
fig = px.scatter(data, x = "Temperature", y = "Ice-cream Sales( ₹ )" )
fig.show()
corr = data.corr()
print(corr)