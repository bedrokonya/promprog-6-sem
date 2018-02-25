Sender отправляет сообщения receiver'у с помощью rabbitmq, reciever, в свою очередь, сохраняет сообщения в бд (использовала mongo). Reciever, db и rabbit соединяются между собой с помощью docker-compose; sender запускаем отдельно в интерактивном режиме.


Пример запуска:

*(Первая консоль)*
```bash
docker-compose build
docker-compose up
```

*(Вторая консоль)*
```bash
docker build -t sender_tag sender
docker run -it --network=task1_public sender_tag
```
*Прим. для меня любимой*: чтобы осознать, к какой сети подключать Sender'a можно использовать docker network ls
*Прим. для преподавателя*: я пыталась проверить, действительно ли mongo что-нибудь сохраняет в bd, но docker-compose не выводит ничего из того, что записывается в stdout; различные способы это обойти не сработали (у меня, по крайней мере).
