from pathlib import Path
import pandas as pd
import streamlit as st

st.title("Maiden väkiluvut")
st.write("Data luetaan puhdistetusta tiedostosta `tpl-dkp-muuntaminen/data/countries_cleaned.json`.")

data_path = Path(__file__).resolve().parents[2] / "tpl-dkp-muuntaminen" / "data" / "countries_cleaned.json"
df = pd.read_json(data_path)

top_n = st.slider("Montako suurinta maata näytetään", min_value=5, max_value=30, value=10)
top_df = df.sort_values(by="population", ascending=False).head(top_n)

st.subheader(f"Top {top_n} maata väkiluvun mukaan")
st.dataframe(top_df, hide_index=True)

st.subheader("Väkiluku maittain")
st.bar_chart(top_df.set_index("name")["population"])
