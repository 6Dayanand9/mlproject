import sys
from logger import logging

def error_message_detail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name =exc_tb.tb_frame.f_code.co_filename
    error_message = "\n============\nError Ouccured n python script name[{0}]\n------- line number[{1}]-------\n------error message[{2}]-----\n============".format(
        file_name,exc_tb.tb_lineno,str(error)
      
    )
    return error_message
 
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details=error_detail)
    
    def __str__(self):
        return self.error_message
    
if(__name__)=="__main__":
    try:
        1 / 0
    except Exception as e:
        logging.info("Divide By Zero")
        raise CustomException("An error occurred", sys)
    

