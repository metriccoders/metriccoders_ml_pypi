# Metric Coders Model Loader

## Overview

Welcome to Metric Coders Model Loader PyPI Package source code. Your one-stop solution for effortlessly loading machine learning models directly from GitHub repository of Metric Coders Model Hub. This Python package is designed to simplify the process of fetching and integrating pre-trained models hosted on GitHub, allowing you to focus on the magic of your machine learning applications.

## Features

- **GitHub Integration**: Seamlessly fetch machine learning models hosted on GitHub with just a few lines of code.
- **Versatility**: Compatible with various machine learning frameworks and models stored in GitHub repositories.
- **Easy to Use**: Minimal setup and intuitive functions for quick integration into your projects.
- **Customizable**: Adapt the loading process to suit your specific project requirements.

## Installation

```bash
pip install metriccoders_ml
```

## Usage

### Load a Model from GitHub

```python
from ml_algorithms.algorithms import MLPowerEngine
from sklearn.datasets import load_iris

# Specify the GitHub repository URL
repo_url = "https://raw.githubusercontent.com/metriccoders/ml-models/main/classifiers/adaboostclassifier_10/model64_0.32271997615954084_SAMME.R/model.joblib"

# Load the model from GitHub
engine = MLPowerEngine(repo_url)
ml_engine = engine.load_model()
iris = load_iris()
print(ml_engine.predict(iris.data))
```


## Contribution

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to submit a pull request.

### How to run unittest
```bash
python -m unittest discover
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Support

For any questions, issues, or feedback, please open an [issue](https://github.com/metriccoders/metriccoders_ml_pypi/issues).

Let's make loading machine learning models from Metric Coders Model Hub a breeze! 🚀