import os
import pandas as pd


def load_checkpoint(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        completed = set(df["Question"])
        print(f"Loaded {len(completed)} completed questions.")

        return df, completed

    print("Starting new run.")

    return pd.DataFrame(), set()


def save_checkpoint(responses, path):

    pd.DataFrame(responses).to_csv(
        path,
      index=False)
