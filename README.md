# 🚀 AI Resume Screener (Deployed ML Application)

🔗 **Live App:** https://ai-resume-screener-5fw82amunqbkrudru4x37a.streamlit.app  
🔗 **GitHub Repo:** https://github.com/VadaboinaSowjanya/ai-resume-screener  

---

## 📌 Overview
AI Resume Screener is an end-to-end Machine Learning application that classifies resumes into job categories using Natural Language Processing (NLP).

The system supports both **PDF resume uploads** and **text input**, making it practical for real-world recruitment scenarios.

---

## 🧠 Problem Statement
Recruiters receive thousands of resumes for different roles, and manually screening them is:
- Time-consuming ⏳  
- Inefficient ❌  
- Error-prone ⚠️  

This project automates resume screening by predicting the **most relevant job category** based on resume content.

---

## ⚙️ Tech Stack
- Python  
- Pandas & NumPy  
- Scikit-learn  
- NLP (TF-IDF Vectorization)  
- LinearSVC (Support Vector Machine)  
- Streamlit (Web App Deployment)  
- PyPDF2 (PDF parsing)  

---

## 🔄 Workflow
1. Load large-scale resume dataset  
2. Clean and preprocess text data  
3. Convert text → numerical features using TF-IDF  
4. Split data into training & testing sets  
5. Train model using LinearSVC  
6. Evaluate model performance  
7. Save model using Pickle  
8. Build UI using Streamlit  
9. Deploy app on Streamlit Cloud  

---

## 📊 Features
✅ Upload resume in **PDF format**  
✅ Paste resume text manually  
✅ Real-time prediction  
✅ Clean and interactive UI  
✅ Deployed and accessible online  

---

## 📈 Model Performance
- Algorithm: **LinearSVC (SVM)**
- Accuracy: **~75%+**
- Trained on a **large dataset for better generalization**

---

## 🧪 How It Works
- Resume text is cleaned and preprocessed  
- TF-IDF converts text into numerical vectors  
- Model learns patterns between resume content & job roles  
- Predicts category for new resumes instantly  

---

## 🔥 Key Learnings
- End-to-end ML pipeline development  
- NLP techniques for text classification  
- Model deployment using Streamlit  
- Handling real-world input (PDF resumes)  
- GitHub + Cloud deployment workflow  

---

## 🚀 Future Improvements
- Improve accuracy using advanced models (BERT, Transformers)  
- Add confidence score for predictions  
- Implement job-role recommendation system  
- Store results using database  
- Enhance UI/UX  

---

## 👩‍💻 Author
**Sowjanya Vadaboina**  

---

## ⭐ If you like this project
Give it a ⭐ on GitHub and share your feedback!
