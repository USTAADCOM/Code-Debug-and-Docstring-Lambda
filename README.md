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
Response 
```code
    {
      'statusCode': 200, 
      'body': "Code with requested type"
    }
```
