import json
import os
import signal
import sys
import time
import logging

import schedule
from dotenv import load_dotenv

from producer import generate_producer
from request import send_request
from config import SITES_LIST, REQUEST_INTERVAL

# Load environment variables from .env file. 
load_dotenv()

kafka_username = os.getenv("SASL_USERNAME")
kafka_password = os.getenv("SASL_PASSWORD")
bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS")
topic_name = os.getenv("TOPIC_NAME")
ssl_cafile = os.getenv("SSL_CAFILE")

# Configure logging to show when information is written.
logging.basicConfig(level=logging.INFO, format="%(message)s : %(asctime)s")


def close_producer(producer):
    def close(signal_number, stack_frame):
        """
        Function that closes a Kafka producer gracefully.
        """
        producer.flush()
        producer.close()
        sys.exit(0)
    return close


def check_sites(producer):
    """
    Checks the list of specified sites and writes information to a Kafka topic.
    """
    for site in SITES_LIST:
        url = site["url"]
        regex = site.get("regex")
        response = send_request(url, regex)
        message = json.dumps(response)
        producer.send(topic_name, message.encode("utf-8"))
    producer.flush()
    logging.info("checked website statuses")


if __name__ == "__main__":
    # Create a Kafka producer using the configured variables. 
    kafka_producer = generate_producer(bootstrap_servers, kafka_username, kafka_password, ssl_cafile=ssl_cafile)

    # Register close_producer to run on signal interrupt. 
    signal.signal(signal.SIGINT, close_producer(kafka_producer))

    # Periodically checks websites and writes information until signal interrupt.
    schedule.every(REQUEST_INTERVAL).seconds.do(check_sites, kafka_producer)

    while True:
        schedule.run_pending()
        time.sleep(1)


