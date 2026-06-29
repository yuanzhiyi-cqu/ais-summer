import pandas as pd

scores = pd.read_csv("data/scores.csv")

print("AIS Summer Score Analyzer")
print(scores)

average_score = scores["score"].mean()
max_score = scores["score"].max()
min_score = scores["score"].min()

print("Average score:", average_score)
print("Max score:", max_score)
print("Min score:", min_score)