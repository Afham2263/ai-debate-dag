import logging

logging.basicConfig(
    filename="debate_log.txt",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_message(message: str):
    logging.info(message)
