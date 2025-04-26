import streamlit as st
import pandas as pd
import time
from datetime import datetime
# from streamlit_autorefresh import st_autorefresh


current_time =time.time()
date_record = datetime.fromtimestamp(current_time).strftime('%d-%m-%Y')
time_record = datetime.fromtimestamp(current_time).strftime('%H-%M-%S')
df = pd.read_csv("Attendence\\Attendence_"+date_record+ ".csv")


### implement auto refresh

# count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# if count == 0:
#     st.write("Count is zero")
# elif count % 3 == 0 and count % 5 == 0:
#     st.write("FizzBuzz")
# elif count % 3 == 0:
#     st.write("Fizz")
# elif count % 5 == 0:
#     st.write("Buzz")
# else:
#     st.write(f"Count: {count}")

col1, spacer, col2 = st.columns([5, 1, 5]) 


with col1:
    st.image("background webapp.png")

with col2:
    st.subheader("Attendence Data")
    st.dataframe(df.style.highlight_max(axis =0))

