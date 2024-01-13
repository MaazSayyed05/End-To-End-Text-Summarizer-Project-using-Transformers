
from pathlib import Path

from Text_Summarizer.config import ConfigurationManager
from Text_Summarizer.components.model_evaluation import ModelEvaluation

from Text_Summarizer.logging import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()
    
    
