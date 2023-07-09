import logging
logging.basicConfig(filename='test.log', level=logging.INFO)
    #info
logging.info("this is my very first code for logging")
    #warning
logging.warning("this will try to load warning message")
    #error
logging.error("this is a error message from the system")

l=[1,2,3,4,5,6,7,7]
for i in l:
    if i==2 :
        logging.info(i)     #passing the arguments
        logging.warning(f'this is a warning of a user that they have found {i} in list')    #passing the arguments

logging.shutdown()      #shutdown the  logging