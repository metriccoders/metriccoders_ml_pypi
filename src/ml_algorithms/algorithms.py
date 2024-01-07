import requests
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris
import joblib
from io import BytesIO


class MLPowerEngine:
    """
    A class handling models
    
    Attributes:
        model_path (str): Raw github path to the model
    
    Methods:
        load_model(): Loads the pipeline of model
    
    """
    def __init__(self, model_path) -> None:
        """
        Initializes a new instance of MLPowerEngine class
        
        Args:
            model_path (str): Raw github path to the model
        """
        self.model_path = model_path

    def load_model(self):
        """
            Fetches the model stored on github and loads the pipeline
        """
        if self.model_path != "" or self.model_path != None:
            r = requests.get(self.model_path)

            if r.status_code == 200:
                return joblib.load(BytesIO(r.content))
            else:
                print("Unable to load the model: ", r.status_code)