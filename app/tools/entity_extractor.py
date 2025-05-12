import spacy
from langchain.tools import Tool

nlp = spacy.load("en_core_web_sm")

def get_entity_tool():
    return Tool(
        name="EntityExtractor",
        func=lambda text: list(set(ent.text for ent in nlp(text).ents)),
        description="Extracts named entities (people, places, etc.) from a story."
    )
