from auto_encoder.logger import logging
from auto_encoder.exception import AutoencoderException
from auto_encoder.entity import config_entity,artifact_entity
from auto_encoder.component.DataIngestion import DataIngestion
from auto_encoder.component.DataCleaning import DataCleaning
import os,sys
from auto_encoder import utils

# write  this code to test the logging and exception handling
if __name__=="__main__":
    try:
        TrainingPipelineObj = config_entity.TrainingPipelineConfig()
        DataingestionConfigObj = config_entity.DataingestionConfig(
            Training_pipeline_config=TrainingPipelineObj
        )
        DataIngestionObj = DataIngestion(dataingestionconfig=DataingestionConfigObj)
        DataIngestionArtifact = DataIngestionObj.initiateingestion()

        DataCleaningConfig = config_entity.DataCleaningConfig(Training_pipeline_config=TrainingPipelineObj)
        DataCleaningObj = DataCleaning(datacleaningconfig=DataCleaningConfig,
                                       dataingestionartifact=DataIngestionArtifact)
        DataCleaningObj.initiate_datacleaning()

    except Exception as e:
        raise AutoencoderException(e,sys)