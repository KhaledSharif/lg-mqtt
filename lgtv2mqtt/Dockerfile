FROM node:8.15.1-jessie
RUN  npm install -g lgtv2mqtt
CMD  lgtv2mqtt -v info --tv $TV_IP_ADDRESS --url mqtt://mosquitto
