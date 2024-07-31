import re

def validate_request(valid_auth_tokens, request):
    method, url = request
    params = re.search(r'\?(.*)', url)
    
    if params:
        params = params.group(1).split('&')
        auth_token = None
        csrf_token = None
        
        for param in params:
            key, value = param.split('=')
            if key == 'token':
                auth_token = value
            elif key == 'csrf':
                csrf_token = value
        
        if auth_token and auth_token in valid_auth_tokens:
            if method == 'GET' or (method == 'POST' and csrf_token and re.match("^[a-z0-9]{8,}$", csrf_token)):
                return f'VALID, {",".join(params)}'
    
    return 'INVALID'

def get_responses(valid_auth_tokens, requests):
    # return [validate_request(valid_auth_tokens, request) for request in requests]
    l = []
    for request in requests:
        l.append(validate_request(valid_auth_tokens, request))
    return l



# Example usage
valid_auth_tokens = ["ah37j2ha483u", "safh34ywb0p5", "ba34wyi8t902"]
requests = [
    ["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"],
    ["GET", "https://example.com/?token=safh34ywbQp5&name=sam"],
    ["POST", "https://example.com/?token=safh34ywb0p5&name=alex"],
    ["POST", "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]
]

responses = get_responses(valid_auth_tokens, requests)
print(responses)

