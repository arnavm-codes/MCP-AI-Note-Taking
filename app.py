# # front end; basic streamlit app for implementing shttp

# import streamlit as st
# from mcp_use import MCPAgent, MCPClient
# from langchain_groq import ChatGroq
# import os
# import asyncio
# from dotenv import load_dotenv

# load_dotenv()

# client = MCPClient.from_config_file("server/note_server.json")
# llm = ChatGroq(
#     model = "qwen-qwq-32b"
#     )
# agent = MCPAgent(
#     llm =llm,
#     client = client,
#     memory_enabled = True,
#     max_steps = 15
# )


# st.set_page_config(page_title="Note Taking Assistent", page_icon = "📝")
# st.title("AI enabled Note Taking chatbot")

# # store chat history in session
# if "history" not in st.session_state:
#     st.session_state.history = []

# user_input= st.text_input("What's on your mind?...")

# if user_input:
#     st.session_state.history.append(("You: ", user_input))
    
#     async def get_response():
#         return await agent.run(user_input)

#     response  = asyncio.run(get_response())
#     st.session_state.history.append(("Archivist: ", response))

# for speaker, message in st.session_state.history:
#     with st.chat_message(speaker):
#         st.markdown(message)