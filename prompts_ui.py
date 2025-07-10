from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
import re 
from langchain_core.prompts import PromptTemplate,load_prompt


llm=HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=200
    )
)
model=ChatHuggingFace(llm=llm)

import streamlit as st

st.header('Research tool')
paper_input = st.selectbox(
    "Select Research paper name",
    [
        "select...",
        "ImageNet Classification with Deep Convolutional Neural Networks",
        "Deep Residual Learning for Image Recognition",
        "Attention is All You Need",
        "Generative Adversarial Nets",
        "Long Short-Term Memory",
        "YOLOv3: An Incremental Improvement"
    ]
)


style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)
# #template 
# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}  
# Explanation Length: {length_input}  
# 1. Mathematical Details:  
#    - Include relevant mathematical equations if present in the paper.  
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
# 2. Analogies:  
#    - Use relatable analogies to simplify complex ideas.  
# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=['paper_input', 'style_input','length_input'],
# validate_template=True
# )

#method-2
template=load_prompt('template.json')


#fill the place holders
prompt=template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})

if st.button('summarize'):
    result=model.invoke(prompt)
    # output = result.content
    # clean_output = re.sub(r'<\|.*?\|>|\</s\>', '', output).strip()
    st.write(result.content)
   