# Reflection

I used Qwen 3.5 9B through OpenCode to help build the YouTube transcript summarizer.  
It saved me time by producing clean, well-formatted Python code and handling unfamiliar libraries such as Tkinter.  
This was especially useful for the GUI, since much of its code was repetitive and mechanical, and it reduced the need for long documentation searches.  
However, the model was difficult to run locally because it nearly filled my 8 GB of VRAM, leaving little space for the context window.  
At a 4K context size it often stopped halfway through its reasoning, while 16K worked more reliably but heavily used the CPU and made generation slow.  
Because of this, writing follow-up prompts and repeatedly correcting mistakes was inconvenient.  
The biggest error was that it kept suggesting Whisper even though I explicitly asked it to use youtube-transcript-api, and it also generated incorrect API calls for that library.  
I found that the model could not reliably generate the entire app in one prompt, so the best strategy was to work function by function and clearly state each function's input, output, and responsibility.  

For example, instead of asking the model to create the whole app, I separately asked it to:

1. Extract the video ID from a YouTube URL
2. Fetch the transcript and return it as a string
3. Create a summarizer class that connects to Ollama
4. Build a GUI that accepts the URL and displays the result

Example prompts included: “Create a function that takes a YouTube URL and returns its transcript using youtube-transcript-api; do not use Whisper,” and “Create a simple Tkinter GUI that takes the URL and displays the result using helper functions from the other files.”  
Overall, Qwen was most useful for boilerplate and structure, while I still had to verify the APIs, test the code, and integrate the final application myself.

## Prompts Used

### Prompt 1: Initial Application Logic

> Pretend you're a senior Python developer. Your goal is to help me develop a small Python app to summarize YouTube videos using their transcripts. First write the app's main logic (i.e the ollama request and the summarizer). The summary will be made using a local Llama 3.1 model and using the OpenAI Python library. Assume you already have the transcript.

### Prompt 2: Transcript Extraction

> Write a helper function that takes a YouTube URL, extracts its video ID, fetches the English transcript using the `youtube-transcript-api` library, and returns the full transcript as a single string. Do not use Whisper or download the video audio.

### Prompt 3: GUI Generation

> I am making the GUI that just takes the URL and prints the output using the helper functions from the other files. Keep a consistent style and format. Keep it neat and simple.

### Prompt 4: Function-by-Function Guidance

> Create this function only. It should take a YouTube URL as input and return the transcript as a string. Use the existing YouTube transcript instead of transcribing audio. Keep the function simple and do not add unrelated functionality.

## Final Evaluation

Overall, Qwen 3.5 9B was useful for accelerating implementation, especially for repetitive or unfamiliar parts of the project. It was strongest when generating structured boilerplate and giving me a starting point that I could edit.

However, it was less reliable when dealing with unfamiliar third-party APIs and when asked to generate too much at once. The local hardware limitations also made long conversations and repeated correction difficult.