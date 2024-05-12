import logging

logger = logging.getLogger("gunicorn.error")
logger.setLevel(logging.INFO)


fmt = logging.Formatter("%(asctime)s - %(levelname)s -- %(message)s")
