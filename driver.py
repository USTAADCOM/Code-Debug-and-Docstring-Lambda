"""
module contain the testing method for the created lambda endpoints.
"""
import json
import sys
from lambda_function import lambda_handler
def tool_testing(json_data, content)-> None:
    """
    input json file and test the string pladirme or not the required results.

    Parameters
    ----------
    json_data: json
        json data containing the request content.

    Return
    ------
    None
    """
    result = lambda_handler(json_data, content)
    print(result)

CONTENT = None
json_data = {}
data = {
    "type" : "google_doc",
    "code" : "def get_noun(paragraph, model = \"gpt-3.5-turbo\"):\n    prompt = make_prompt(paragraph)\n    messages = [{\"role\": \"user\", \"content\": prompt}]\n    response = openai.ChatCompletion.create(\n        model=\"gpt-3.5-turbo\",\n        messages = messages,\n        temperature = 1, # this is the degree of randomness of the model's output\n    )\n    return response.choices[0].message[\"content\"]"
}
json_data["body"] = json.dumps(data)
tool_testing(json_data, CONTENT)
