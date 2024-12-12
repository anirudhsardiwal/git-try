import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option("display.float_format", lambda x: "%.2f" % x)
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/Sardiwal_Anirudh/Documents/DSBA/1 SMDM/Lok+Sabha_2019.csv")

df.head()

sns.barplot(df, x=df["WINNER"])

sns.boxplot(df, x=df["AGE"])
