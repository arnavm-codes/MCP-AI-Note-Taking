import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os   

async def run_memory_chat():
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    config_file = "server/note_server.json"

    print("Initializing chat...")

    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(
        model = "qwen-qwq-32b")

    agent = MCPAgent(
        llm = llm,
        client = client,
        memory_enabled=True,
        max_steps=15
    )

    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("==================================\n")
    
    try:
        # Main chat loop
        while True:
            # Get user input
            user_input = input("\nYou: ")

            # Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            # Check for clear history command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            # Get response from agent
            print("\nArchivist: ", end="", flush=True)

            try:
                # Run the agent with the user input (memory handling is automatic)
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")
    
    finally:
    # Clean up
        if client and client.sessions:
            await client.close_all_sessions()       
            
                
if __name__ == "__main__":
    asyncio.run(run_memory_chat())                