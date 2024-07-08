import yaml
from src import data_preprocessing, model_training, model_inference

def main():
    with open("config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    data_preprocessing.run(config['data'])

    model_training.run(config['model'])

    model_inference.run(config['model'])

if __name__ == "__main__":
    main()