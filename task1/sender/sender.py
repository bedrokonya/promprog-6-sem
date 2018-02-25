import pika
import sys
import time


print("** Start sending... **")
print()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
channel = connection.channel()
print("Connection established\n")

for line in sys.stdin:
    channel.basic_publish(exchange='',
                          routing_key='my_queue',
                          body=line)

channel.close()
connection.close()

