import unittest
from ml_algorithms.algorithms import MLPowerEngine
from sklearn.datasets import load_iris
import numpy as np


MODEL_PATH = "https://raw.githubusercontent.com/metriccoders/ml-models/main/test_models/rf_classifier_iris.joblib"

class TestMLPowerEngine(unittest.TestCase):
    def setUp(self):
        print("\n Running setup...")
        self.ml_power_engine_1 = MLPowerEngine(MODEL_PATH)
        self.iris = load_iris()
    def test_load_model(self):
        print("\n Running test_load_model...")
        model_pipeline = self.ml_power_engine_1.load_model()
        result = np.array_equal(model_pipeline.predict(self.iris.data), self.iris.target)
        self.assertEqual(result, True)
        
        
if __name__ =='__main__':
    unittest.main()