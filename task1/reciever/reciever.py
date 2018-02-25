import pika
from time import sleep
import mongoengine


print("** Start receive... **")

mongoengine.connect('task1', host='db')
class Message(mongoengine.Document):
    text = mongoengine.StringField(required=True)

parameters = pika.ConnectionParameters('rabbit')
connection = None
while connection is None:
    try:
        connection = pika.BlockingConnection(parameters)
    except pika.exceptions.ConnectionClosed:
        sleep(4.2)

my_channel = connection.channel()
my_channel.queue_declare(queue='my_queue')


for _, _, body in my_channel.consume('my_queue'):
    Message(text=body).save()
    print("** Saved message: %s **", body)


#проверяем, что мы что-то записали в бд
for text in Message.objects:
    print("** %s **", text)

