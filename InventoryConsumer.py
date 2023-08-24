import pika

class InventoryConsumer:
    def __init__(self, queue_name, exchange_name):
        self.queue_name = queue_name
        self.exchange_name = exchange_name

    @staticmethod
    def create_connection(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
        )
        return connection
    
    def consume_message(self, exchange, routing_key, message):
        connection = InventoryConsumer.create_connection()
        channel = connection.channel()
        channel.queue_declare(
            queue_name='Shipping'
        )
        channel.exchange_declare(
            exchange='AmazonCheckout',
            exchange_type='topic'
        )
        channel.basic_consume(
            exchange='AmazonCheckout',
            routing_key=routing_key,
            body=message
        )
        connection.close()

publisher = InventoryConsumer()
publisher.publish_message('AmazonCheckout', 'cart', 'Sending a message to be consumed')

