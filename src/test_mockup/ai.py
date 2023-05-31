import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = "your AP key"

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(input_variables=["product"], template="What is a good name for a company that makes {product}?"
                        ,)
chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run("python beginner training")
while True:
    user_input = input("Enter a product name (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    result = chain.run(user_input)
    print("Generated company name:", result)