import argparse

import pandas as pd
from iris_model.iris import IrisDataProcessing, model_training, model_inference


class IrisRunStep():
    def __init__(self, input_path: str, output_path: str):
        self.processing: IrisDataProcessing
    def run_step(self):

    data_preprocessing.run(config['data'])

    model_training.run(config['model'])

    model_inference.run(config['model'])

if __name__ == "__main__":
    main()