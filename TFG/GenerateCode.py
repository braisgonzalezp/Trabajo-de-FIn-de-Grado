from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from Utils import ReadPrompt
from Utils import ReadTest

from config import OPENAI_API_KEY
from config import MISTRAL_API_KEY

def GenerateCode(model,Algorithm):
    if(model == 3):
        modelo="gpt-3.5-turbo"
    elif(model==4):
        modelo="gpt-4"
    elif(model==5):
        modelo="mistral-large-latest"
    template = ReadPrompt("OnlyCode")
    prompt = PromptTemplate(input_variables=["Algorithm"], template=template)
    prompt_value = prompt.format(Algorithm=Algorithm)
    if(modelo=="mistral-large-latest"):
        llm = ChatMistralAI(mistral_api_key=MISTRAL_API_KEY, model_name=modelo, temperature=0)
        code = llm.invoke([HumanMessage(content=prompt_value)])
    else:
        llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=modelo, temperature=0)
        code = llm.invoke([HumanMessage(content=prompt_value)])
    return code.content

def GenerateTests(model,Algorithm,code):
    if (model == 3):
        modelo = "gpt-3.5-turbo"
    elif (model == 4):
        modelo = "gpt-4"
    elif (model == 5):
        modelo = "mistral-large-latest"
    template = ReadPrompt("PromptCodeAndTest")
    prompt = PromptTemplate(input_variables=["Algorithm","code"], template=template)
    prompt_value = prompt.format(Algorithm=Algorithm, code=code)
    if (modelo == "mistral-large-latest"):
        llm = ChatMistralAI(mistral_api_key=MISTRAL_API_KEY, model_name=modelo, temperature=0)
        code = llm.invoke([HumanMessage(content=prompt_value)])
    else:
        llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=modelo, temperature=0)
        code = llm.invoke([HumanMessage(content=prompt_value)])
    return code.content