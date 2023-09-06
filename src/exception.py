import sys                                                                   # any exception that is basically getting controlled,  the sys library will automatically have the information
from src.logger import logging


#for error message details, how error mesaage should be displayed w.r.t custom exception
def error_message_detail(error,error_detail:sys):                             # whenerror an exception gets raised, it  will pushed as own custom message
    _,_,exc_tb=error_detail.exc_info()                                        # the first two fields we are not interested in, next will give us error detail, exc_tb will tell on which file /line exception has occured
    file_name=exc_tb.tb_frame.f_code.co_filename                              # insde the exc_tb, we will be having tb_frame, f_code and co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
# when the above error raise, this particular function is called

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    

    #when we raise a custom exception, it will print  the error message itself
    def __str__(self):
        return self.error_message