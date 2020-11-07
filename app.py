import datetime as dt
import re

import pandas as pd
import streamlit as st
from flair.data import Sentence
from flair.models import TextClassifier


# Set page title
st.title('Sentiment Analysis')

# Load classification model
with st.spinner('Loading classification model...'):
    classifier = TextClassifier.load('/Users/mengyu/Desktop/engineering/models/best-model.pt')

# Preprocess function
allowed_chars = ' AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789~`!@#$%^&*()-=_+[]{}|;:",./<>?'
punct = '!?,.@#'
maxlen = 280

def preprocess(text):
    # Delete URLs, cut to maxlen, space out punction with spaces, and remove unallowed chars
    return ''.join([' ' + char + ' ' if char in punct else char for char in [char for char in re.sub(r'http\S+', 'http', text, flags=re.MULTILINE) if char in allowed_chars]])


# Get sentence input, preprocess it, and convert to flair.data.Sentence format
tweet_input = st.text_input('Please input your sentence:')

st.button('Submit')

if tweet_input != '':
    # Pre-process
    sentence = Sentence(preprocess(tweet_input))

    # Make predictions
    with st.spinner('Predicting...'):
        classifier.predict(sentence)

    # Show predictions
    label_dict = {'0': 'Negative', '4': 'Positive'}

    if len(sentence.labels) > 0:
        st.write('Prediction:')
        st.write(label_dict[sentence.labels[0].value] + ' with ',
                sentence.labels[0].score*100, '% confidence')
