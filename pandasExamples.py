#import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

file = r"C:\Users\Michael\Downloads\data.csv"

df = pd.read_csv(file)
#df.plot(kind = 'line', color="red")
colours=["red","gold","green"]
for col in colours: 
    df['Age'].plot(kind='hist',color=col)
plt.show()

