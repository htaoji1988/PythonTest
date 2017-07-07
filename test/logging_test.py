import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                    level=logging.INFO, filename='../logs/test.txt')

logging.info('start program!')
logging.info('Trying to divide 1 by 0')
try:
    print(1 / 0)
except Exception as e:
    logging.error('wrong!')

logging.info('The division successes')
logging.info('')
