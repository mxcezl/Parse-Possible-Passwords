import requests

def getRawResponse(url: str) -> str:
    return requests.get(url).content