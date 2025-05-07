import pandas as pd

df = pd.read_json("meta_Video_games.json", lines=True)
df_reduced = df[["asin", "title"]]

df_reduced = df_reduced.rename(columns={
    "asin": "itemId",
    "title": "name"
})

df_reduced.to_csv("videogames.csv", index=False)

