import streamlit as st
import pandas as pd

def create_expanding_section(title, content):
    """Create an expandable section for detailed content"""
    with st.expander(title):
        st.markdown(content)
