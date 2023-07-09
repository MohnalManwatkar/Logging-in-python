import logging

logging.basicConfig(filename='test2.log', level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')

'''
we can use this also in format=
{format='%(asctime)s %(name)s  %(message)s',format='%(asctime)s %(name)s %(levelname)s %(message)s'}
'''

logging.info("this is my log with timestamp")