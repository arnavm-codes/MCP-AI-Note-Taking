from mcp.server.fastmcp import FastMCP
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

mcp = FastMCP("AI Notes") # server name - AI Notes

load_dotenv()
# print("Load API KEY:", os.getenv("GROQ_API_KEY"))

client = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="qwen-qwq-32b"
) # LLM client

NOTES_FILE = "notes.txt"

def ensure_file():
    """Makes sure NOTES_FILE exists"""
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as file:
            file.write("")


@mcp.tool()
def add_note(message: str) -> str:
    """Append a new note to the notes file.
    
    Args:
        message(str): The note to be appended.

    Returns:
        str: Confirmation message that the note is added successfully.    
    """
    ensure_file()
    with open(NOTES_FILE, "a") as file:
        file.write(message+"\n")
    return "Note added."    


@mcp.tool()
def read_note()->str:
    """Reads notes from the notes file.

    Returns:
        str: All notes as a single string seperated by line breaks. If no notes,
             then returns a default message.
    """
    ensure_file()
    with open(NOTES_FILE , "r") as file:
        content = file.read().strip()
    return content or "No notes to read."   


@mcp.tool()
def delete_all_notes()->str:
    """ Clears all notes in the notes file.

    Returns:
        str: Confirmation message that all notes are cleared.
    """
    ensure_file()
    open(NOTES_FILE, "w").close()
    return "All notes cleared."


@mcp.tool()
def delete_note(keyword: str) -> str:
    """Deletes notes with specified keyword
    
    """
    ensure_file()
    with open(NOTES_FILE, "r") as file:
        lines = file.readlines()

    new_lines = [line for line in lines if keyword.lower() not in line.lower()]
    delete_count = len(lines) - len(new_lines)
    if delete_count == 0:
            return "No matches found"

    with open(NOTES_FILE, "w") as file:
        file.writelines(new_lines)
    return f"{delete_count} note(s) deleted."    


@mcp.tool()
def search_note(keyword: str)-> str:
    """Searches a note using provided keyword
    
    Args:
        keyword(str): The keyword to match in the notes file.

    Returns:
        str: Confirmation message that a match to keyword is found. If not matched, 
             then returns a default message     
    """
    ensure_file()
    with open(NOTES_FILE, "r") as file:
        matches = [line for line in file if keyword.lower() in line.lower()]

        if matches:
            return "\n".join(matches)
        else:
            return "No matches found"   


@mcp.tool()
def summarize_all_notes()-> str:
    """Summarizes all notes using GROQ LLM
    
    Returns:
        str: Summarization of all the notes in paragraph form. If no notes exist, returns a 
             default message.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as file:
        content = file.read().strip()

    if not content:
        return "No notes found."

    prompt = f"Summarize the following notes in paragraph form. \n{content}"

    try:
        response = client.invoke(prompt)        
        return response.content.strip()
    except Exception as e:
        return f"An error occured during summarisation: {str(e)}"


@mcp.tool()
def summarize_notes(keyword:str) -> str:
    """Uses provided keyword to search for notes with that keyword and summarizes it.
    
    Args:
        keyword(str) : The keyword to match in the notes file.

    Returns:
        str: Summarization of all the notes cotaining the specified keyword, in paragraph form. 
             If no such notes exist, then returns a default message. 
    """     
    ensure_file()
    with open(NOTES_FILE, "r") as file:
        matches = [line for line in file if keyword.lower() in line.lower()]

        if not matches:
            return "No matches found."

        content = matches
        prompt = f"Summarize all the notes which contain the keyword: {keyword} in a paragraph.\n{content}"

        try:
            response = client.invoke(prompt)
            return response.content.strip()
        except Exception as e:
            return f"An error occured during summarisation: {str(e)}"


              