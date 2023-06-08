import numpy as np
import pandas as pd

def add_one(x):
    return x + 1

def add_one_to_df(x):
    x = add_one(x)
    out = pd.DataFrame(x)
    return out

