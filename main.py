import sys
from transcript import get_transcript
from summarizer import OllamaSummarizer

if __name__ == "__main__":
    
    url = sys.argv[1]
    print(f"URL: {url}")
    
    # Initialize the summarizer
    summarizer = OllamaSummarizer(model="llama3.1", instruction="Generate a concise summary of the following YouTube video transcript")

    # Example usage with a text string
    transcript_txt = get_transcript(url)
    summary = summarizer.summarize_text(transcript_txt)
    print(summary)