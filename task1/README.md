Sender отправляет сообщения Receiver'у с помощью rabbitmq, Reciever, в свою очередь, сохраняет сообщения в бд (использовала mongo)
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
Прим. для меня любимой: чтобы осознать, к какой сети подключать Sender'a можно использовать docker network ls
Прим. для преподавателя: я пыталась проверить, действительно ли mongo что-нибудь сохраняет в bd, но docker-compose не выводит ничего из того, что записывается в stdout; различные способы это обойти не сработали (у меня, по крайней мере). 
