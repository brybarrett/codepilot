# tools/api_tester.py

import requests
import json

# Function to send API request based on input
def test_api(url, method, headers, body):
    try:
        # Convert headers and body strings to dictionaries
        headers_dict = json.loads(headers) if headers else {}
        body_dict = json.loads(body) if body else {}

        # Choose GET or POST method
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers_dict)
        else:
            response = requests.post(url, headers=headers_dict, json=body_dict)

        # Return JSON or text depending on response content
        try:
            return response.json()
        except ValueError:
            return {"text": response.text}

    except Exception as e:
        return {"error": str(e)}
