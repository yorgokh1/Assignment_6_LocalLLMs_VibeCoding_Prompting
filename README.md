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

## Assignment Structure

```text
gui.py                                  Tkinter interface
main.py                                 Command-line entry point
transcript.py                           Transcript extraction
summarizer.py                           Local Ollama summarization
prompting_parameters_minitasks.ipynb    Minitask Notebook
Reflection.md                           Vibecoding Reflection
```

## Notes

- The video must have an available English transcript.
- All summarization runs locally through Ollama.
- Ollama must be available at `http://localhost:11434`.


## Screenshots

<img width="851" height="146" alt="Screenshot 2026-07-21 074826" src="https://github.com/user-attachments/assets/37838004-47ed-4d19-a63a-92f829eb63b2" />
<img width="1280" height="759" alt="Screenshot 2026-07-21 074926" src="https://github.com/user-attachments/assets/f451fa81-9ee0-48ec-ba1e-95cd9f6413c1" />
<img width="1280" height="758" alt="Screenshot 2026-07-21 075403" src="https://github.com/user-attachments/assets/57293a06-8573-4d53-8de5-55f7395fe19c" />
<img width="1280" height="725" alt="Screenshot 2026-07-21 083345" src="https://github.com/user-attachments/assets/c6b341a6-e6db-4b86-8d82-19ca4f83f5e1" />

