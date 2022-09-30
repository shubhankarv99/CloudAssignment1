import json
def lambda_handler(event, context):
    response = {
        "messages":
            [
                {"type": "unstructured",
                "unstructured":
                    {
                        "text": 'Application under development. Search functionality will be implemented in Assignment 2'
                    }
                }
            ]
    }
    return response