import pandas as pd
import numpy as np

print("AIS summer environment is ready.")

scores = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy"],
    "score": [90, 85, 88]
})

print(scores)
print("Average score:", np.mean(scores["score"]))