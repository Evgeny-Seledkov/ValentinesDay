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
    st.write("<h3 align='center'><font color='#66cccc'><font size='5'><font face='Tahoma, Geneva, sans-serif'>Это Женя "
             "&#128526;</font></font></font></h3>", unsafe_allow_html=True)
    st.image(f"images/Igen.jpg")

with col2_1:
    st.write("<h3 align='center'><font color='#66cccc'><font size='5'><font face='Tahoma, Geneva, sans-serif'>А это Аня "
                 "&#128131;</font></font></font></h3>", unsafe_allow_html=True)
    st.image(f"images/Park.jpg")

st.divider()

st.title("А дальше будут :blue[фото]!")
st.subheader("Просто напомню тебе, чем :rainbow[МЫ] "
             "занимались последние 3 года :man_and_woman_holding_hands:", anchor=False)

st.divider()


col1, emp1, col2, emp2, col3 = st.columns([3, 1, 3, 1, 3])

with col1:
    st.header(":blue[Часть 1] :arrow_down:", divider=True)
    for index, row in df[:col1_pos].iterrows():
        date = str(row['date'])
        location = str(row['location'])
        description = str(row['description'])
        st.subheader(f"{date}: {location}")
        st.text(description)
        st.image(f"images/{row['file']}")
        st.divider()

with col2:
    st.header(":blue[Часть 2] :arrow_down:", divider=True)
    for index, row in df[col1_pos:col2_pos].iterrows():
        date = str(row['date'])
        location = str(row['location'])
        description = str(row['description'])
        st.subheader(f"{date}: {location}")
        st.text(description)
        st.image(f"images/{row['file']}")
        st.divider()

with col3:
    st.header(":blue[Часть 3] :arrow_down:", divider=True)
    for index, row in df[col2_pos:].iterrows():
        date = str(row['date'])
        location = str(row['location'])
        description = str(row['description'])
        st.subheader(f"{date}: {location}")
        st.text(description)
        st.image(f"images/{row['file']}")
        st.divider()

st.write("<address style='text-align: center;'><font color='#333399'><font size='4'><samp>"
         "А сколько всего я еще не показал! А сколько всего еще будет!</samp></font></font></address>",
         unsafe_allow_html=True)
st.write("<address style='text-align: center;'><font size='6'><font color='#333399'><samp>"
         "Я тебя &#129655;!</samp></font></font></address>",
         unsafe_allow_html=True)
