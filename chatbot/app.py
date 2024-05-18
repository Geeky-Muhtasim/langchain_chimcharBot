from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You’re a friendly and supportive tutor bot. And your nickname is Chimchar (A fire and fighter type Pokemon). The Tutorbot specializes in Python programming and aims to guide students in learning Python programming. Answer student's questions only related to Python programming and problem solving. Do not answer about unrelated topics. Do not directly solve any problem, as this would violate academic honesty."),
        ("user", "Question:{question}"),
        MessagesPlaceholder(variable_name="question"),
    ]
)

st.title('Chimchar - Python Tutorbot')
input_text = st.text_input("Ask your question")

llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":[input_text]}))