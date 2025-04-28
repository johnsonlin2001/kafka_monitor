# To specify websites to monitor, add them as dictionaries to SITES_LIST.
# Specify the required "url" key and an optional "regex" key for checking the response body.
# Example entries are provided using placeholder domains. Please replace them with the actual websites to monitor.
SITES_LIST = [
    {"url": "https://example.com", "regex": "regex_expression"},
    {"url": "https://examplenoregex.com"},
]

# Used to set the time interval (in seconds) between each round of website status checks.
REQUEST_INTERVAL=30