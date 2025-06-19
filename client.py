import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os   

def rules(user_input: str) -> str:
    prompt=f"""You are a specialised expert system focused on Note taking MCP tools integrated with you. Your purpose is to 
    answer queries and questions only related to the MCP tool. You will not answer any question beyond the scope of this 
    context. If a question is asked beyond this scope of the MCP tool you should kindly inform them that you can answer
    questions only regarding the MCP tool.
    User question: {user_input}
    """
    return prompt


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
                await client.close_all_sessions()  
                break

            # Check for clear history command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            
            contextual_prompt = rules(user_input)
            
            # Get response from agent
            print("\nArchivist: ", end="", flush=True)

            try:
                # Run the agent with the user input (memory handling is automatic)
                response = await agent.run(contextual_prompt)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")
    
    finally:
    # Clean up
        if client and client.sessions:
            await client.close_all_sessions()       
            
                
if __name__ == "__main__":
    asyncio.run(run_memory_chat())                