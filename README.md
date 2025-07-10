# research-paper-summarizer

# 🧠 Research Paper Summarizer using TinyLlama + Streamlit

A simple web app that generates concise and styled summaries of well-known research papers using Hugging Face's `TinyLlama` model. Built with `Streamlit` and `LangChain`, it provides customizable explanations based on user preferences.

## 🚀 Features

- 🔍 Select from iconic research papers in AI/ML
- 🧑‍🏫 Multiple explanation styles: Beginner-Friendly, Technical, Code-Oriented, Mathematical
- 📏 Adjustable summary lengths: Short, Medium, Long
- 🤖 Uses Hugging Face's `TinyLlama-1.1B-Chat-v1.0` for text generation
- 🧠 LangChain prompt templating for dynamic prompt creation

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Hugging Face Transformers](https://huggingface.co/)
- [TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)

## 📦 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/research-paper-summarizer.git
   cd research-paper-summarizer
2.  **Install dependencies:**
      pip install -r requirements.txt
3. **Run the app:**
       streamlit run prompts_ui.py
