import logging

# create logger with 'best_stocks'
logger = logging.getLogger('best_stocks')

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

# create file handler which logs info messages
file_handler = logging.FileHandler('app.log')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
