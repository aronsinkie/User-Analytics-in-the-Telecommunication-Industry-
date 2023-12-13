import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px
from ADD import db_execute_fetch

st.set_page_config(page_title="Day 5", layout="wide")

def loadData():
    query = "SELECT * FROM xdr_data"
    df = db_execute_fetch(query, dbName="telecome", rdf=True)
    return df
print(loadData())
