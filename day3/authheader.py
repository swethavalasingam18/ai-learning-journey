# Calling OpenAI's API (what your n8n AI agent nodes do internally)
headers = {
    "Authorization": "Bearer sk-...",
    "Content-Type": "application/json"
}
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

#2. Telling the server what format you're sending/expecting
headers = {
    "Content-Type": "application/json",   # "I'm sending you JSON"
    "Accept": "application/json"          # "Please send JSON back"
}

#3. Avoiding being blocked when scraping or calling public sites
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# 4. Rate limiting / usage tracking
headers = {
    "X-Client-Id": "my-app-v1"
}


#5. Passing session/cookie-like tokens between requests

headers = {
    "Authorization": f"Bearer {session_token}"
}



#The 3 common patterns

#1. API Key in header (most common for AI APIs)

headers = {
    "Authorization": "Bearer sk-your-api-key-here"
}
response = requests.get("https://api.example.com/data", headers=headers)

#2. API Key as a custom header (no "Bearer")

headers = {
    "X-API-Key": "your-api-key-here"
}

#3.API key as a query parameter (older style, less secure)

response = requests.get("https://api.example.com/data", params={"api_key": "your-key"})