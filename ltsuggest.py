# Written by ChatGPT-4

import requests

def suggest_translation(url, q, s, source, target):
    # Build the JSON payload
    payload = {
        "q": q,
        "s": s,
        "source": source,
        "target": target
    }

    # Add trailing slash to URL if not present
    if not url.endswith("/"):
        url += "/"    
    
    # Make the request
    response = requests.post(f"{url}suggest", json=payload)

    return response
