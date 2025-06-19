# AI Enabled MCP Server for Note Taking
## This server allows you to instruct an LLM to perform note taking and retrieval tasks.
### Features included:
- Adding notes
- Deleting all notes at once
- Deleting specific notes, filtered via a keyword
- Searching a note via entering a keyword
- Reading all notes 
- Summarizing all notes at once
- Summarizing specific notes via instructing the LLM to search for a keyword within that note.
- Core topic detection, by instructing the LLM to detect the topic of a specified note via keyword.
- LLM has been restricted to the context of note taking, and won't respond to any other query.


## Concepts
- Uses ChatGroq for summarization and topic detection
- Server is built using FastMCP framework
- Handles STDIO-based communication
- Different clients can access the server such as, Claude Desktop, Cursor AI, etc.
- Also provides interactive chatbot on terminal using ChatGroq.



## About MCP
- MCP is an open protocol that standardizes how applications provide context to LLMs. It's like the USB-C port for AI applications. 
- MCP provides standardiized ways to connect AI models to different tools and sources.
- MCP allows you to build agents and complex workflows on top of LLMs

## General Architecture
- MCP hosts are programs like Claude Desktop, AI integrated IDEs etc.
- MCP clients are protocol clients that maintain one-to-one connections with servers.
- MCP servers are lightweight programs that each expose specific capabilities and tools via MCP protocol.

## Core concepts
### MCP servers provide 3 types of capabilities:
- Tools : Funtions that can be called by the LLM, with user approval.
- Resources : File-like data that can be read by clients (like APIs).
- prompts : Pre-written templates that help the user accomplish specific tasks.
