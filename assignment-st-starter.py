# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()



# show the title

st.title('Your Full Name - Titanic Data Analysis')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.write(df.head())


# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below



fig, axes = plt.subplots(1, 3, figsize=(15, 5))


sns.boxplot(data=df[df['Pclass'] == 1], y='Fare', ax=axes[0])
axes[0].set_title('Ticket Prices - Class 1')
axes[0].set_xlabel('Class 1')
axes[0].set_ylabel('Fare')

sns.boxplot(data=df[df['Pclass'] == 2], y='Fare', ax=axes[1])
axes[1].set_title('Ticket Prices - Class 2')
axes[1].set_xlabel('Class 2')
axes[1].set_ylabel('Fare')

sns.boxplot(data=df[df['Pclass'] == 3], y='Fare', ax=axes[2])
axes[2].set_title('Ticket Prices - Class 3')
axes[2].set_xlabel('Class 3')
axes[2].set_ylabel('Fare')


st.pyplot(fig)

