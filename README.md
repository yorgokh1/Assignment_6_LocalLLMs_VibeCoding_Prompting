# YouTube Video Summarizer

A small Python app that extracts the transcript from a YouTube video and summarizes it using a local **Llama 3.1** model through Ollama.

The project includes both a Tkinter GUI and a command-line interface.

## Built With

- Python
- Tkinter
- Ollama
- Llama 3.1
- OpenAI Python library
- YouTube Transcript API

The app was developed with **Qwen 3.5 9B** using **OpenCode**.

## Requirements

- Python 3.10+
- Ollama installed and running
- The `llama3.1` model downloaded locally

Install the Python dependencies:

```bash
pip install openai youtube-transcript-api
```

Download the local model:

```bash
ollama pull llama3.1
```

## Usage

Start Ollama, then run the GUI:

```bash
python gui.py
```

Paste a YouTube URL and click **Get Summary**.

To use the command-line version:

```bash
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Project Structure

```text
gui.py          Tkinter interface
main.py         Command-line entry point
transcript.py   Transcript extraction
summarizer.py   Local Ollama summarization
```

## Notes

- The video must have an available English transcript.
- All summarization runs locally through Ollama.
- Ollama must be available at `http://localhost:11434`.
