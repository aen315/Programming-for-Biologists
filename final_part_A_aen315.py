import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
import pandas as pd
import sys

from pandas import Series, DataFrame
import scipy.cluster.hierarchy as hc 

exp = pd.read_table('tetrahymena.tsv', delim_whitespace=True)
#loaded file into a dataframe with the given names as column names.
x = exp['diameter']>= 19.2
#in the read table x is the diameter if its greater than or equal to 19.2
exp = exp[x] 
y = exp['diameter']<= 26.0
#in the read table y is the diameter if its less than or equal to 26
exp = exp[y]

exp['log_concentration'] = np.log(exp.conc)
exp['log_diameter'] = np.log(exp.diameter)

plot1 = sns.pairplot(x_vars=['conc'], y_vars=['diameter'], data=exp, hue= 'glucose',markers= ['x','o'], height=5)
plot2 = sns.pairplot(x_vars=['log_concentration'], y_vars=['log_diameter'], data=exp, hue= 'glucose',markers= ['x','o'],height=5)
#markers changes shape of markers for glucose depending on its presence

plot1.savefig("final_part_A_nonlog_aen315.pdf")
plot2.savefig("final_part_A_log_aen315.pdf")

