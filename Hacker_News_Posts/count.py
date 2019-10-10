import pandas as pd
import numpy as np
import read
from collections import Counter


if __name__ == "__main__":
    data = read.load_data()
    words = data['headline'].str.extractall("(?P<letter>[a-zA-Z]+)") 
    combined_words = words["letter"].str.cat(sep=" ").lower()
    top_hundred = Counter(combined_words.split()).most_common(100)
    print(top_hundred)