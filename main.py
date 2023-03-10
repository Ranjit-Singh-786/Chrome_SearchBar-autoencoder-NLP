from auto_encoder.logger import logging
from auto_encoder.exception import AutoencoderException
import os,sys

# write  this code to test the logging and exception handling
if __name__=="__main__":
    try:
        logging.info(f"entering  in try block")
        a =  5
        b = 0
        c  = a/b
        print(c)
        logging.info('try block executed successfully !')
    except Exception as e:
        raise AutoencoderException(e,sys)