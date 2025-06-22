from dotenv import load_dotenv
import os

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY"), stream=True
)

msg = HumanMessage(
    content="tell me the information and code about udp in python both client and server side"
)
for chunk in llm.stream([msg]):
    print(chunk.content, end="", flush=True)
