import pandas as pd
import csv

df = pd.read_csv("final_data.csv")
print(df.shape)

del df["Star_name1"]
del df["Distance1"]
del df["Mass1"]
del df["Radius1"]

df.to_csv("new_data.csv")