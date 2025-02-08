from wasteDetection.logger import logging 
from wasteDetection.exception import AppException
import sys


try:
    a = 6/"a"
except Exception as e:
    raise AppException(e,sys)


