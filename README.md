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



Install the required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file in the project directory and add your Groq API key:

ini
Copy
Edit
GROQ_API=your_groq_api_key
How to Run
Launch the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open the app in your web browser (default: http://localhost:8501).

Enter the following details:

Groq API Key: Provide your API key (or it will load from .env).
URL: Enter a valid YouTube or website URL.
Click on Summarize the Content from YT or Website to generate the summary.

Code Overview
Key Components
Dependencies:
langchain, streamlit, yt_dlp, dotenv, and others.
Input Handling:
YouTube or website URLs are validated using validators.url.
Content Extraction:
YouTube video details and transcripts are fetched using yt-dlp.
Webpage content is loaded using UnstructuredURLLoader.
Text Summarization:
LangChain's ChatGroq LLM is used for summarization with a custom prompt.
Output:
Displays a summary of the input content.
Error Handling
Validates input URL format.
Handles YouTube content extraction errors.
Displays exceptions for better debugging.
Example
Input
YouTube URL: https://www.youtube.com/watch?v=example
Website URL: https://example.com/article
Output
A concise, 600-word summary of the video transcript or webpage content.
Libraries Used
Streamlit: For building the web app interface.
LangChain: For creating and managing the summarization chain.
Groq API: To interact with the Gemma model.
yt-dlp: For fetching YouTube video details and transcripts.
dotenv: For managing environment variables.
Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

License
This project is licensed under the MIT License.

Acknowledgments
LangChain
Streamlit
yt-dlp
