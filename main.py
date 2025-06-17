from tkinter import NO
from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("AI Notes") # server name - AI Notes

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
        #return matches if matches else "No match found."

        if matches:
            return matches
        else:
            return "No matches found"   
              