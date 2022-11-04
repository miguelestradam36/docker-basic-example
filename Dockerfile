FROM python:latest
LABEL Maintainer="miguelestradam"
COPY app/main.py ./app/main.py
COPY app/main.py ./app/setup.py
COPY app/src/ ./app/src/
VOLUME app/data/

CMD [ "python", "./app/main.py"]