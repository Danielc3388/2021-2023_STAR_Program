import re
from collections import Counter
import tkinter as tk
from tkinter import ttk
from textblob import TextBlob
from textblob.sentiments import PatternAnalyzer


def tokenize(text):
    words = re.findall(r'\b\w+\b',text.lower())
    return words

def get_capitalized_phrases(text):
    phrases = re.findall(r'\b[A-Z][a-z]+\b(?:\s+_[A-Z][a-z]+\b)*', text)
    return phrases

def text_analysis(text):
    analysis = ""
    blob = TextBlob(text,analyzer = PatternAnalyzer())
    sentiment = blob.sentiment
    analysis += f"Sentiment:\n Polarity:{sentiment.polarity}\n Subjectivity:{sentiment.subjectivity}\n\n"

    words = tokenize(text)
    word_counts = Counter(word.lower() for word in words)
    analysis += "Word frequencies: \n"
    for word, count in word_counts.most_common(10):
        analysis += f"{word}:{count}\n"

    capitalized_phrases = get_capitalized_phrases(text)
    analysis += "\nCapitalized Phrases: \n"
    for phrases in capitalized_phrases:
        analysis += f"{phrases} \n"

    return analysis

def on_click():
    input_text = input_box.get("1.0", tk.END)
    result = text_analysis(input_text)
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)

app = tk.Tk()
app.title("Text Analytics")

frame = ttk.Frame(app,padding='10')
frame.grid(row=0, column=0, sticky=(tk.W,tk.E, tk.N,tk.S))

input_label = ttk.Label(frame, text = "Please input the text:")
input_label.grid(row=0, column=0, sticky=(tk.W), pady=(0,10))

input_box = tk.Text(frame, wrap=tk.WORD, width=50, height=10)
input_box.grid(row=1, column=0, sticky=(tk.W,tk.E,tk.N,tk.S))

result_label = ttk.Label(frame, text = "Analysis Result:")
result_label.grid(row=2, column=0, sticky=(tk.W), pady=(10,10))

result_box = tk.Text(frame, wrap=tk.WORD, width=50, height=10)
result_box.grid(row=3, column=0, sticky=(tk.W,tk.E,tk.N,tk.S))

button = ttk.Button(frame, text="Analysis", command=on_click)
button.grid(row=4,column=0, pady=(10,10))

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(3, weight=1)


app.mainloop()
