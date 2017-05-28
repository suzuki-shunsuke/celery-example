# celery-example

celeryを使った簡単な非同期処理のサンプル

* https://www.rabbitmq.com/tutorials/tutorial-one-python.html
* https://hub.docker.com/_/rabbitmq/
* http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

Flaskアプリケーションでリクエストを受け付けてceleryに時間のかかる処理を投げ、
ユーザーには即座にレスポンスを返すサンプル。

## Requirements

* direnv
* pyenv
* Docker Engine
* Docker Compose

## Prepare

```
$ direnv allow
$ pip install pip-tools
$ pip-sync requirements.txt requirements.dev.txt
```

## Run

```
$ docker-compose up  # RebbitMQの起動
$ celery -A tasks worker --loglevel=info  # Celeryの起動
$ python main.py  # Flaskの起動
$ tail -f log.txt  # celeryによって更新されるファイルを監視
$ curl localhost:5000  # Flaskにリクエストを投げる。即座にレスポンスが返ってきて、時間を置いてlog.txtが更新される
```
