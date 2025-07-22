import time
import streamlit as st
import os
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("StreamLit Practice")
st.header("This is a Heading")
st.subheader("This is a SubHeading")
st.write("Hello 123")
st.write({"Key": "value"})
st.write(False)
st.caption("Captions")

code = """
    def greet(name):
        print("Hello, ", name)
"""
st.code(code, language="python")
st.divider()
st.image(os.path.join(os.getcwd(), "static", "thumbnail.jpg"))
st.divider()

df = pd.DataFrame(
    {
        "Name": ["Rohith", "Aadithya", "Karthik", "Abhishek"],
        "Age": [20, 20, 20, 20],
        "Occupation": ["Engineer", "Engineer", "Engineer", "Engineer"],
    }
)

# st.write(df)
st.subheader("Data frame")
st.dataframe(df)

st.subheader("Data editor")
edited_df = st.data_editor(df)
# print(edited_df)

st.subheader("Static Table")
st.table(df)

st.subheader("Mstrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df["Age"].mean()))
st.divider()

st.subheader("JSON and dictionary")
simple_dict = {
    "Name": "Rohith",
    "Age": 19,
    "Skills": ["Python", "Java"],
}
st.json(simple_dict)
st.divider()

st.header("Charts in Streamlit")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.dataframe(chart_data)

st.subheader("area_chart")
st.area_chart(chart_data)

st.subheader("line_chart")
st.line_chart(chart_data)

st.subheader("bar_chart")
st.bar_chart(chart_data)

st.subheader("scatter_chart")
scatter_data = pd.DataFrame(
    {
        "x": np.random.randn(100),
        "y": np.random.randn(100),
    }
)
st.scatter_chart(scatter_data)

st.subheader("Map - Random points in Mangalore")
mnglr_lat = 12.9141
mnglr_lon = 74.8560
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [mnglr_lat, mnglr_lon], columns=["lat", "lon"]
)
st.map(map_data)

st.subheader("PyPlot")
flg, ax = plt.subplots()
ax.plot(chart_data["A"], label="A")
ax.plot(chart_data["B"], label="B")
ax.plot(chart_data["C"], label="C")
ax.set_title("Pyplot line chart")
st.pyplot(flg)

st.divider()

st.header("Form")
form_value = {
    "name": None,
    "age": None,
    "gender": None,
    "dob": None,
}
min_date = datetime(1990, 1, 1)
max_date = datetime.now()
with st.form(key="user_info"):
    form_value["name"] = st.text_input("Enter your name: ")
    form_value["age"] = st.number_input("Enter your age: ")
    form_value["gender"] = st.radio("Gender", ["MALE", "FEMALE"])
    form_value["dob"] = st.date_input(
        "Enter your D. O. B. ", min_value=min_date, max_value=max_date
    )
    submit_btn = st.form_submit_button()
    if submit_btn:
        if not all(form_value.values()):
            st.warning("Please fill all details")
        else:
            st.balloons()
            st.write("### Your Info")
            for key, value in form_value.items():
                st.write(f"{key.capitalize()}: {value}")
st.divider()

st.header("Sessions")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1
    st.write(f"Counter increment to {st.session_state.counter}")
if st.button("reset"):
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")

st.divider()

st.header("Callbacks")

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}


def go_to_Step2(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2


def go_to_Step1():
    st.session_state.step = 1


if st.session_state.step == 1:
    st.subheader("Part 1: info")
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))
    # if st.button("next"):
    #     # st.session_state.info["name"] = name
    #     # st.session_state.step = 2
    st.button("next", on_click=go_to_Step2, args=(name,))  # callback

elif st.session_state.step == 2:
    st.subheader("Part 2: review")
    st.subheader("Please review this")
    st.write(f"**NAME**: {st.session_state.info.get("name","")}")
    if st.button("Submit"):
        st.success("Geart!!")
        st.balloons()
        st.session_state.info = {}

    # if st.button("back"):
    #     st.session_state.step = 1
    st.button("back", on_click=go_to_Step1)

st.divider()

st.header("Layouts")
st.sidebar.title("Sidebar")
st.sidebar.write("Hello this text in sidebar")
sidebar_input = st.sidebar.text_input("Enter something in sidebar")

tab1, tab2, tab3 = st.tabs(["TAB1", "TAB2", "TAB3"])

with tab1:
    st.write("You are in tab 1")
with tab2:
    st.write("You are in tab 2")
with tab3:
    st.write("You are in tab 3")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Content of column 1")
with col2:
    st.header("Column 2")
    st.write("Content of column 2")

with st.container(border=True):
    st.write("This like a div in html.")
    st.write("Can be used do contain elements")

placeholder = st.empty()
placeholder.write("Something can be written here")

if st.button("Update placeholder"):
    placeholder.write("Updated text")

with st.expander("Expand for more details"):
    st.write("1. Nothing much important here")
    st.write("2. Nothing much important here")


st.caption("Hover over the below button for a tooltip")
st.text_input("Help", help="Hey there this is help button")

st.divider()

st.header("Advanced Widgets features")

if "check" not in st.session_state:
    st.session_state.check = False


def toggle_input():
    st.session_state.check = not st.session_state.check


st.checkbox("Show input field", value=st.session_state.check, on_change=toggle_input)

if st.session_state.check:
    user_input = st.text_input("Enetr something", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")

st.write(f"User input: {user_input}")
st.divider()

st.header("Caching")

@st.cache_data(ttl=60)
def fetch_data():
    time.sleep(3)
    return {'data': 'Nothing'}

st.write("Fetching....")
data = fetch_data()
st.write(data)

st.divider()


st.header("Fragments")
@st.fragment()
def fragmented_elemts():
    cols = st.columns(2)
    cols[0].toggle("Toggle Me")
    cols[1]._text_area("Toggle Me")
    # st.rerun(scope='app')
    # st.rerun(scope='fragment')

fragmented_elemts()

st.divider()
st.header("Multipage")
st.write("In Home Page ")
