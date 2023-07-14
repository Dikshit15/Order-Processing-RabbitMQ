import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue)



def sendMessage(queue_name, msg):
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=msg
    )