import streamlit as st
import pandas

df = pandas.read_csv('data.csv', sep=';')
df_len = int(len(df))
col1_pos = int(df_len / 3)
col2_pos = int(2 * df_len / 3)

st.set_page_config(page_title='To Anechka with Love', page_icon="images/favicon.png", layout='wide')

st.write("<h2 style='text-align: center;'><font size='6'><font color='#66cccc' face='Tahoma, Geneva, "
         "sans-serif'><var><font color='#66cccc'>Happy Valentine&#39;s Day,</font> <font "
         "color='#DDA0DD'>Анюта</font>!</var></font></font></h2>", unsafe_allow_html=True)

st.divider()

col1_1, emp1_1, col2_1 = st.columns([3, 1, 3])
with col1_1:
    st.write("<h3><font color='#66cccc'><font size='5'><font face='Tahoma, Geneva, sans-serif'>Это Женя "
             "&#128526;</font></font></font></h3>", unsafe_allow_html=True)
    st.image(f"images/Igen.jpg")

with col2_1:
    st.write("<h3><font color='#66cccc'><font size='5'><font face='Tahoma, Geneva, sans-serif'>А это Аня "
                 "&#128131;</font></font></font></h3>", unsafe_allow_html=True)
    st.image(f"images/Park.jpg")

st.divider()

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
        st.divider()

with col2:
    for index, row in df[col1_pos:col2_pos].iterrows():
        date = str(row['date'])
        location = str(row['location'])
        description = str(row['description']).capitalize()
        st.subheader(f"{date}: {location}")
        st.text(description)
        st.image(f"images/{row['file']}")
        st.divider()

with col3:
    for index, row in df[col2_pos:].iterrows():
        date = str(row['date'])
        location = str(row['location'])
        description = str(row['description']).capitalize()
        st.subheader(f"{date}: {location}")
        st.text(description)
        st.image(f"images/{row['file']}")
        st.divider()

st.write("А сколько всего я еще не показал! А сколько всего еще будет!")
st.write("Я тебя люблю! :heart:")
