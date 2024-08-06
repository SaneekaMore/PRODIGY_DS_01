#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas matplotlib seaborn Pillow


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np

csv_path = r"C:\Users\Saneeka\Downloads\train.csv"
dataset = pd.read_csv(csv_path)

# Bar chart for Sex vs. Survived
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(bg_image, aspect='auto', extent=ax.get_xlim() + ax.get_ylim(), zorder=-1)
sns.countplot(data=dataset, x='Sex', hue='Survived', palette='viridis', ax=ax)
ax.set_title('Survival Count by Gender', fontsize=16)
ax.set_xlabel('Gender', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.legend(title='Survived', fontsize=12, title_fontsize=14)
plt.show()


# In[8]:


# Histogram for Age
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(bg_image, aspect='auto', extent=ax.get_xlim() + ax.get_ylim(), zorder=-1)
sns.histplot(dataset['Age'].dropna(), bins=20, kde=True, color='black', ax=ax)
ax.set_title('Age Distribution', fontsize=16)
ax.set_xlabel('Age', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)
plt.show()


# In[ ]:




