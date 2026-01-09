# LLM-based-Data-Reader-
Simple python script that reads natural language input to return specific details out of the same.
Usage Instructions:
1. Create a env file with the api key, model and the base url, where base url corresponds to your LLM provider.
2. Run the script.

**Note:** This program requires you to fill in the details of the model you want to access in the .env file. It will not work without it.
Currently, a sample .env file has been provided, designed to allow one click access to OpenAI API compliant Local LLM servers like Jan and LMStudio. Would need these to be setup or configured before use. 
**.env**
Save the below format, after changes as .env in the same folder as this file.

Format:

MODEL="meta-llama-3.1-8b-instruct"

BASE_URL="http://127.0.0.1:1234/v1"

OPENAI_API_KEY="random"

Ensure newlines after each of the keys.
