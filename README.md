# LangChain 项目环境配置

## 步骤

1. 推荐使用 [uv](https://github.com/astral-sh/uv) 创建和管理虚拟环境（更快、更现代）：

   ```bash
   pip install uv
   uv venv venv
   ```

2. 激活虚拟环境：
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. 安装依赖（uv 安装速度更快）：
   ```bash
   uv pip install -r requirements.txt
   ```

4. 复制 `.env.example` 为 `.env`，并填写你的 API Key：
   ```bash
   cp .env.example .env
   ```

5. 开始你的 LangChain 项目开发！

## 参考

- [LangChain 官方文档](https://python.langchain.com/)
- [uv 项目主页](https://github.com/astral-sh/uv)
