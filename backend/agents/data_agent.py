import pandas as pd
import random

def load_data():
    df = pd.read_csv("data/resources.csv")

    # 🔥 Simulate real-time fluctuations
    df["usage"] = df["usage"].apply(
        lambda x: max(0, min(100, x + random.randint(-15, 15)))
    )

    df["task_time"] = df["task_time"].apply(
        lambda x: max(1, x + random.randint(-3, 5))
    )

    return df