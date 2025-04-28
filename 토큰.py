import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "e5f6cb4aafc66dc0673f64ed81d9886d",
    "redirect_uri" : "http://localhost:8000/oauth",
    "code"         : 'rKxJrZGo8Hsafvd2yAIhQEY9AdDi67YD8Jsa9AYZSn1ofefvRqjuFAAAAAQKFwEPAAABlZTwwG6SBpCp5rpDbg'
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)
