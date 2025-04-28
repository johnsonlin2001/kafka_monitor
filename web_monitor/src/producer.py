import time
from kafka import KafkaProducer


def generate_producer(bootstrap_servers, username, password, sasl_mechanism="SCRAM-SHA-256", security_protocol="SASL_SSL", ssl_cafile=None):
    """
    Function that takes in configuration parameters and returns a Kafka producer object. 

    Args:
        bootstrap_servers: String specifying the service URI of the Kafka instance. 
        username: String specifying the SASL username. 
        password: String specifying the SASL password. 
        sasl_mechanism (optional): String specifying the SASL mechanism to use (defaults to SCRAM-SHA-256).
        security_protocol (optional): String specifying the Kafka security protocol to use (defaults to SASL_SSL).
        ssl_cafile: String specifying the path to the CA certificate.

    Returns:
        A configured KafkaProducer object.
    """
    return KafkaProducer(bootstrap_servers=bootstrap_servers, sasl_mechanism=sasl_mechanism, sasl_plain_username=username, sasl_plain_password=password, security_protocol=security_protocol, ssl_cafile=ssl_cafile)

