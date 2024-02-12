import streamlit as st
import pandas

df = pandas.read_csv('data.csv', sep=';')
df_len = int(len(df))
col1_pos = int(df_len/3)
col2_pos = int(2*df_len/3)

st.set_page_config(page_title='To Anechka with Love', layout='wide')
st.header("Happy Valentine's day")

col1_1, emp1_1, col2_1 = st.columns([3, 1, 3])
with col1_1:
    st.subheader("Это Женя")
    st.image(f"images/Igen.jpg")

with col2_1:
    st.subheader("А это Аня")
    st.image(f"images/Park.jpg")

st.title("А дальше будут Мы")
st.title("")

col1, emp1, col2, emp2, col3 = st.columns([3, 1, 3, 1, 3])

with col1:
    for index, row in df[:col1_pos].iterrows():
        date = str(row['date'])
        location = str(row['location'])
        description = str(row['description']).capitalize()
        st.subheader(f"{date}: {location}")
        st.text(description)
        st.image(f"images/{row['file']}")

with col2:
    for index, row in df[col1_pos:col2_pos].iterrows():
        date = str(row['date'])
        location = str(row['location'])
        description = str(row['description']).capitalize()
        st.subheader(f"{date}: {location}")
        st.text(description)
        st.image(f"images/{row['file']}")

with col3:
    for index, row in df[col2_pos:].iterrows():
        date = str(row['date'])
        location = str(row['location'])
        description = str(row['description']).capitalize()
        st.subheader(f"{date}: {location}")
        st.text(description)
        st.image(f"images/{row['file']}")