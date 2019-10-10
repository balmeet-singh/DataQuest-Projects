import numpy as mp
import pandas as pd

def load_data():
    data = pd.read_csv('hn_stories.csv', encoding='latin1',names=['submission_time', 'upvotes', 'url', 'headline'])

    return data


if __name__ == "__main__":
    load_data()