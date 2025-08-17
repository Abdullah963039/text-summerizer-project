from ai_model.logging import logger
from ai_model.pipline.stage_01_data_ingestion import DataIngestionTrainigPipline
from ai_model.pipline.stage_02_data_validation import DataValidationTrainigPipline
from ai_model.pipline.stage_03_data_transformation import DataTransformationTrainigPipline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainigPipline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} ended <<<<<<<\n\n\t\tx=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainigPipline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} ended <<<<<<<\n\n\t\tx=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Tranformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_tranformation = DataTransformationTrainigPipline()
    data_tranformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} ended <<<<<<<\n\n\t\tx=================x")
except Exception as e:
    logger.exception(e)
    raise e

