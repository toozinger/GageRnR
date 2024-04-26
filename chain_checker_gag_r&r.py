#!/usr/bin/env python3
"""Example showing how to use GageRnR."""
from GageRnR import GageRnR
import numpy as np

import pandas as pd

# Read the Excel file
excel_file = r'C:\Users\dowdt\OneDrive - purdue.edu\TestRig\Research\Chain wear checker\gage_rr_data.xlsx'
df = pd.read_excel(excel_file, sheet_name='regime_2_simulated',
                   usecols='B:N', skiprows=2, nrows=14)

# trim nan data
df = df.dropna(axis=1, how='all')
df = df.dropna(axis=0, how='all')

# sort by operator
df = df.sort_values("operator")

# Print the DataFrame
# print(df)

data = []
for operator in df["operator"].unique():

    subset = df[df["operator"] == operator]
    print(subset)
    data.append(subset.iloc[:, 3:].to_numpy())


data = np.array(data)

# data = np.array(            #
#     [[[3.29, 3.41, 3.64],   # p1 | o1
#       [2.44, 2.32, 2.42],   # p2
#       [4.34, 4.17, 4.27],   # p3
#       [3.47, 3.5, 3.64],    # p4
#       [2.2, 2.08, 2.16]],   # p5
#      [[3.08, 3.25, 3.07],   # p1 | o2
#       [2.53, 1.78, 2.32],   # p2
#       [4.19, 3.94, 4.34],   # p3
#       [3.01, 4.03, 3.2],    # p4
#       [2.44, 1.8, 1.72]],   # p5
#      [[3.04, 2.89, 2.85],   # p1 | o3
#       [1.62, 1.87, 2.04],   # p2
#       [3.88, 4.09, 3.67],   # p3
#       [3.14, 3.2, 3.11],    # p4
#       [1.54, 1.93, 1.55]]])  # p5

# print(data)
g = GageRnR(data)
g.calculate()
print(g.summary())
