import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
import pandas as pd
import sys

from pandas import Series, DataFrame
import scipy.cluster.hierarchy as hc

exp = pd.read_table('tetrahymena.tsv', delim_whitespace=True)
print(exp)
