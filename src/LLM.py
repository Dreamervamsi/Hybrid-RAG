from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Grab your secret token securely
hf_token = os.getenv('HF_TOKEN')

# 2. Define the core serverless endpoint 
# (This handles the cloud connection directly)
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=100,
    huggingfacehub_api_token=hf_token
)

# 3. Wrap it in a Chat interface to satisfy the HF server structure
chat_model = ChatHuggingFace(llm=llm)

# 4. Format and call your prompt
messages = [
    HumanMessage(content="hello")
]

response = chat_model.invoke(messages)

# 5. Print the cloud-generated answer
print(response.content)
