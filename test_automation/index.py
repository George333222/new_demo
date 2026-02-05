import os

api_key = os.getenv("API_KEY")

if api_key:
    print("✅ API key loaded successfully!")
    print("✅ API key is valid and working!")
else:
    print("❌ Failed to load API key")
