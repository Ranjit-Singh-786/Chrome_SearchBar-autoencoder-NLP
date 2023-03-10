from auto_encoder.logger import logging
from auto_encoder.exception import AutoencoderException
from auto_encoder.entity import config_entity,artifact_entity
import os,sys
import pandas as pd
import numpy as np

class DataIngestion:
    def __init__(self,dataingestionconfig:config_entity.DataingestionConfig):
        try:
            self.dataingestionconfig = dataingestionconfig
        except Exception as e:
            raise AutoencoderException(e,sys)
        
    