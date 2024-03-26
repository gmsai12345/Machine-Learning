import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.memory import ConversationBufferMemory
GOOGLE_API_KEY = 'AIzaSyBn_FRq9m89xNgOGoADxGHGD3V8uuEWLqw'
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
#tweet_prompt = PromptTemplate.from_template("You are a content creator. Write me a tweet about {topic}.")
tweet_prompt = PromptTemplate.from_template("Tell me about celebrity {name}")
nameprompt = PromptTemplate.from_template("when was {name} born")
tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True,output_key='person')
dobchain= LLMChain(llm=llm, prompt=nameprompt, verbose=True,output_key='dob')
# can run one by one or use SimpleSequentialChain
parent_chain=SimpleSequentialChain(chains=[tweet_chain,dobchain],verbose=True)
'''def generate_detail(name):
  return parent_chain.run(name=name)
'''
st.title("cebrity detail generator")

name = st.text_input("Enter the name:")
if name:
    st.write(parent_chain.run(name))

