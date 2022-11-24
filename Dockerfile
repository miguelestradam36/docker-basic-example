FROM python:latest
LABEL Maintainer="miguelestradam"
COPY app/main.py ./app/main.py
COPY app/tests ./app/tests
COPY app/tox.ini ./app/tox.ini
COPY app/src/ ./app/src/
VOLUME app/data/

CMD [ "python", "./app/main.py"]