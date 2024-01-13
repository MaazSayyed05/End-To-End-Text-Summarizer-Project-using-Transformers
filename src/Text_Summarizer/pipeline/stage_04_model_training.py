
from pathlib import Path

from Text_Summarizer.config import ConfigurationManager
from Text_Summarizer.components.model_trainer import ModelTrainer

from Text_Summarizer.logging import logger


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
