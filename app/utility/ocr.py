import easyocr
import numpy as np


class OCR:

    def __init__(self, conf:float=0.7, top_n:int=4):
        self.easyocr_reader = easyocr.Reader(lang_list=['en'],
                                             model_storage_directory='./easyocr_model')
        self.conf = conf
        self.top_n = top_n

    @staticmethod
    def bbox_area(coords):
        length = abs(coords[0][0] - coords[1][0])
        width = abs(coords[1][1] - coords[2][1])
        area = length * width
        return area

    def __call__(self, image_array:np.ndarray):
        result = self.easyocr_reader.readtext(image_array)
        res = [{i[1] : dict(conf=i[2], area=self.bbox_area(i[0]))} for i in result]
        res = sorted(res, key=lambda x: list(x.values())[0].get('conf'), reverse=True)
        res = [i for i in res if list(i.values())[0].get('conf')>=self.conf][:self.top_n]
        product_name = ' '.join([list(i.keys())[0] for i in res]).strip().lower()
        return product_name