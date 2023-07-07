import sys
from scr.logger import logging
def error_message_detailed(error,error_detailed:sys):
    _,_,exc_tb = error_detailed.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message ".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detailed(error_message,error_detailed=error_detail)
    
    def __str__(self):
        return self.error_message 