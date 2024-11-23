from src.ds_project import logger
from src.ds_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e