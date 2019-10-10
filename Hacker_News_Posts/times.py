import pandas as pd
import numpy as np
import read
from collections import Counter
from dateutil.parser import parse

def extract_hour(timestamp):
    parsed_timestamp = parse(timestamp)
    hour = parsed_timestamp.hour
    return hour

if __name__ == "__main__":
    data = read.load_data()
    timestamps = data["submission_time"]
    hours = timestamps.apply(extract_hour)
    hour_counts = hours.value_counts()
    
    data['hours'] = data["submission_time"].apply(extract_hour)
    hour_upvotes = pd.pivot_table(data, values='upvotes', index='hours', aggfunc=np.sum).sort_values(by="upvotes", ascending=False)
    print(hour_upvotes)