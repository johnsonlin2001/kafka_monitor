# Web Monitor

This is a Python web monitoring tool which acts as a producer that periodically checks websites for their status and sends the result to a Kafka topic. 

## Setup and usage instructions

1. Clone the project repository and cd into the web_monitor directory. 

2. It is recommended to use a virtual environment for this project. 
```bash
python3 -m venv venv_name
source venv/bin/activate 
```

3. Install the project dependencies within the web_monitor directory.
```bash
pip install -r requirements.txt
```

4. Create a .env inside the src directory with the following variables: 
BOOTSTRAP_SERVERS = bootstrap-url:port
SASL_USERNAME = sasl-username
SASL_PASSWORD = sasl-password
TOPIC_NAME = topic-name
SSL_CAFILE = path-to-ca.pem-from-src

# Note that these are all placeholders and should be filled in with the values from your Kafka configuration.
It is recommended to place your ca.pem inside the src directory and set SSL_CAFILE = ca.pem for simplicity. 

5. Edit config.py to specify website targets and the time interval between checks. 

6. To initiate monitoring, execute the run.py script inside src. Use Ctrl+C to stop the script.
```bash
python3 run.py
```

It will provide basic logging showing when information is written to the Kafka topic. 

## Testing
This project provides some basic unit tests defined in the test directory. 

To run these tests, execute "python3 -m unittest" from the project root directory (web_monitor).

## LLM Usage
In order to speed up development, I used LLM assistance to familiarize myself with the kafka-python package. 
Namely, to better understand the KafkaProducer object and associated APIs. 


