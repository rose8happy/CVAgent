import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from langchain.llms import DeepSeek

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

class WebPageParser:
    def __init__(self, url):
        self.url = url

    def get_text(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()

class ResumeAgent:
    def __init__(self, api_key):
        self.llm = DeepSeek(deepseek_api_key=api_key)

    def fill_resume(self, web_content, user_info):
        prompt = f"根据以下网页内容和用户信息，帮我填写一份简历：\n网页内容：{web_content}\n用户信息：{user_info}"
        return self.llm(prompt)

if __name__ == "__main__":
    url = "https://example.com/resume-tips"
    user_info = "姓名：张三，专业：计算机科学，技能：Python、数据分析"

    parser = WebPageParser(url)
    web_content = parser.get_text()

    agent = ResumeAgent(DEEPSEEK_API_KEY)
    resume = agent.fill_resume(web_content, user_info)
    print(resume)