from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

hf_token = os.getenv('HF_TOKEN')

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=100,
    huggingfacehub_api_token=hf_token
)

chat_model = ChatHuggingFace(llm=llm)

messages = [
    HumanMessage(content="hello")
]

response = chat_model.invoke(messages)

print(response.content)
