from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
import fitz  # PyMuPDF
import io

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

def get_gemini_response(input_text, pdf_content, prompt):
    # You can change this to gemini-1.5-flash or gemini-3.5-flash as per your setup
    model = genai.GenerativeModel('gemini-3.5-flash')
    
    # Send Job description (if provided), PDF image, and the specific prompt template
    if input_text.strip():
        response = model.generate_content([input_text, pdf_content[0], prompt])
    else:
        response = model.generate_content([pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            # Read the PDF using PyMuPDF
            doc = fitz.open(stream=uploaded_file.getvalue(), filetype="pdf")
            
            # For simplicity, let's take the first page of the resume
            page = doc.load_page(0)
            
            # Convert the page to an image
            pix = page.get_pixmap()
            img_byte_arr = pix.tobytes("jpeg")

            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": img_byte_arr
                }
            ]
            return pdf_parts
        except Exception as e:
            st.error(f"Error processing PDF: {e}")
            raise e
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize our Streamlit app
st.set_page_config(page_title="ATS Resume Expert")
st.title("Smart ATS Resume Analyzer")
st.header("Optimize Your Resume with Gemini")

input_text = st.text_area("Job Description (Optional): ", key="input", height=200)
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

col1, col2, col3 = st.columns(3)
with col1:
    submit1 = st.button("What to Change / Improve")
with col2:
    submit2 = st.button("How is my Resume?")
with col3:
    submit3 = st.button("Percentage Match")

# Prompt Templates (With JD)
input_prompt1 = """
You are an expert career coach and ATS (Applicant Tracking System) specialist. 
Based on the provided resume image and the job description, evaluate the resume and tell the user how they can improve their skills and resume. 
- What specific skills or areas should they focus on? 
- What should they change in their resume to better align with the job description? 
- What is better to add or remove? 
Please give concrete, actionable advice.
"""

input_prompt2 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science, software engineering, and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches the job description. 
First the output should come as a percentage and then keywords missing and last final thoughts.
"""

# Prompt Templates (Without JD)
input_prompt_improve_general = """
You are an expert career coach and ATS (Applicant Tracking System) specialist. 
Based on the provided resume image, evaluate the resume and tell the user how they can improve it in general.
- What specific skills or areas could be presented better?
- What should they change in their resume to make it stand out to recruiters?
- Are there formatting, structural, or content issues?
Please give concrete, actionable advice.
"""

input_prompt_overview = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume.
Please share a general overview of the candidate's profile.
Highlight their core strengths, primary skills, potential career trajectory, and any notable weaknesses or gaps in the resume.
"""

# Handle button clicks
if submit1:
    if uploaded_file is not None:
        with st.spinner("Analyzing your resume..."):
            pdf_content = input_pdf_setup(uploaded_file)
            prompt = input_prompt1 if input_text.strip() else input_prompt_improve_general
            response = get_gemini_response(input_text, pdf_content, prompt)
            st.subheader("Recommendations & Improvements")
            st.write(response)
    else:
        st.warning("Please upload the resume.")

elif submit2:
    if uploaded_file is not None:
        with st.spinner("Evaluating your profile..."):
            pdf_content = input_pdf_setup(uploaded_file)
            prompt = input_prompt2 if input_text.strip() else input_prompt_overview
            response = get_gemini_response(input_text, pdf_content, prompt)
            st.subheader("HR Evaluation / Overview")
            st.write(response)
    else:
        st.warning("Please upload the resume.")

elif submit3:
    if uploaded_file is not None:
        if input_text.strip():
            with st.spinner("Calculating match percentage..."):
                pdf_content = input_pdf_setup(uploaded_file)
                response = get_gemini_response(input_text, pdf_content, input_prompt3)
                st.subheader("ATS Match Results")
                st.write(response)
        else:
            st.warning("Please provide a Job Description to calculate the Percentage Match.")
    else:
        st.warning("Please upload the resume.")
