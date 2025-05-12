from transformers import pipeline
from langchain.tools import Tool

summarizer_pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def get_summary_tool():
    return Tool(
        name="SummaryGenerator",
        func=lambda text: summarizer_pipe(text[:1000], max_length=1000, min_length=30, do_sample=False)[0]["summary_text"],
        description="Summarizes a given story."
    )
