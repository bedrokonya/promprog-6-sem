Sender отправляет сообщения receiver'у с помощью очереди rabbitmq; reciever, в свою очередь, сохраняет сообщения в бд (использовала mongo). Reciever, db и rabbit коннектятся между собой с помощью docker-compose; sender коннектим к ним отдельно и запускаем  в интерактивном режиме.


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
*Прим. для преподавателя*: я пыталась проверить, действительно ли mongo что-нибудь сохраняет в базу данных, но docker-compose не выводит ничего из того, что записывается в stdout; различные способы это обойти, которые я смогла нагуглить,  у меня не сработали.
*Прим. для меня любимой*: чтобы осознать, к какой сети подключать Sender'a, можно использовать *docker network ls*.

