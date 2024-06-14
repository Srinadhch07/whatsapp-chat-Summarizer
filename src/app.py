import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
#Load environmental varibles.
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(
model_name="gemini-1.0-pro")
convo = model.start_chat(history=[]) 
#Reading the whatsapp chatfile

def text_extraction(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        text = file.read()
        return text



#Response tuning
prompt="""You are a Chat Summerizer. You will take the conersation of two people and analyses it. After analysing the conversion,
         you provides the summary of conversation as key points  by dividing converstions day to day and topic by topic.
        Please provide the summary of below conversion:\n """

def tuning_response(text):
    convo.send_message(prompt+text)
    response=str(convo.last.text)
    return response
st.title("Whatsapp Chat Summerizer")
path=st.text_input("Provide the Path of File: ") 
if path:
    coversation=text_extraction(path)
    summary=tuning_response(coversation)
    st.markdown("## Conversation Summary")
    st.write(summary)


