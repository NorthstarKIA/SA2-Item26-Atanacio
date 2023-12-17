# Importing library
from scipy.stats import f_oneway
import pandas as pd
import researchpy as rp 

df = pd.read_csv("https://raw.githubusercontent.com/NorthstarKIA/SA2-Item26-Atanacio/main/RatExploration_csvFile.csv")
df.drop('ID', axis= 1, inplace= True)

# Recoding value from numeric to string
df['Stimuli'].replace({1: 'Shape', 2: 'Pattern', 3: 'Picture'}, inplace= True)

df.info()

rp.summary_cont(df['Stimuli'])

rp.summary_cont(df['Time'].groupby(df['Stimuli']))

import scipy.stats as stats

stats.f_oneway(df['Time'][df['Stimuli'] == 'Shape'],
               df['Time'][df['Stimuli'] == 'Pattern'],
               df['Time'][df['Stimuli'] == 'Picture'])
