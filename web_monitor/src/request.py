import requests
import re
import time

def send_request(url, regex=None):
    """
    Sends an HTTP get request to the specified url and records status code, response time, and the result of an optional regex check. 

    Args:
        url: A string specifying the url to send the request. 
        regex (optional): A regex pattern to search for in the response body. 

    Returns:
        A dictionary object containing response information.
        Keys include:
            - "website": The url that was requested. 
            - "response_time": The response time of the request if successful. 
            - "status_code": The HTTP status code if the request succeeded. 
            - "regex_match": A boolean corresponding to whether there was a regex match (False if none provided).
            - "timeout": True if the request timed out.
            - "error": Error message if the request failed for other reasons. 
    """
    try:

        response = requests.get(url, timeout=10)
        response_time = response.elapsed.total_seconds()
        response_body = response.text
        status_code = response.status_code
        regex_match = False

        # Perform a regex check on the response body if regex was provided
        if(regex):
            if(re.search(regex, response_body)):
                regex_match = True
        
        return {"website": url, "response_time": response_time, "status_code": status_code, "regex_match": regex_match}

        
    except requests.Timeout:
        return {"website": url, "timeout": True}
    except requests.RequestException as error:
        return {"website": url, "error": str(error)}
    
