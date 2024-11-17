import os
from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
import docx

OPENAI_API_KEY = "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"


def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])


st.title("Key Insights Generator")
st.subheader("BY PROCODEBASE AI")
input_method = st.radio(
    "How would you like to provide the story?",
    options=["Upload a File", "Type/Paste Text"],
    horizontal=True
)

story = None
if input_method == "Upload a File":
    uploaded_file = st.file_uploader("Upload a story file (txt, pdf, docx)", type=["txt", "pdf", "docx"])
    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1]
        if file_type == "txt":
            story = uploaded_file.read().decode("utf-8")
        elif file_type == "pdf":
            story = extract_text_from_pdf(uploaded_file)
        elif file_type == "docx":
            story = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file format!")
elif input_method == "Type/Paste Text":
    story = st.text_area("Type or paste your story below:")


insight_type = st.text_input("Enter the type of insight you want (e.g., productivity, career guidance)")


if st.button("Generate Insights"):
    if story and insight_type:
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_text(story)

        chat = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY, temperature=0.7)
        
        insights = []
        for chunk in chunks:
            messages = [HumanMessage(content=f"Provide key insights on {insight_type} and give some suggestion according to it:\n{chunk}")]
            response = chat(messages)  
            insights.append(response.content)  

        st.subheader("Generated Insights")
        for idx, insight in enumerate(insights, 1):
            st.write(f"**Insight {idx}:** {insight}")
    else:
        st.error("Please provide the story and specify the insight type.")
