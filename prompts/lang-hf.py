from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Step 1: Create the LLM endpoint object
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # A known chat-compatible model
    task="chat-completion",
)

# Step 2: Use that in ChatHuggingFace
model = ChatHuggingFace(llm=llm)

# Step 3: Invoke your prompt
result = model.invoke("What is the capital of India?")
print(result.content)

if __name__ == "__main__":
    # This is just to ensure the script runs when executed directly
    print("Script executed successfully.")
    if result.content:
        print(f"Response: {result.content}")
        if "New Delhi" in result.content:
            print("The response is correct.")
    else:
        print("No response received.")
    if not result.content:
        print("The model did not return any content.")
    else:
        print("Model returned content successfully.")    