import os,sys
from auto_encoder.exception import AutoencoderException
from auto_encoder.logger import  logging
from datetime import datetime
from auto_encoder import utils
from typing import List

FILE_NAME = os.getenv('FILE_NAME')
CLEANED_FILE_NAME = os.getenv('CLEANED_FILE_NAME')

class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),'artifacts',f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise AutoencoderException(e,sys)
    

class DataingestionConfig:
    def __init__(self,Training_pipeline_config:TrainingPipelineConfig): 
        try:
            logging.info('configuring all the dataIngestion path variable')
            self.history_file_path:List[str] = utils.get_data_path()
            self.data_ingestion_dir:str = os.path.join(Training_pipeline_config.artifact_dir,'DataIngestion')
            self.data_dir_path:str = os.path.join(self.data_ingestion_dir,'Dataset')
            self.data_file_path:str = os.path.join(self.data_dir_path,FILE_NAME)
            logging.info('successfully configured')
        except Exception as e:
            raise AutoencoderException(e,sys)


class DataCleaningConfig:
    def __init__(self,Training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_cleainig_dir = os.path.join(Training_pipeline_config.artifact_dir,'datacleaning')
            self.data_dir = os.path.join(self.data_cleainig_dir,'cleaned_file')
            self.cleaned_file_path = os.path.join(self.data_dir,CLEANED_FILE_NAME)
        except Exception as e:
            raise AutoencoderException(e,sys)
