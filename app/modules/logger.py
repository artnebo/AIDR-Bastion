import logging
import logging.handlers
from queue import Queue

log_queue = Queue()

pipeline_logger = logging.getLogger("pipeline")
pipeline_logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()

formatter = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")
console_handler.setFormatter(formatter)

queue_handler = logging.handlers.QueueHandler(log_queue)

pipeline_logger.addHandler(queue_handler)

listener = logging.handlers.QueueListener(log_queue, console_handler)
listener.start()
