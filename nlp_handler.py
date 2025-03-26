from langchain.llms import HuggingFaceHub
from config import HF_API_TOKEN

llm = HuggingFaceHub(
    huggingfacehub_api_token=HF_API_TOKEN,
    repo_id="google/flan-t5-large",  # You can choose other models if you prefer
    model_kwargs={"temperature": 0.5, "max_length": 100}
)

def get_response(prompt):
    response = llm(prompt)
    return response.strip()
