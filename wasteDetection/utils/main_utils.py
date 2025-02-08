import os.path
import sys
import yaml
import base64

from wasteDetection.exception import AppException
from wasteDetection.logger import logging


def read_yaml_file(filepath:str) -> dict:
    try:
        with open(filepath, 'rb') as yaml_file:
            logging.info('Read yaml file successfully')
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys) from e 
def write_yaml_file(file_path:str,content:object,replace :bool=False) ->  None:
    try:
        if replace :
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
            logging.info(f'Wrote yaml file successfully to {file_path}')
    except Exception as e:
        raise AppException(e,sys)

def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" * fileName,'wb') as f:
        f.write(imgdata)
        f.close()
        
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())

