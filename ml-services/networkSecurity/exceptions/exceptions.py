import sys
from networkSecurity.logging import logger

class CustomException(Exception):
    def __init__(self, errorMessage, errorDetails:sys):
        self.errorMessage = errorMessage
        _,_,exc_tb = errorDetails.exc_info()
        self.line_no = exc_tb.tb_lineno
        self.fileName = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"\nERROR OCCURED AT\nFileName: '{self.fileName}'\nLineNo: {self.line_no}\nError Message: {self.errorMessage}"
    
if __name__ == "__main__":
    try:
        logger.logging.info("Checking custom exception")
        a = 1/0
    except Exception as e:
        raise CustomException(e, sys)