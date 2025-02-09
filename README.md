# LangChain: Summarize Text from YouTube or Website

This is a Streamlit-based application that uses LangChain, Groq API, and other libraries to summarize content from either a YouTube video or a website URL. The app extracts text (e.g., video transcripts or webpage content) and generates a concise summary using a language model.

## Features
- Extracts YouTube video details and subtitles using `yt-dlp`.
- Loads webpage content using `UnstructuredURLLoader`.
- Summarizes the extracted content using LangChain's `ChatGroq` and a custom prompt template.
- User-friendly interface built with Streamlit.

## Prerequisites
- Python 3.8 or above
- A valid Groq API key
- Installed dependencies from `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/langchain-summarizer.git
   cd langchain-summarizer
