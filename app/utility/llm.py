import requests


class LLM:

    def __init__(self, api_key):
        self.__api_key = api_key

    def build_prompt(self, user_input):
        system_prompt = f"""Summarize only the nutritional contents of the following product in a clear and 
        concise manner in a single table and convert it to json with string values as strings and 
        corresponding product related heading only, suitable for a health-conscious reader."""
        messages = [{"role": "system", "content": system_prompt}]
        messages.append({"role": "user", "content": user_input})
        return messages

    def query_llm(self, user_input):
        url = "https://api.groq.com/openai/v1/chat/completions"
        messages = self.build_prompt(user_input)
        headers = {
            "Authorization": f"Bearer {self.__api_key}",
            "Content-Type": "application/json"
        }       
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": messages,
            "temperature": 0.3,
            # "max_tokens": 800          
        }
        response = requests.post(url, headers=headers, json=payload)
        output = response.json()['choices'][0]['message']['content'].strip()
        return output