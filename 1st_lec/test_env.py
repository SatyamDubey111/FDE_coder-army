from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if api_key:
    print("API KEY LOADED SUCCESSFULLY")
else:
    print("API KEY NOT FOUND")