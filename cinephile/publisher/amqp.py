from cinephile.core import PublisherInferface
import logging
import sys
import json
from pika import BlockingConnection, URLParameters, BasicProperties
from pika.exceptions import AMQPConnectionError, UnroutableError


class AMQPPublisher(PublisherInferface):
    def __init__(self, url: str, exchange: str, routing_key: str):
        try:
            self.conn = BlockingConnection(parameters=URLParameters(url))
            self.channel = self.conn.channel()
            logging.info(f'Successfully connected to AMQP Broker at [{url}]')
            self.exchnage = exchange
            self.routing_key = routing_key
            # Declare the queue
            self.channel.queue_declare(routing_key, durable=True)
            self.channel.confirm_delivery()
        except AMQPConnectionError:
            logging.error(f'Couldn\'t connect to the AMQP broker at [{url}]')
            sys.exit(2)

    def publish(self, event: dict) -> bool:
        properties = BasicProperties(content_type='text/json', delivery_mode=1)
        args = {
            'exchange': self.exchnage,
            'routing_key': self.routing_key,
            'body': json.dumps(event),
            'properties': properties,
            'mandatory': True,
        }
        try:
            self.channel.basic_publish(**args)
        except UnroutableError:
            logging.error('Message was returned')
