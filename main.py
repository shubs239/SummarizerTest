import streamlit as st
#import pandas as pd
#import numpy as np
from transformers import pipeline
#import os
#from io import StringIO

st.title('Please upload the file which you want to summarize.')



#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
    # To read file as bytes:
    #bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    #string_data = stringio.read()
    #st.write(string_data)

#summarizer = pipeline("summarization")
#summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
def summarize_text(text: str, max_len: int) -> str:
    #try:
        summary = summarizer(text, max_length=max_len, min_length=10, do_sample=False)
        return summary[0]["summary_text"]
    #except IndexError as ex:
        
        #return summarize_text(text=text[:(len(text) // 2)], max_len=max_len//2) + summarize_text(text=text[(len(text) // 2):], max_len=max_len//2)





txt = st.text_area('Text to analyze')

pressed = False
if(st.button("Generate Summary")):
    pressed=True
st.write("""
#Here's your Summary
""")


if(pressed):
    st.write(summarize_text(txt,1024))



