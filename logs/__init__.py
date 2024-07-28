import logging
logging.basicConfig(filename= 'log.test.log', level=logging.INFO, format='% (asctime)s - %(name)s - %(levelname)s - '
                                                                         '%(message)s)', datefmt='%Y-%m-%d %H:%M:%S')

logging.info('My name is Daniel')
logging.debug('My name is Alex')
logging.warning('My name is James')



