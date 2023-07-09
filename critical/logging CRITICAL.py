import logging
logging.basicConfig(filename='CRITICAL.log', level=logging.CRITICAL, format='%(levelname)s %(asctime)s %(name)s %(message)s')

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
        print(e)

division(3,0)