FROM python:3.5
RUN  pip install paho-mqtt gunicorn falcon
COPY ./main.py /main.py
CMD  cd / && gunicorn -b 0.0.0.0:80 main:api
