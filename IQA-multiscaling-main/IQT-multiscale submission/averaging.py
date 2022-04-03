# -*- coding: utf-8 -*-
"""Averaging.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16CKCua3a6LSzWbyNxNJDCe3L5UxWVE1X
"""

import pandas as pd

#We have mannualy added the column name A,B for the reference
df1 = pd.read_csv("outputScale0.5.txt")
df2 = pd.read_csv("outputScale1.txt")
df3 = pd.read_csv("outputScale2.txt")
df4 = pd.read_csv("outputScale3.txt")
df5 = pd.concat([df1['A'],(df1['B'] + df2['B'] + df3['B']+df4['B'])/4],axis = 1)
df5.to_csv("output.txt", index = False)
#After saving the output file one can remove the first like containing A and B as column name
