import os
import requests

# Read your API key from environment variables
api_key = os.getenv("API_KEY")

if not api_key:
    print("❌ API key not found!")
else:
    print("✅ API key loaded successfully!")

    # Send a test request directly to OpenAI’s endpoint
    url = "https://api.openai.com/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("✅ API key is valid and working!")
    elif response.status_code == 401:
        print("🚫 Invalid API key or not authorized.")
    else:
        print(f"⚠️ Something else went wrong: {response.status_code}")
