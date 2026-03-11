import logging
import os
from datetime import datetime


def get_logger():

    logger = logging.getLogger("FlightBookingLogger")
    logger.setLevel(logging.INFO)

    # Create logs folder if not exists
    log_folder = "logs"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Log file name with timestamp
    log_file = os.path.join(
        log_folder,
        f"test_log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
    )

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger