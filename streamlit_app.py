import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

st.success('Strona poprawnie załadowana!')
st.image("image.png")

st.title('Prezentacja modelu do tłumaczenia oraz analizy tekstu')

st.header('Wprowadzenie 👋')

st.write('Jest to przykładowa aplikacja z wykorzystaniem Streamlit.')
st.write('Pozwala ona na skorzystanie z dwóch modeli.')
st.write('\t**sentiment-analysis** pozwalającego na analizę danego słowa/zdania (po angielsku) pod względem jego wydźwięku emocjonalnego')
st.write('\t**google-t5/t5-base** służącego do przetłumaczenia zdań w języku angielskim na niemiecki')

st.header('Analizator wydźwięku emocjonalnego tekstu 😃😡')
st.subheader('sentiment-analysis')
st.write('By skorzystać z analizatora wprowadź tekst do pola poniżej.')
st.write('Następnie kliknij przycisk *Run*')
st.write('Po chwili wyświetli Ci się wynik')
st.write('POSITIVE oznacza, że słowo/zdanie ma wydźwięk pozytywny')
st.write('NEGATIVE zaś, że negatywny')
st.write('Value wyświetlana niżej oznacza jak bardzo dany tekst ma wydźwięk pozytywny/negatywny')

import streamlit as st
from transformers import pipeline

text_analise = st.text_area(label="Wpisz tekst do analizy")
if(st.button('Run',key="b1")):
    classifier = pipeline("sentiment-analysis")
        
    st.spinner()
    with st.spinner(text='Analizuję...'):
        answer = classifier(text_analise)
    a_label = answer[0]["label"]
    a_value = round(answer[0]["score"] * 100,2)
    if a_label == "POSITIVE":
        st.markdown(f'<span style="color:green">{a_label}</span>', unsafe_allow_html=True)
    else:
        st.markdown(f'<span style="color:red">{a_label}</span>', unsafe_allow_html=True)
    st.slider("Value %", 0.0, 100.0, a_value, disabled=True)

st.header('Tłumacz z języka angielskiego na niemiecki 🇬🇧➡️🇩🇪')
st.subheader('google-t5/t5-base')
st.write('By skorzystać z tłumacza wprowadź tekst do pola poniżej.')
st.write('Następnie kliknij przycisk *Run*')
st.write('Po chwili wyświetli Ci się przetłumaczony tekst')

text_translate = st.text_area(label="Wpisz tekst do przetłumaczenia (ENG)")
if(st.button('Run', key="b2")):
    classifier = pipeline(model="google-t5/t5-base")
    st.spinner()
    with st.spinner(text='Tłumaczę...'):
        answer = classifier(text_translate)
    answer = answer[0]["translation_text"]
    st.write(answer)

st.subheader("s21584")
