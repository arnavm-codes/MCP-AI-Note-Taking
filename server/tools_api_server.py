from fastapi import FastAPI, Body
from note_server import(add_note, read_note, delete_all_notes, delete_note, search_note, 
                        summarize_all_notes, summarize_notes, detect_topics)

app = FastAPI()

@app.get("/add_note")
def add_note_api(note: str = Body(...)):
    return {"result": add_note(note)}

@app.get("/read_note")
def read_note_api():
    return {"result": read_note()}

@app.get("/delete all notes")
def delete_all_notes():
    return {"result": delete_all_notes()}

@app.get("/delete_note")
def delete_note_api(keyword: str = Body(...)):
    return {"result": delete_note(keyword)}

@app.get("/search_notes")
def search_notes_api(keyword: str):
    return {"result": search_note(keyword)}

@app.get("/summarize_notes")
def summarize_notes_api(keyword: str):
    return {"result": summarize_notes(keyword)}

@app.get("/summarize_all_notes")
def api_summarize_all_notes():
    return {"result": summarize_all_notes()}

@app.get("/detect_topics")
def api_detect_topics(text: str):
    return {"result": detect_topics(text)}