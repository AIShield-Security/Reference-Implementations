import time
import logging

logging.basicConfig(level=logging.INFO)

while True:
    logging.info("Microservice log message")
    time.sleep(5)
