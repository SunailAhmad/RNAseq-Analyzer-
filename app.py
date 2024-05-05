import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate dummy data
data = {
    'A': np.random.randn(100),
    'B': np.random.rand(100) * 100,
    'C': np.random.choice(['X', 'Y', 'Z'], 100),
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
st.write("First few rows of the DataFrame:")
st.write(df.head())

# Perform descriptive analysis
st.write("Descriptive statistics of the DataFrame:")
st.write(df.describe())

# Plot some graphs
st.write("Histogram of a column:")
selected_column = st.selectbox("Select a column for histogram", df.columns)
fig, ax = plt.subplots()
ax.hist(df[selected_column], bins=20, color='skyblue', edgecolor='black')
st.pyplot(fig)

st.write("Pairplot of selected columns:")
selected_columns = st.multiselect("Select columns for pairplot", df.columns)
fig, ax = plt.subplots()
sns.pairplot(df[selected_columns])
st.pyplot(fig)
