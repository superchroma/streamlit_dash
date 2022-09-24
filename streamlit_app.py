import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import requests
import datetime
from datetime import datetime, timedelta

df = pd.read_csv("https://raw.githubusercontent.com/superchroma/streamlit_dash/main/prescreen_data.csv")

# date time
today = st.date_input(f"Date: {datetime.now()}")
# 200 for a successful response or 500 for a server error.
response_API = requests.get('https://essexlab.sona-systems.com/services/SonaAPI.svc?singleWsdl')
print(response_API.status_code)
st.markdown(f"API Status Code: {response_API.status_code}")


df = df.drop('start_time', axis=1)
df['end_time'] = pd.to_datetime(df['end_time'])
count=0
for i in range(len(df)):
  if df['end_time'][i] >= (datetime.now() - timedelta(days=7)):
    count+=1
print(count)

percentage=len(df)/1892 *100

# create title
st.title("SONA Migration Tracking Dashboard")

# header
st.header("Overview")

# markdown
num = len(df)
st.markdown(f"The total number of participants who have completed the SONA prescreen is: {num}")
st.markdown(f"This week, {count} new participant(s) completed the prescreen questionnaire, with {round(percentage,2)}% of the total SONA database having completed the prescreen questionnaire.")

st.header("Participant Types")
# bar graph
val_count  = df['Q1'].value_counts()
fig = plt.figure(figsize=(10,5))
sns.barplot(x=val_count.index, y=val_count.values, alpha=0.8).set_title("Participants Signed Up By Type")
plt.title('Participants Signed Up By Type')
plt.ylabel('Number of Participants', fontsize=12)
plt.xlabel('Participant Type', fontsize=12)
st.pyplot(fig)

st.header("By Student Types")
val_count  = df['Q19'].value_counts()
fig = plt.figure(figsize=(13,10))
sns.barplot(x=val_count.values, y=val_count.index, alpha=0.8).set_title("Participants Signed Up By Student Type")
plt.ylabel('Participant Type', fontsize=12)
plt.xlabel('Number of Student Type', fontsize=12)
st.pyplot(fig)

st.header("By Courses")
val_count  = df['Q20'].value_counts()
fig = plt.figure(figsize=(13,10))
sns.barplot(val_count.values, val_count.index, alpha=0.8).set_title("Participants Signed Up By Course")
plt.ylabel('Participant Type', fontsize=12)
plt.xlabel('Number of Student Type', fontsize=12)
st.pyplot(fig)

st.header("By Gender")
val_count  = df['Q3'].value_counts()
fig = plt.figure(figsize=(13,10))
sns.barplot(x=val_count.values, y=val_count.index, alpha=0.8).set_title("Participants Signed Up By Gender")
plt.ylabel('Gender', fontsize=12)
plt.xlabel('Participants', fontsize=12)
st.pyplot(fig)


#if __name__ == "__main__":
 #   main()