import pika


class CheckoutPublisher:
    def __init__(self, config):
        self.config = config

    def publish(self, routing_key, message):
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
        'exchange': 'AmazonQueue'
    }
    
publisher = CheckoutPublisher(config)
publisher.publish('inventory', 'Reconfigure inventory for order')
publisher.publish('shipping', 'Ship order to address')