import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

GOOGLE_API_KEY = 'AIzaSyBn_FRq9m89xNgOGoADxGHGD3V8uuEWLqw'

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

#tweet_prompt = PromptTemplate.from_template("You are a content creator. Write me a tweet about {topic}.")
tweet_prompt = PromptTemplate.from_template("Tell me about celebrity {name}")

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)

def generate_tweet(name):
    return tweet_chain.run(name=name)

st.title("AI Tweet Generator")

name = st.text_input("Enter the  name:", "how AI is really cool")
if st.button("Generate name"):
    tweet = generate_tweet(name)
    st.write("Generated Tweet:")
    st.write(tweet)

'''
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

tweet_prompt = PromptTemplate.from_template("You are a content creator. Write me a tweet about {topic}.")

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)

def generate_tweet(topic):
    return tweet_chain.run(topic=topic)

st.title("AI Tweet Generator")

topic = st.text_input("Enter the topic:", "how AI is really cool")
if st.button("Generate Tweet"):
    tweet = generate_tweet(topic)
    st.write("Generated Tweet:")
    st.write(tweet)

'''

