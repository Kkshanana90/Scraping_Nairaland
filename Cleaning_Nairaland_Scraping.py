#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np

full_data= pd.read_csv('Nairaland_df.csv',lineterminator='\n')
full_data.head(20)


# In[ ]:



def examine(comments):
    if comment== np.nan or comments == None or len(comments.split()) < 2:
        return False
    else:
        return True


# In[ ]:


mask = df.loc[:, 'Comments'].map(examine)
df_clean = df[mask]
df_clean

