import os
from dotenv import load_dotenv
from langchain_community.llms import DeepSeek

def test_deepseek_api():
    load_dotenv()
    api_key = os.getenv("DEEPSEEK_API_KEY")
    llm = DeepSeek(deepseek_api_key=api_key)
    prompt = "你好，请简单介绍一下你自己。"
    response = llm(prompt)
    assert isinstance(response, str) and len(response) > 0
    print("DeepSeek API 测试通过，返回内容：", response)

if __name__ == "__main__":
    test_deepseek_api()