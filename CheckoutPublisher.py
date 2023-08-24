import pika
import sys

class CheckoutPublisher:
    @staticmethod
    def create_connection():
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
        )
        return connection
    
    def publish_message(self, routing_key, message):
        connection = CheckoutPublisher.create_connection()
        channel = connection.channel()
        channel.exchange_declare(
            exchange='AmazonCheckout',
            exchange_type='topic'
        )
        channel.basic_publish(
            exchange='AmazonCheckout',
            routing_key=routing_key,
            body=message
        )
        connection.close()

publisher = CheckoutPublisher()
routing_key = sys.argv[1] if len(sys.argv) > 2 else print("Incomplete input")
message = ' '.join(sys.argv[2:])
publisher.publish_message(routing_key, message)

