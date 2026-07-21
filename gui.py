import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading

from transcript import get_transcript
from summarizer import OllamaSummarizer


def get_summary(url):
    summarizer = OllamaSummarizer(
        model="llama3.1",
        instruction="Generate a concise summary of the following YouTube video transcript"
    )

    transcript = get_transcript(url)
    return summarizer.summarize_text(transcript)


class SummaryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Transcript Summary")
        self.geometry("600x450")
        self.configure(bg="#1e293b")

        main_frame = tk.Frame(self, bg="#1e293b")
        main_frame.pack(fill="both", expand=True, padx=24, pady=(60, 24))

        input_label = tk.Label(
            main_frame,
            text="YouTube URL:",
            font=("Segoe UI", 11),
            fg="white",
            bg="#1e293b",
        )
        input_label.pack(anchor="w")

        self.url_entry = tk.Entry(
            main_frame,
            fg="#e2e8f0",
            bg="#334155",
            insertbackground="white",
            relief="flat",
            font=("Segoe UI", 9),
        )
        self.url_entry.insert("end", "https://youtube.com/watch?v=...")
        self.url_entry.pack(fill="x", pady=(6, 2), ipady=6)

        self.url_entry.bind("<Return>", lambda event: self.fetch_summary())

        self.go_btn = tk.Button(
            main_frame,
            text="Get Summary\n↓",
            command=self.fetch_summary,
            fg="#fff7ed",
            bg="#ea3e3d",
            activeforeground="white",
            activebackground="#dc2626",
            font=("Segoe UI", 9),
            relief="flat",
            padx=16,
            pady=4,
        )
        self.go_btn.pack(pady=(6, 10))

        summary_label = tk.Label(
            main_frame,
            text="Summary:",
            font=("Segoe UI", 11),
            fg="white",
            bg="#1e293b",
        )
        summary_label.pack(anchor="w")

        self.summary_box = scrolledtext.ScrolledText(
            main_frame,
            wrap="word",
            font=("Consolas", 9),
            fg="#e2e8f0",
            bg="#334155",
            insertbackground="white",
            relief="flat",
            padx=12,
            pady=10,
        )
        self.summary_box.pack(fill="both", expand=True, pady=(6, 0))

        self.summary_box.insert("1.0", "Your summary will appear here.")

    def fetch_summary(self):
        url = self.url_entry.get().strip()

        if not url or url == "https://youtube.com/watch?v=...":
            messagebox.showwarning(
                "Missing URL",
                "Please enter a YouTube URL."
            )
            return

        self.go_btn.config(state="disabled", text="Loading...")
        self.summary_box.delete("1.0", "end")
        self.summary_box.insert("1.0", "Generating summary...")

        thread = threading.Thread(
            target=self.generate_summary,
            args=(url,),
            daemon=True,
        )
        thread.start()

    def generate_summary(self, url):
        try:
            summary = get_summary(url)
            self.after(0, self.show_summary, summary)

        except Exception as error:
            self.after(0, self.show_error, str(error))

    def show_summary(self, summary):
        self.summary_box.delete("1.0", "end")
        self.summary_box.insert("1.0", summary)
        self.go_btn.config(state="normal", text="Get Summary\n↓")

    def show_error(self, error):
        self.summary_box.delete("1.0", "end")
        self.summary_box.insert("1.0", f"Error: {error}")
        self.go_btn.config(state="normal", text="Get Summary\n↓")


if __name__ == "__main__":
    app = SummaryApp()
    app.mainloop()