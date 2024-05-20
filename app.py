import streamlit as st
from dotenv import load_dotenv 

load_dotenv()
import os
import google.generativeai as genai
from pytube import extract 
from transcript import extract_transcript_details , generate_gemini_content

from youtube_transcript_api import YouTubeTranscriptApi

st.title("Youtube Videos to notes converter")
youtube_link = st.text_input("Enter Youtube Video Link:")

prompt =  """You are Youtube Video summarizer.You will take the trascript text and summarize the entire video 
    and provide the important summary in points within 400 words Please provide the summary of the text given here"""

if st.button("Generate notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text,prompt)
        id= extract.video_id(youtube_link)
        st.image(f"http://img.youtube.com/vi/{id}/0.jpg", use_column_width=True)
        st.markdown("## Detailed Notes:")
        st.write(summary)