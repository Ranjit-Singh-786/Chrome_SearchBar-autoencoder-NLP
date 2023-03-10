from auto_encoder.logger import logging
from auto_encoder.exception import AutoencoderException
from auto_encoder.entity import config_entity,artifact_entity
import os,sys
import pandas as pd
import numpy as np

class DataIngestion:
    def __init__(self,dataingestionconfig:config_entity.DataingestionConfig,):
        try:
            self.dataingestionconfig = dataingestionconfig
        except Exception as e:
            raise AutoencoderException(e,sys)
    

    def merge_files(self)->pd.DataFrame:
        try:
            list_of_file_path = self.dataingestionconfig.history_file_path
            df = pd.read_csv(list_of_file_path[0])
            df2 = pd.read_csv(list_of_file_path[1])
            logging.info(f"merging the histories files in a one file..")
            merged_df = pd.merge(left=df,right=df2,how='outer')
            title = merged_df[['title']]
            return title
        except Exception as e:
            raise AutoencoderException(e,sys)
        

    def initiateingestion(self)->artifact_entity.DataCleaningArtifact:
        try:
            logging.info(f"initiating DataIngestion")
            directory_path = self.dataingestionconfig.data_dir_path
            os.makedirs(directory_path,exist_ok=True)
            titles = self.merge_files()
            ingestion_file_path = self.dataingestionconfig.data_file_path
            titles.to_csv(ingestion_file_path,index=False,header=True)
            dataingestionartifact = artifact_entity.DataIngestionArtifact(
                merge_df_path=self.dataingestionconfig.data_file_path
            )
            logging.info(f"initiated DataIngestion")
            return dataingestionartifact
        except Exception as e:
            raise AutoencoderException(e,sys)

    