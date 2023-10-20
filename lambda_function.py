"""
lambda method module 
"""
import json
from module import generator
def make_success_response(output_data: dict)-> dict:
    """
    method take Tool data and return a response.

    Parameters

    ----------
    output_data: dict
        data dictionary return as output by requested Tool.

    Return
    ------
    dict
        return response as dictionary.
    
    """
    response = {
        "statusCode": 200,
        'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*'
                },
        "body": json.dumps(output_data)
        }
    return response

def make_validation_response()-> dict:
    """
    method amke the Bad params response.

    Parameters

    ----------
    None

    Return
    ------
    dict
        return response as dictionary.
    
    """
    output_dict = {}
    output_dict["Error"] = "Bad Params"
    output_dict["Message"] = "Code must be given"
    return {'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*'
                },
            'body' : json.dumps(output_dict)
        }
def validate_request(event):
    """
    doc
    """
    if "code" not in event:
        return False
    elif event["code"] == "":
        return False
    return True
def lambda_handler(event_jsonified, context):
    """
    lambda handler method recive the json data and return the response as json file.

    Parameters
    ----------

    event_jsonified: json
        json request data.
    context: Null
        null.
    Return
    ------
        return json resposne as a result according to the request.
    """
    output = {}
    try:
        if "body" not in event_jsonified:
            output["Error"] = "Bad Params"
            output["Message"] = "Body Param not found"
            return {
                "statusCode": 400,
                'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                "body" : json.dumps(output)
                }
        else:
            event = event_jsonified["body"]
            event = json.loads(event, strict = False)
            if "type" not in event:
                output["Error"] = "Bad Params"
                output["Message"] = "type key missing"
                return {
                    'statusCode': 400,
                    'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                    "body" : json.dumps(output)
                    }
            elif event["type"] == "":
                output["Error"] = "Bad Params"
                output["Message"] = "Must be provided type bug_fix, doc_google, doc_numpy"
                return {
                    'statusCode': 400,
                    'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                    "body" : json.dumps(output)
                    }
            else:
                code = event["code"]
                type = event["type"]
                if type == "bug_fix":
                    validation = validate_request(event)
                    if validation:
                        response = generator.code_debug(code, type)
                        return response
                    return make_validation_response()
                elif type == "google_doc":
                    validation = validate_request(event)
                    if validation:
                        response = generator.create_doc(code, type)
                        return response
                    return make_validation_response()
                elif type == "numpy_doc":
                    validation = validate_request(event)
                    if validation:
                        response = generator.create_doc(code, type)
                        return response
                    return make_validation_response()
                else:
                    return {
                        'statusCode': '404',
                        'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                        'body': 'Requested Tool Not Found'
                    }
    except Exception as error:
        response = {
            'statusCode': 500,
            'Error' : error, 
            'headers': {
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                    },
            'Message' : "Internal Server Error"
            }
        return response
