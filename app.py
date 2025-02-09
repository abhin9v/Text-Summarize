import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.docstore.document import Document
from dotenv import load_dotenv
import yt_dlp
import os

# Load environment variables from .env file
load_dotenv()

## Streamlit APP
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

## Get the Groq API Key and URL (YT or website) to be summarized
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value=os.getenv("GROQ_API"), type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

## Gemma Model Using Groq API
llm = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)

prompt_template = """
Provide a summary of the following content in 600 words:
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

def load_youtube_transcript(url):
    """Load transcript text from a YouTube video using yt-dlp."""
    try:
        ydl_opts = {
            'quiet': True,
            'extract_flat': False,
            'skip_download': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitlesformat': 'vtt',
            'outtmpl': '%(id)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_title = info.get('title', 'Unknown Title')
            st.info(f"Loaded video: {video_title}")
            return f"Video Title: {video_title}\nDescription: {info.get('description', '')}"
    except Exception as e:
        st.error(f"Error loading YouTube content: {e}")
        return None

if st.button("Summarize the Content from YT or Website"):
    ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YT video URL or website URL")
    else:
        try:
            with st.spinner("Waiting..."):
                ## Loading the website or YT video data
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    content_text = load_youtube_transcript(generic_url)
                    if not content_text:
                        st.error("Failed to extract content from the YouTube video.")
                        st.stop()
                    docs = [Document(page_content=content_text)]
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url], ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                    )
                    docs = [Document(page_content=doc.page_content) for doc in loader.load()]

                ## Chain For Summarization
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)

                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception: {e}")