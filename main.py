
from Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Text_Summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Text_Summarizer.pipeline.stage_04_model_training import ModelTrainingPipeline
from Text_Summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

from Text_Summarizer.logging import logger



STAGE_NAME=  "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>>>> Initialize {STAGE_NAME}  <<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>> Completed {STAGE_NAME} Successfully  <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
    



STAGE_NAME =  "Data Validaiton Stage"
try:
    logger.info(f">>>>>>>>>>>>> Initialize {STAGE_NAME}  <<<<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>>>> Completed {STAGE_NAME} Successfully  <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME =  "Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>>>>> Initialize {STAGE_NAME}  <<<<<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>>>>> Completed {STAGE_NAME} Successfully  <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME =  "Model Training Stage"
try:
    logger.info(f">>>>>>>>>>>>> Initialize {STAGE_NAME}  <<<<<<<<<<<<<")
    # model_trainer = ModelTrainingPipeline()
    # model_trainer.main()
    logger.info(f">>>>>>>>>>>>> Completed {STAGE_NAME} Successfully  <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME =  "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>>>>>>> Initialize {STAGE_NAME}  <<<<<<<<<<<<<")
    # model_evaluation = ModelEvaluationPipeline()
    # model_evaluation.main()
    logger.info(f">>>>>>>>>>>>> Completed {STAGE_NAME} Successfully  <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e





