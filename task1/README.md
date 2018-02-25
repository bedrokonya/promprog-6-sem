Sender отправляет сообщения Receiver'у с помощью rabbitmq, Reciever в свою очередь сохраняет сообщения в бд (использовала mongo)
Пример запуска:
(Первая консоль)
```bash
docker-compose build
docker-compose up
```
(Вторая консоль)
```bash
docker build -t sender_tag sender
docker run -it --network=task1_public sender_tag
```
