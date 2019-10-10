import pandas as pd
import numpy as np
import read
from collections import Counter

def remove_subdomains(domain):
    if pd.isnull(domain):
        return domain
    domain = str(domain)
    if domain.count('.') > 1:
        index = domain.find('.')
        real_domain = domain[index+1:]
        return real_domain
    else:
        return domain

if __name__ == "__main__":
    data = read.load_data()
    top_100 = data["url"].value_counts()[:100]
    domains = data["url"]
    domains = domains.apply(remove_subdomains)
    real_top_100 = domains.value_counts()[:100]
    print(real_top_100)