import sys
import logging


def error_message_details(error, error_details: sys):
    """
    Return a formatted string with filename, line number and original message.
    """
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    return "Error occurred in python script [{0}] at line [{1}] : {2}".format(
        file_name, line_no, str(error)
    )


class CustomException(Exception):
    def __init__(self, error, error_details: sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_details)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e, sys)
