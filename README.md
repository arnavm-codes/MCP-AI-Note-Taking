# AI Enabled MCP Server for Note Taking
## This server allows you to instruct an LLM to perform note taking and retrieval tasks.
### Features included:
### - Adding notes
### - Deleting all notes at once
### - Deleting specific notes, filtered via a keyword
### - Searching a note via entering a keyword
### - Reading all notes 
### - Summarizing all notes at once
### - Summarizing specific notes via instructing the LLM search for a keyword within that note.
### - Core topic detection, by instructing the LLM to detect the topic of a specified note via keyword.


## Concepts
### - Uses ChatGroq for summarization and topic detection
### - Server is built using FastMCP framework
### - Handles STDIO-based communication
### - Different clients can access the server such as, Claude Desktop, Cursor AI, etc.