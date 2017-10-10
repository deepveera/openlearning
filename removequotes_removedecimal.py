import pandas as pd
import numpy as np
import csv
df = pd.read_csv("input.csv",header=None)
df.apply(lambda x: x.replace('"', ''))
df.to_csv('output.csv', float_format='%.0f',index=False,header=False,quoting=csv.QUOTE_NONE)