import requests

ROOT_MODEL_URL = "https://raw.githubusercontent.com/metriccoders/ml-models/main/"


model_name = "https://raw.githubusercontent.com/metriccoders/ml-models/main/rf_classifier_iris.joblib"


def load_model(url = model_name):
    r = requests.get(url)

    if r.status_code == 200:
        return r.content
    else:
        print("Unable to load the model: ", r.status_code)


load_model(model_name)