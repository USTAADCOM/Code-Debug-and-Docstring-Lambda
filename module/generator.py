"""
noun generator module will take the string and return the nouns list in string.
"""
import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')
def make_prompt(code: str, action: str)-> str:
    """
    make_prompt take code as input and retirn the prompt with the given
    pargraph.

    Parameters
    ----------
    paragraph: str
        string text to find the nouns.
    action: str
        type of action.
    Return
    ------
    prompt: str
        prompt to find the nouns from given paragraph.
    """
    if action=="bug_fix":
        file_path = "./prompt/bug_fixer.txt"
    elif action=="google_doc":
        file_path = "./prompt/google__style_doc.txt"
    else:
        file_path = "./prompt/numpy_style_doc.txt"
    with open(file_path, "r", encoding = "utf8") as file:
        prompt = file.read()
    return prompt

def code_debug(code, action = None,  model = "gpt-3.5-turbo"):
    """
    code_debug method take code and model as input and return the output
    according to the prompt.

    Parameters
    ----------
    prompt: str
        prompt to generate the output.
    model: str
        model name.
    
    Return
    ------
        return response with bugs and code with bug fixes.
    """
    prompt = make_prompt(code, action)
    messages=[
    {
      "role": "system",
      "content": prompt
    },
    {
      "role": "user",
      "content": code
    }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        temperature = 1, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def create_doc(code,action = None,  model = "gpt-3.5-turbo"):
    """
    create_doc method take code and model as input and return the output
    according to the prompt.

    Parameters
    ----------
    prompt: str
        prompt to generate the output.
    model: str
        model name.
    
    Return
    ------
        return reponse with code doc string.
    """
    prompt = make_prompt(code, action)
    messages=[
    {
      "role": "system",
      "content": prompt
    },
    {
      "role": "user",
      "content": code
    }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        temperature = 1,
        max_tokens = 1024,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    return response.choices[0].message["content"]
