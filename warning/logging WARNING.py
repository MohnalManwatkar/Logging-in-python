import logging
logging.basicConfig(filename='WARNING.log', level=logging.WARNING, format='%(levelname)s %(asctime)s %(name)s %(message)s')

def division(a,b):
    logging.info("the number entered by user is %s and %s", a,b)
    try:
        logging.info("we are into the try block")
        div = a/b
        logging.info("this line is print when div=a/b opration performs successflly")
        logging.info("result of the code is %s", div)
        return div
    except Exception as e:
        logging.exception(e)

division(3,0)