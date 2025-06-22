from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
import os

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro-preview-03-25",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    thinking_budget=1024,  # enables thought-process tracing
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain quantum entanglement step by step."),
]

response = model.invoke(messages)
print(response.content)
