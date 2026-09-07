import pandas as pd
import json
import ast

with open("data.Json", "r", encoding = "utf-8") as file:
        output = json.load(file)
        print (len(output))
        df = pd.DataFrame(output)
        df.info()
        
df.to_csv("info.csv")

df_working = df.copy()
df_working = df_working.loc[:, df.isnull() == False]

df_0 = df[df_working["outcomePrices"] == '["0", "0"]'].copy()
df_1 = df[~(df_working["outcomePrices"] == '["0", "0"]')].copy()

