import logging
import config


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    level = config.Environment.log_level
    logger.setLevel(level)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # File handler with UTF-8 encoding
    file_handler = logging.FileHandler(f"{name}.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


logger = get_logger("application")
