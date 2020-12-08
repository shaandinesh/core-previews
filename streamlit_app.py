import streamlit as st

st.title("Slider")

v1 = st.slider("Label 1", 0, 100, 25, 1)
st.write("Value:", v1)

st.title("Multiselect")

v2 = st.multiselect("selectbox 4", ["coffee", "tea", "water"], ["tea", "water"])
st.text("Value: %s" % v2)
