from auto_encoder.logger import logging
from auto_encoder.exception import AutoencoderException
import os,sys
from auto_encoder import utils

# write  this code to test the logging and exception handling
if __name__=="__main__":
    try:
        list_of_file_path = utils.get_data_path()
        print(list_of_file_path)     
        logging.info('try block executed successfully !')
    except Exception as e:
        raise AutoencoderException(e,sys)