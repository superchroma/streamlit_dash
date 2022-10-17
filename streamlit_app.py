import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import requests
import datetime
from datetime import datetime, timedelta

df = pd.read_csv("https://raw.githubusercontent.com/superchroma/streamlit_dash/main/prescreen_data.csv")
df2 = pd.read_csv('https://raw.githubusercontent.com/superchroma/streamlit_dash/main/studies_analysis.csv')
df2 = df2.drop(['short_description', 'long_description', 'private_comments'], axis=1)
df2 = df2[df2.active_flag > 0]
df3 = pd.read_csv('https://raw.githubusercontent.com/superchroma/streamlit_dash/main/signups_analysis.csv', parse_dates=True, infer_datetime_format=True)

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

percentage=len(df)/2077 *100

# create title
st.title("SONA Tracking Dashboard")

# header
st.header("Overview")

# markdown
num = len(df)
st.markdown(f"The total number of participants who have completed the SONA prescreen is: {num}")
st.markdown(f"This week, {count} new participant(s) completed the prescreen questionnaire, with {round(percentage,2)}% of the total SONA database having completed the prescreen questionnaire.")

# header
st.header("Active Studies")

# create buttons
# executes when button is clicked
# index 3
if st.button("Public Opinion Study (VANCOPPEN-1121)"):
    st.write(f'Duration of Study: {df2.duration_minutes[3]} minutes.')
    st.write(f'Number of Participants: 135')
# index 6
if st.button("Language attitudes and dialect identification in England (COLE-0422) "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[6]} minutes.')
    st.write(f'Number of Participants: 54')
# index 8
if st.button("Voting Experiment (DIANAT-0222)   "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[8]} minutes')
    st.write(f'Number of Participants: 53')
# index 9
if st.button("ENGLISH MONOLINGUALS: Interactions of first and second language (SOTOGARCIA-0122)"):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[9]} minutes')
    st.write(f'Number of Participants: 23')
# index 10
if st.button("ENGLISH-SPANISH BILINGUALS: Interactions of first and second language (SOTOGARCIA-0122) "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[10]} minutes')
    st.write(f'Number of Participants: 23')
# index 11
if st.button("SPANISH HERITAGE SPEAKERS: Interactions of first and second language (SOTOGARCIA-0122)     "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[11]} minutes')
    st.write(f'Number of Participants: 12')
# index 12
if st.button("Social processing of naturalistic social interactions - DAUGHTERS-0422  "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[12]} minutes')
    st.write(f'Number of Participants: 117')
# index 13
if st.button("ENGLISH MONOLINGUALS (2-part): Interactions of first and second language (SOTOGARCIA-0122) - Part 1 "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[13]} minutes')
    st.write(f'Number of Participants: 27')
# index 14
if st.button("ENGLISH MONOLINGUALS (2-part): Interactions of first and second language (SOTOGARCIA-0122) - Part 2   "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[14]} minutes')
    st.write(f'Number of Participants: 19')
# index 15
if st.button("SPANISH NATIVE SPEAKERS 2-part: Interactions of first and second language (SOTOGARCIA-0122) - Part 1 "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[15]} minutes')
    st.write(f'Number of Participants: 4')
# index 16
if st.button("SPANISH NATIVE SPEAKERS 2-part: Interactions of first and second language (SOTOGARCIA-0122) - Part 2 "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[16]} minutes')
    st.write(f'Number of Participants: 4')
# index 17
if st.button("Does the Beauty beat the Beast? (FULLARD-0122O)"):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[17]} minutes')
    st.write(f'Number of Participants: 0')
# index 18
if st.button("Why copy others' financial decisions? (FREER-0522)"):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[18]} minutes')
    st.write(f'Number of Participants: 25')
# index 19
if st.button("DIANAT-0522 - Conspicuous Consumption in the Lab  "):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[19]} minutes')
    st.write(f'Number of Participants: 0')
# index 21
if st.button("Decision Making Study"):
    st.write("")
    st.write(f'Duration of Study: {df2.duration_minutes[21]} minutes')
    st.write(f'Number of Participants: 0')


st.header("Studies")
val_count  = df3['experiment_name'].value_counts()
fig = plt.figure(figsize=(15,18))
sns.barplot(x=val_count.values, y=val_count.index, alpha=0.8)
plt.ylabel('Study Name', fontsize=12)
plt.xlabel('Number of Participants', fontsize=12)
st.pyplot(fig)


st.header("Participant Types")
# bar graph
val_count  = df['Q1'].value_counts()
fig = plt.figure(figsize=(10,5))
sns.barplot(x=val_count.values, y=val_count.index, alpha=0.8).set_title("Participants Signed Up By Type")
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
sns.barplot(x=val_count.values, y=val_count.index, alpha=0.8).set_title("Participants Signed Up By Course")
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
