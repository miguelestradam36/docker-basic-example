# This is the env to be used into the Dockerfile
FROM python:latest
# This is a label
LABEL Maintainer="miguelestradam"
# Copy into docker needed files
COPY app/main.py ./app/main.py
COPY app/tests ./app/tests
COPY app/tox.ini ./app/tox.ini
COPY app/src/ ./app/src/
# Loads data into dockerfile
VOLUME app/data/
# Setting command for application startup
CMD [ "python", "./app/main.py"]