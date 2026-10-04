import logging

def get_logger() -> logging.Logger:
    logger = logging.getLogger('inventory_system')
    if not logger.handlers:
        handler = logging.FileHandler('inventory.log', encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
