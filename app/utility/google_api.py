from google import genai
import os


class GoogleSearch:

    def __init__(self, api_key):
        os.environ['GOOGLE_API_KEY'] = api_key
        self.model_id = "gemini-2.5-flash-lite-preview-06-17"
        self.client = genai.Client()

    def search(self, query):
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=query,
            config={"tools": [{"google_search": {}}]},
        )
        return response.text



class ProductNutritionSearch(GoogleSearch):

    def __init__(self, api_key):
        super().__init__(api_key)

    def __call__(self, product):
        query = f"{product} brand product nutrition contents"
        response = self.search(query)
        return response