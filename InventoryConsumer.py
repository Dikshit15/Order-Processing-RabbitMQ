import pika


class InventoryConsumner:
    def __init__(self, config):
        self.config = config

    def consume(self, routing_key, message):
        connection = self.create_connection()
        connection.channel()

        channel.exchange_declare(
            exchange=self.config['exchange'],
            exchange_type = 'topic'                
            )

        channel.basic_publish(
            exchange=self.config['exchange'],
            routing_key=routing_key,
            body=message
            )
            
    def create_connection(self):
        param = pika.ConnectionParameters(
            host=self.config['host'],
            port=self.config['port']
        )
        return pika.BlockingConnection(param)

    config = {
        'host': 'localhost',
        'port': 5672,
        'exchange': 'AmazonExchange'
    }
    publisher = CheckoutPublisher(config)
    publisher.publish('inventory', 'data')
    publisher.publish('shipping', 'ship')