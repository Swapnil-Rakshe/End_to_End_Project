import sys
from src.logger import logging


# Define a function to generate detailed error messages
def error_message_detail(error,error_detail:sys):
     # Get the exception traceback
    _,_,exc_tb=error_detail.exc_info()
    
    # Extract the filename and line number from the traceback
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    # Create a detailed error message
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
# Define a custom exception class that provides detailed error messages
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    