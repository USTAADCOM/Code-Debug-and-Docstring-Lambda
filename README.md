# Code Debug and Docstring Lambda
Here we develop AWS lambda for the following task.
* Code Debug
* Code DocString
  * Numpy Style
  * Google Style
## Setup
  ```code
  git clone https://github.com/USTAADCOM/Code-Debug-and-Docstring-Lambda.git
  cd Code-Debug-and-Docstring-Lambda
  pip install requirements.txt -q
  ```
## .env setup
create .env and put your key
```code
OPENAI_API_KEY = "your sceret key here"
```
## Payload and Response 
Payload
```code
    {
      "type" : "Your type here code_debug, google_doc, numpy_doc",
      "code" : "Your code here",
    }
```
Note: code structure Should be
```code
"def get_noun(paragraph, model = \"gpt-3.5-turbo\"):\n    prompt = make_prompt(paragraph)\n    messages = [{\"role\": \"user\", \"content\": prompt}]\n    response = openai.ChatCompletion.create(\n        model=\"gpt-3.5-turbo\",\n        messages = messages,\n        temperature = 1, # this is the degree of randomness of the model's output\n    )\n    return response.choices[0].message[\"content\"]"
``` 
Response 
```code
    {
      'statusCode': 200, 
      'body': "Code with requested type"
    }
```
## Local Test Run
```code
python driver.py
```
Note: Change payload according to the need.