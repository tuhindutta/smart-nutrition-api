import string
from ast import literal_eval
import re
from utility.google_api import ProductNutritionSearch
from utility.llm import LLM


class NutritionData():

    def __init__(self, google_api_key, groq_api_key):
        self.product = ProductNutritionSearch(google_api_key)
        self.llm = LLM(groq_api_key)

    def __call__(self, product):
        product_nutrition_data = self.product(product)
        translator = str.maketrans('', '', string.punctuation)
        res = self.llm.query_llm(product_nutrition_data)
        
        splitted = re.sub(r'\bnull\b', 'None', res).split('\n')
        heading = splitted[0].strip().translate(translator)
        heading = None if heading.startswith('json') else heading
        data = ''.join(splitted[splitted.index('```json')+1:splitted.index('```')])
        data = literal_eval(data)
        return res, heading, data