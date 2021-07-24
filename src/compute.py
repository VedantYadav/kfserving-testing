# import logging

import kfserving
from transformers import pipeline

# from preprocess import lower_case


# logging.basicConfig(level=logging.DEBUG)

# def model_predict(data):
#     if data:
#         data = lower_case(data)
#         return model(data)
#     else:
#         return {'data foramt incorrect'}

class KF_test(kfserving.KFModel):
    def __inti__(self, name):
        super().__init__(name)
        self.name = name
        self.ready = False
        
    def load(self):
        self.model = pipeline('sentiment-analysis')
        self.ready = True
        
    def predict(self, request):
        inputs = request["instances"]
        source_text = inputs[0]["text"]
        
#         logging.debug("source text -> " + soruce_text)

        print("source text -> " + soruce_text)
        if isinstance(source_text, str):
            return {"predictions": self.model(soruce_text)}
        else:
            return {"predictions": "Wrong data format"}
        

if __name__=="__main__":
    model = KF_test("kfserving_custom")
    model.load()
    kfserving.KFServer(workers=1).start([model])