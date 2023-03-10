from auto_encoder.logger import logging
from auto_encoder.exception import AutoencoderException
import os,sys
from typing import List


def get_data_path()->List[str]:
    try:
        logging.info(f'arranging file path of all chrome history csv files in a list!')
        file_paths = []
        data_dir_path = 'Data/'
        elemnts = os.listdir(data_dir_path)
        for item in elemnts:
            if item.endswith('.csv'):
                file_path = os.path.join('Data/',item)
                file_paths.append(file_path)
        return file_paths    
    except Exception as e:
        raise AutoencoderException(e,sys)
    

def save_text_file(file_path:str, text:str):
    try:
        logging.info(f"saving the cleaned text file")
        dirNames  = os.path.dirname(file_path)
        os.makedirs(dirNames,exist_ok=True)
        with open(file_path,'w') as file:
            file.write(text)
        logging.info(f"successfully saved the cleaned text file !")
    except Exception as e:
        raise AutoencoderException(e,sys)