import logging
logging.basicConfig(filename="test3.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')

try:
    with open("sudh.text", 'r'):
        logging.info("this logging will execute when file is open and read")
except Exception as e:
    logging.info("if the file is not open this exception block will execute")
    logging.critical("this is a situation for us")
    logging.warning("this is a warning")
    logging.error(e)
    logging.exception(e)