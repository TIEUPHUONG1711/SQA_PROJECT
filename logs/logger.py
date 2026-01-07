import logging
import os

def get_logger():
    logger = logging.getLogger("SQA_LOGGER")
    logger.setLevel(logging.INFO)

    # tránh add handler nhiều lần
    if logger.handlers:
        return logger

    log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "sqa_run.log")

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # 1️⃣ File handler (ghi toàn bộ log)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # 2️⃣ Console handler (hiện terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(levelname)s - %(message)s")
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
