import streamlit as st
import pickle
import re
import PyPDF2

# load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = re.sub(r'\b\w{1,2}\b', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# 🔥 PDF text extraction
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

st.title("AI Resume Screener 🚀")
st.write("Upload your resume (PDF) or paste text to predict category")

# 🔥 FILE UPLOAD (PDF)
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

resume_input = ""

if uploaded_file is not None:
    try:
        resume_input = extract_text_from_pdf(uploaded_file)
    except:
        st.error("Error reading PDF")

# TEXT INPUT
text_input = st.text_area("Or paste resume here")

if text_input:
    resume_input = text_input

if st.button("Predict"):
    if resume_input:
        cleaned = clean_text(resume_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)

        st.success(f"Predicted Category: {prediction[0]}")
    else:
        st.error("Please upload or paste a resume")