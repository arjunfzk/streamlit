# Core Pkgs
import streamlit as st # NLP Pkgs
import spacy_streamlit
import spacy
nlp = spacy.load('en_core_web_sm')

import requests







def main():
    """A Simple NLP app with Spacy-Streamlit"""
    st.title("Spacy-Streamlit NLP App  ")
    menu = ["NER"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "NER":
                    st.subheader("Named Entity Recognition use words like coronavirus, elonmusk,laptop etc It may show error for some words due to disambiguation")
                    raw_text = st.text_area("")
                    if len(raw_text)>1:
                        print(raw_text)
                        url='https://flaskarjun.herokuapp.com/'+raw_text
                        response = requests.get(url)
                        raw_text=response.json()['data']

                    docx = nlp(raw_text)
                    spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)

















if __name__ == '__main__':
    main()
